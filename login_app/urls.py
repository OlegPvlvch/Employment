from django.urls import path
from django.contrib.auth import views as v
from . import views

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', v.LogoutView.as_view(), name='logout')
]