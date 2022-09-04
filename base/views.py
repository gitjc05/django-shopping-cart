from itertools import product
from unicodedata import name
from django.shortcuts import render, redirect
from . import models
import random
import string

# Create your views here.

def l_form(strt):
    nl = []
    tmp = ""
    incorrect = ['"', "'", ",", "[", "]", " "]
    for x in strt:
        if x not in incorrect:
            tmp += x
        if x == "]" or x == ",":
            nl.append(tmp)
            tmp = ""
            
    return nl

def get_items():
    items = models.Product.objects.all()
    nl = []
    for x in items:
        nl.append(
            {
                "name": x.name,
                "price": x.price,
                "sizes": l_form(x.sizes)
            }
        )
    return nl

def items(request):
    items = get_items()
    context = {
        "items": items
    }
    
    response =  render(request, "base/items.html", context)
    alphabet = string.ascii_lowercase
    set_cook_usr = random.choices(alphabet, k=10)
    
    try:
        user_id = request.COOKIES["user_id"]
        set_cook_usr = "".join(set_cook_usr)
        print(request.COOKIES["user_id"])
    except KeyError:
        set_cook_usr = "".join(set_cook_usr)
        response.set_cookie("user_id", set_cook_usr)
        user_id = request.COOKIES["user_id"]
        print(request.COOKIES["user_id"])
        return response
    if request.method == "POST":
        name1 = request.POST.get("item")
        if "create-item" in request.POST:            
            models.Product.objects.create(
                name=request.POST.get("name"),
                price=request.POST.get("price")
            )
                
            return response
        else:
            if models.UserItem.objects.filter(name1=name1, user=user_id):
                quant2 = models.UserItem.objects.filter(name1=name1).get(user=user_id)
                quant1 = quant2.quantity + 1

                models.UserItem.objects.filter(name1=name1).filter(user=user_id).update(quantity=quant1)
            else:
                models.UserItem.objects.create(
                    user=user_id,
                    name1=models.Product.objects.get(name=request.POST.get("item")).name,
                    product=models.Product.objects.get(name=request.POST.get("item"))
                )
            return response
    return response

def cart(request):
    user_id = request.COOKIES["user_id"]
    items = models.UserItem.objects.filter(user=user_id)
    context = {
        "cart_items": items
    }
    
    if request.method == "POST":
        if "add_cart" in request.POST:
            user_item = request.POST.get("updateItem")
            user_id = request.COOKIES["user_id"]
            newquant = int(request.POST.get("inputQuant"))
            models.UserItem.objects.filter(user=user_id).filter(name1=user_item).update(quantity=newquant)
            return redirect("cart")

        if "remove" in request.POST:
            print("deleting")
            user_id = request.COOKIES["user_id"]
            print("found user")
            user_item = request.POST.get("updateItem")
            print("found user item")
            models.UserItem.objects.filter(user=user_id).filter(name1=user_item).delete()
            print("deleted")
            return redirect("cart")
    return render(request, "base/cart.html", context)