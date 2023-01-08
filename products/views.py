from django.shortcuts import render


# Create your views here.


def index(request):
    context = {
        'title': 'Store',
        'is_promotion': True,
    }
    return render(
        request,
        'products/index.html',
        context,
    )


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
            {
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'name': 'Синяя куртка The North Face',
                'price': 6090,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
        ]
    }
    return render(
        request,
        'products/products.html',
        context,
    )
