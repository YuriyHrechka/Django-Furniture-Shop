from django.shortcuts import render

goods = [
    {'image': 'deps/images/goods/set of tea table and three chairs.jpg',
     'name': 'Чайний столик і три стільці',
     'description': 'Комплект із трьох стільців і дизайнерський столик для вітальні кімнати.',
     'price': 150.00},

    {'image': 'deps/images/goods/set of tea table and two chairs.jpg',
     'name': 'Чайний столик і два стільці',
     'description': 'Набір зі столу та двох стільців у мінімалістичному стилі.',
     'price': 93.00},

    {'image': 'deps/images/goods/double bed.jpg',
     'name': 'Двоспальне ліжко',
     'description': 'Ліжко двоспальне з надголовником і взагалі дуже ортопедичне.',
     'price': 670.00},

    {'image': 'deps/images/goods/kitchen table.jpg',
     'name': 'Кухонний стіл з раковиною',
     'description': 'Кухонний стіл для обіду з вбудованою раковиною і стільцями.',
     'price': 365.00},

    {'image': 'deps/images/goods/kitchen table 2.jpg',
     'name': 'Кухонний стіл з вбудовуванням',
     'description': 'Кухонний стіл із вбудованою плитою та раковиною. Багато полиць і взагалі красивий.',
     'price': 430.00},

    {'image': 'deps/images/goods/corner sofa.jpg',
     'name': 'Кутовий диван для вітальні',
     'description': 'Кутовий диван, розкладається в двоспальне ліжко, для вітальні та прийому гостей саме те!',
     'price': 610.00},

    {'image': 'deps/images/goods/bedside table.jpg',
     'name': 'Приліжковий столик',
     'description': 'Приліжковий столик з двома висувними шухлядами (квітка не входить до комплекту).',
     'price': 55.00},

    {'image': 'deps/images/goods/sofa.jpg',
     'name': 'Диван звичайний',
     'description': 'Диван, він же софа звичайна, нічого примітного для опису.',
     'price': 190.00},

    {'image': 'deps/images/goods/office chair.jpg',
     'name': 'Стілець офісний',
     'description': 'Опис товару, про те який він класний, але це стілець, що тут сказати...',
     'price': 30.00},

    {'image': 'deps/images/goods/plants.jpg',
     'name': 'Рослина',
     'description': 'Рослина для прикраси вашого інтер\'єру подарує свіжість і безтурботність обстановці.',
     'price': 10.00},

    {'image': 'deps/images/goods/flower.jpg',
     'name': 'Квітка стилізована',
     'description': 'Дизайнерська квітка (можливо штучна) для прикраси інтер\'єру.',
     'price': 15.00},

    {'image': 'deps/images/goods/strange table.jpg',
     'name': 'Приліжковий столик',
     'description': 'Столик, доволі дивний на вигляд, але підходить для розміщення поруч із ліжком.',
     'price': 25.00},
]


def catalogue(request):
    context: dict[str, str] = {
        'title': 'Home - Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalogue.html', context)


def products(request):
    return render(request, 'goods/product.html')
