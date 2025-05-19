from django.urls import path
from django.views.generic import RedirectView

from .views import *


app_name = 'core'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='core:products', permanent=False)),
    path('about/', about, name='about'),
    path('about/core/', about_core, name='core-about'),

    path('products/', products, name='products'),
]
