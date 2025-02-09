from django.db import transaction
from django.core.exceptions import ValidationError
from orders.models import Order, OrderItem
from carts.models import Cart


def create_order_for_user(user, form_data):
    """
    Створює замовлення для користувача на основі даних форми та товарів у кошику.

    :param user: Користувач, для якого створюється замовлення.
    :param form_data: Очислені дані форми з полями: phone_number, requires_delivery,
                      delivery_address, payment_on_get.
    :return: Створене замовлення (Order).
    :raises: ValidationError, якщо не вистачає товарів на складі або кошик порожній.
    """
    with transaction.atomic():
        cart_items = Cart.objects.filter(user=user)

        if not cart_items.exists():
            raise ValidationError("Ваш кошик порожній!")

        # Створення замовлення
        order = Order.objects.create(
            user=user,
            phone_number=form_data['phone_number'],
            requires_delivery=form_data['requires_delivery'],
            delivery_address=form_data['delivery_address'],
            payment_on_get=form_data['payment_on_get'],
        )

        # Створення замовлених товарів
        for cart_item in cart_items:
            product = cart_item.product
            name = product.name
            price = product.sell_price()
            quantity = cart_item.quantity

            if product.quantity < quantity:
                raise ValidationError(
                    f'Недостатня кількість товарів {name} на складі. '
                    f'В наявності - {product.quantity}'
                )

            OrderItem.objects.create(
                order=order,
                product=product,
                name=name,
                price=price,
                quantity=quantity,
            )

            # Оновлюємо залишок товару
            product.quantity -= quantity
            product.save()

        # Очищуємо кошик після створення замовлення
        cart_items.delete()

        return order
