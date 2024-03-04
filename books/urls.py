from django.urls import path

from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='create_book'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='bood_edit'),
]