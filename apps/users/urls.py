from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from . import views

app_name = 'users'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('list/', views.UserListView.as_view(), name='user-list'),
    path('list/<int:pk>', views.ChangeUserGroupView.as_view(), name='change-group'),

    path('profile/', RedirectView.as_view(pattern_name='core:products', permanent=False))
]
