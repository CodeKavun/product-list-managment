from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import UpdateView, DetailView, DeleteView

from apps.core.forms import ProductForm, CategoryForm, BrandForm
from apps.core.models import Product, Category, Brand


# Create your views here.
def welcome(request):
    return render(request, 'core/pages/welcome.html')


@require_http_methods(['GET', 'POST'])
def products(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        amount = request.POST.get('amount')
        image = request.FILES.get('image')
        brand = request.POST.get('brand')
        category = request.POST.get('category')


        Product.objects.create(
            name=name,
            description=description,
            price=price,
            amount=amount,
            image=image,
            brand_id=brand,
            category_id=category
        )

        return redirect('core:products')

    products_list = Product.objects.all()
    product_form = ProductForm()

    context = {
        'products': products_list,
        'product_form': product_form
    }

    return render(request, 'core/pages/products.html', context)


def brands(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        Brand.objects.create(
            name=name
        )

        return redirect('core:brands')

    brand_list = Brand.objects.all()
    brand_form = BrandForm()

    context = {
        'brands': brand_list,
        'brand_form': brand_form,
        'user_role': request.user.groups.all()[0].name
    }

    return render(request, 'core/pages/brands.html', context)


def categories(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        Category.objects.create(
            name=name
        )

        return redirect('core:categories')

    category_list = Category.objects.all()
    category_form = CategoryForm()

    context = {
        'categories': category_list,
        'category_form': category_form,
        'user_role': request.user.groups.all()[0].name
    }

    return render(request, 'core/pages/categories.html', context)


class ProductsDetails(DetailView):
    model = Product
    template_name = 'core/pages/product-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_role'] = self.request.user.groups.all()[0].name
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'core/pages/product-edit.html'
    success_url = reverse_lazy('core:products')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('core:products')
    template_name = 'core/pages/product-delete.html'


class BrandDeleteView(DeleteView):
    model = Brand
    success_url = reverse_lazy('core:brands')
    template_name = 'core/pages/brand-delete.html'


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('core:categories')
    template_name = 'core/pages/category-delete.html'


def about(request):
    return render(request, 'about_project.html')


def about_core(request):
    return render(request, 'core/about_core.html')
