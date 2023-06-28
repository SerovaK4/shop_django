from django.shortcuts import render

from catalog.models import Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': "Главная"
    }
    return render(request, "catalog/index.html", context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name}, {phone}: {message}")
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    print(request)
    context = {
        'object_list': Product.objects.get(pk=pk),
        'title': 'Карточка товара'
    }
    return render(request, 'catalog/product.html', context)
