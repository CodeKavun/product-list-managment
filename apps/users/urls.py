from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('sign-up/', '', name='sign-up'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
