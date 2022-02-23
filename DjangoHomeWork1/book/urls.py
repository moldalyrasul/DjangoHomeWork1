from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path("books/<int:id>/update/", views.BookUpdateView.as_view(), name="book_update"),
    path("books/<int:id>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
    path("add-book/", views.BookCreateView.as_view(), name="add_book")
]

