from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login_view),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]