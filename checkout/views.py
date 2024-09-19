from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cart.contexts import cart_contents
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from books.models import Book
from django.utils import timezone


def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Book, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()
                print('hereeee')

            messages.error(request, "You have successfully paid")
            request.session['cart'] = {}
            return redirect(reverse('cart:view_cart'))
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    cart_items = cart_contents(request)
    return render(request, "checkout/checkout.html",
                  {'cart_items': cart_items['cart_items'],
                   'order_form': order_form, 'payment_form': payment_form,
                   'total': cart_items['total'],
                   'product_count': cart_items['product_count']})
