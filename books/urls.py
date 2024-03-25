from django.urls import path

from .views import BookListView, book_create_view, BookUpdateView, BookDeleteView, book_detail_view

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', book_detail_view, name='book_detail'),
    path('create/', book_create_view, name='create_book'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
