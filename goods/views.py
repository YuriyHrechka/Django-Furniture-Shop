from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from goods.models import Products


def catalogue(request, category_slug, page=1):
    if category_slug == 'all':
        goods = goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context: dict[str, str] = {
        'title': 'Home - Каталог',
        'goods': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalogue.html', context)


def product(request, product_slug: str):
    product = Products.objects.get(slug=product_slug)

    context: dict[str, Products] = {
        'product': product,
    }

    return render(request, 'goods/product.html', context)
