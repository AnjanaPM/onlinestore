from django.shortcuts import render, redirect
from django.http import HttpResponse
from owner.models import Books
from django.views.generic import View, ListView
from customer.form import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from customer.decorators import sign_in
from customer.models import Carts
from django.db.models import Sum


# Create your views here.
@method_decorator(sign_in, name="dispatch")
class ListAllView(View):
    # @sign_in
    def get(self, req):
        qs = Books.objects.all()
        context = {"books": qs}
        return render(req, "listallbooks.html", context)


class SignUpView(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {"form": form}
        return render(request, 'signup.html', context)

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("saved!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return render(request, 'signup.html')
        else:
            context = {"form": form}
            return render(request, 'signup.html', context)


class SignInView(View):
    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        return render(request, 'signin.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("all_books")
            else:
                context = {"form": form}
                return render(request, "signin.html", context)


def sign_out(request):
    logout(request)
    return redirect("signin")


class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        qs = Books.objects.get(id=id)
        user = request.user
        cart = Carts(user=user, item=qs)
        cart.save()
        print("item saved !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return redirect("all_books")


class CartItems(ListView):
    model = Carts
    template_name = 'cart_item.html'
    context_object_name = 'items'

    def get(self, request, *args, **kwargs):
        qs = self.model.objects.filter(user=self.request.user).exclude(status="cancelled")
        total = qs.aggregate(Sum("item__price"))

        print(total)
        sum = total["item__price__sum"]
        context = {"items": qs, "sum": sum}
        return render(request, self.template_name, context)


class RemoveCartItems(View):
    def get(self, request, *args, **kwargs):
        id = kwargs["id"]
        cart = Carts.objects.get(id=id)
        cart.status = "cancelled"
        cart.save()
        return redirect("all_books")



