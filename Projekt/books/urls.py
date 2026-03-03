from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("", views.BookListView.as_view(), name="list"),
    path("dodaj/", views.book_create, name="create"),
    path("<int:pk>/edytuj/", views.book_edit, name="edit"),
    path("<int:pk>/usun/", views.book_delete, name="delete"),
]
