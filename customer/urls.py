from django.urls import path
from customer import views

urlpatterns = [
    path('all/', views.ListAllView.as_view(), name="all_books"),
    path('account/signup', views.SignUpView.as_view(), name="signup"),
    path('', views.SignInView.as_view(),name="signin"),
    path("account/signout", views.sign_out,name="signout"),
    path('customer/carts/add/<int:id>',views.AddToCartView.as_view(),name='addtocart'),
    path('customer/carts/items/', views.CartItems.as_view(), name='cartitems'),
    path('customer/carts/items/<int:id>',views.RemoveCartItems.as_view(), name='removecartitem')

]
