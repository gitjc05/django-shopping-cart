from django.urls import path
from . import views

urlpatterns = [
    path("", views.items, name="items"),
    path("cart/", views.cart, name="cart")
]