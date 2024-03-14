from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

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
            comment_form = CommentForm
    else:
        comment_form = CommentForm()

    # context
    context = {
        'book': book,
        'comments': book_comment,
        'comment_form': comment_form,
    }

    return render(request, 'books/book_detail.html', context)


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/create_book.html'

    # You can use form method if you want
    # form_class = NewBookForm


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
