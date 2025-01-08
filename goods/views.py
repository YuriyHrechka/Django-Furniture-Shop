from django.shortcuts import render


def catalogue(request):
    return render(request, 'goods/catalog.html')


def products(request):
    return render(request, 'goods/product.html')
