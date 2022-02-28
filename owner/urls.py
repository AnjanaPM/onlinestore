from django.urls import path
from owner import views

#
# urlpatterns = [
#     path('home', views.owner_home),
#     path('books/add', views.add_book),
#     path('books/all', views.list_book),
#     path('books/<int:id>',views.book_detail)

# ]
urlpatterns = [
    path("books/add", views.AddBookView.as_view(), name="addbook"),
    path("books/all", views.BookListView.as_view(), name="booklist"),
    path("books/<int:id>", views.BookDetailView.as_view(), name='bookdetail'),
    path("books/all/<int:id>", views.BookEditView.as_view(), name="bookedit"),
    path("books/delete/<int:id>", views.BookDeleteView.as_view(), name='bookdelete')

]
