from django.db import models
from django.contrib.auth.models import User
from owner.models import Books


# Create your models here.
# relationships:
# 1.one to one.
# 2.one to many. ==> Foreignkey

class Carts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Books, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    options = (
        ("incart", "incart"),
        ("cancelled", "cancelled"),
        ("order_placed", "order_placed")
    )
    status = models.CharField(max_length=150, choices=options, default="incart")


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Books, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    date = models.DateField(auto_now=True)
    options = (
        ("order_placed", "order_placed"),
        ("dispatched", "dispatched"),
        ("in_transit", "in_transit"),
        ("delivered", "delivered"),
        ("cancelled", "cancelled")
    )
    status = models.CharField(max_length=50, choices=options, default="order_placed")