from django.db import models
from goods.models import Products
from users.models import User


class OrderitemQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.product_price() for cart in self.all())

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self.all())
        return 0


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None,
                             verbose_name='Користувач')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення замовлення')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефону')
    requires_delivery = models.BooleanField(default=False, verbose_name='Потрібна доставка')
    delivery_address = models.TextField(null=True, blank=True, verbose_name='Адреса доставки')
    payment_on_get = models.BooleanField(default=False, verbose_name='Оплата при отриманні')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    status = models.CharField(max_length=50, default='Обробляється', verbose_name='Статус замовлення')

    class Meta:
        db_table = 'order'
        verbose_name = 'Замовлення'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"Замовлення № {self.pk} | Покупець {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Замовлення')
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, verbose_name='Продукт',
                                default=None)
    name = models.CharField(max_length=150, verbose_name='Назва')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ціна')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажу')

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Проданий товар'
        verbose_name_plural = 'Продані товари'

    objects = OrderitemQueryset.as_manager()

    def products_price(self):
        return round(self.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Товар"
