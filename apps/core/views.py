from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from apps.core.models import Product


# Create your views here.
def hello(request):
    return HttpResponse("Hello everyone!")


@require_http_methods(['GET', 'POST'])
def products(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        amount = request.POST.get('amount')

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            amount=amount
        )

        return redirect('core:products')

    products_list = Product.objects.all()

    context = {
        'products': products_list
    }

    return render(request, 'core/pages/products.html', context)


def about(request):
    return render(request, 'about_project.html')


def about_core(request):
    return render(request, 'core/about_core.html')
