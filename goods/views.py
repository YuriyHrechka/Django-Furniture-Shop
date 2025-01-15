from django.shortcuts import render, get_list_or_404
from goods.models import Products


def catalogue(request, category_slug):
    if category_slug == 'all':
        goods = goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    context: dict[str, str] = {
        'title': 'Home - Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalogue.html', context)


def product(request, product_slug: int):
    product = Products.objects.get(slug=product_slug)

    context: dict[str, Products] = {
        'product': product,
    }

    return render(request, 'goods/product.html', context)
