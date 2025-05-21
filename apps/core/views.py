from sys import prefix

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django import views
from django.views.decorators.http import require_http_methods

from apps.core.forms import ProductForm
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
        image = request.POST.get('image')

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            amount=amount,
            image=image
        )

        return redirect('core:products')

    products_list = Product.objects.all()

    context = {
        'products': products_list
    }

    return render(request, 'core/pages/products.html', context)


class ProductsDetails(views.View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product_form = ProductForm(instance=product, prefix='product')
        context = {
            'product': product,
            'product_form': product_form
        }
        return render(request, 'core/pages/product-details.html', context)

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product_form = ProductForm(instance=product)

        if product_form.is_valid():
            product_form.save()
            return redirect('product-details', pk=pk)

        return redirect('product-details', pk=pk)


def about(request):
    return render(request, 'about_project.html')


def about_core(request):
    return render(request, 'core/about_core.html')
