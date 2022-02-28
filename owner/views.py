from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.http import HttpResponse
from owner.forms import BookForm
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from owner.models import Books
from customer.decorators import owner_permission_required
from django.utils.decorators import method_decorator


# Create your views here.

class AddBookView(CreateView):
    model = Books
    form_class = BookForm
    template_name = "addbook.html"
    success_url = reverse_lazy("booklist")
    # def get(self, request, *args, **kwargs):
    #     form = BookForm()
    #     return render(request, "addbook.html", {"form": form})
    #
    # def post(self, request, *args, **kwargs):
    #     form = BookForm(request.POST, files=request.FILES)
    #
    #     if form.is_valid():
    #         # print(form.cleaned_data)
    #         form.save()
    #         print("saved!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #         return render(request, "addbook.html")
    #     else:
    #         return render(request, "addbook.html", {"form": form})


@method_decorator(owner_permission_required, name='dispatch')
class BookListView(ListView):
    model = Books
    context_object_name = 'books'
    template_name = 'listbook.html'
    # def get(self, request):
    #     qs = Books.objects.all()
    #     context = {"books": qs}
    #     return render(request, "listbook.html", context)


class BookDetailView(DetailView):
    model = Books
    context_object_name = "book"
    template_name = 'bookdetail.html'
    pk_url_kwarg = "id"
    # def get(self, request, **kwargs):
    #     print(kwargs)
    #     id = kwargs.get("id")
    #     qs = Books.objects.get(id=id)
    #     return render(request, "bookdetail.html", {"book": qs})


class BookEditView(UpdateView):
    model = Books
    template_name = 'bookedit.html'
    form_class = BookForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('booklist')

    # def get(self, request, **kwargs):
    #     id = kwargs.get("id")
    #     qs = Books.objects.get(id=id)
    #     form = BookForm(instance=qs)
    #     context = {"form": form}
    #     return render(request, "bookedit.html", context)

    def post(self, request, **kwargs):
        id = kwargs.get("id")
        qs = Books.objects.get(id=id)
        form = BookForm(request.POST, files=request.FILES, instance=qs)
        if form.is_valid():
            form.save()
            print("inside save!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return render(request, "bookedit.html")
        else:
            print("form error!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return render(request, "bookedit.html", {"form": form})


class BookDeleteView(View):

    def get(self, request, **kwargs):
        id = kwargs.get("id")
        qs = Books.objects.get(id=id)
        qs.delete()
        books = Books.objects.all()
        context = {"book": qs, "books": books}
        return render(request, "listbook.html", context)
        # return redirect("booklist")

# class based views and function based views
# from owner.models import books
#
#
# def owner_home(request):
#     return render(request, "index.html")
#
#
# def add_book(request):
#     if request.method == "GET":
#         print("inside get")
#         return render(request, "addbook.html")
#     else:
#         print("inside post")
#         print(request.method)
#         return render(request, "addbook.html")
#
#
# def list_book(request):
#     context = {"books": books}
#     return render(request, "listbook.html", context)
#
#
# def book_detail(request, id):
#     book = [i for i in books if i["id"] == id]
#     context = {"book": book}
#     return render(request, "bookdetail.html", context)
