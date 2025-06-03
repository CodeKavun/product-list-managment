from django.urls import path
from django.views.generic import RedirectView

from .views import *


app_name = 'core'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='core:welcome', permanent=False)),
    path('welcome/', welcome, name='welcome'),
    path('about/', about, name='about'),

    path('products/', products, name='products'),
    path('products/<int:pk>/', ProductsDetails.as_view(), name='product-details'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    path('brands/', brands, name='brands'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand-delete'),

    path('categories/', categories, name='categories'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete')
]
