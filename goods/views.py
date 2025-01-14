from django.shortcuts import render
from goods.models import Products


def catalogue(request):
    goods = Products.objects.all()

    context: dict[str, str] = {
        'title': 'Home - Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalogue.html', context)


def products(request):
    return render(request, 'goods/product.html')
