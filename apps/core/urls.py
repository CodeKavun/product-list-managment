from django.urls import path

from .views import *


urlpatterns = [
    path('', hello, name='hello'),
    path('about/', about, name='about'),
    path('about/core/', about_core, name='core-about')
]
