from abc import ABC

from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


from .models import Book
from .forms import NewBookForm, CommentForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 6
    ordering = ['-id']
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# class BookDetailView(generic.DeleteView):
#     model = Book
#     template_name = 'books/book_detail.html'
@login_required
def book_detail_view(request, pk):
    # get_book_object
    book = get_object_or_404(Book, pk=pk)
    # get book comment
    book_comment = book.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    # context
    context = {
        'book': book,
        'comments': book_comment,
        'comment_form': comment_form,
    }

    return render(request, 'books/book_detail.html', context)


@login_required()
def book_create_view(request):
    if request.method == 'POST':
        book_form = NewBookForm(request.POST)
        if book_form.is_valid():
            new_book = book_form.save(commit=False)
            new_book.user = request.user
            new_book.save()
            return redirect('book_list')
    else:
        book_form = NewBookForm()

    contex = {
            'form': book_form
        }

    return render(request, 'books/create_book.html', contex)


# class base create
# class BookCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Book
#     fields = ['user', 'title', 'author', 'description', 'price', 'cover', ]
#     template_name = 'books/create_book.html'


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
