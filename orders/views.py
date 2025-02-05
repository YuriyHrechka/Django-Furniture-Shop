from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Створення замовлення
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        # Створення замовлених товарів
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостатня кількість товарів {name} на складі'
                                                      f'В наявності - {product.quantity}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )

                            product.quantity -= quantity
                            product.save()

                        # Очищуєм кошик користувача після створення замовлення
                        cart_items.delete()

                        messages.success(request, 'Замовлення оформлено!')
                        return redirect('user:profile')
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('user:order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        form = CreateOrderForm(data=initial)

    context = {
        'title': 'Home - Оформлення замовлення',
        'form': form,
    }
    return render(request, 'orders/create_order.html', context=context)
