from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

import cart
from cart.contexts import cart_contents


# Create your views here.
def view_cart(request):
    cart_items = cart_contents(request)
    return render(request, "cart/cart.html", context=cart_items)


def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    print(quantity)

    cart = request.session.get('cart', {})
    print(cart)
    if id in cart:
        if cart[str(id)] != quantity:
            cart[id] = quantity

    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    print(cart)

    return redirect(reverse('cart:view_cart'))


def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('cart:view_cart'))


def empty_cart(request):
    request.session['cart'] = {}
    return redirect(reverse('cart:view_cart'))
