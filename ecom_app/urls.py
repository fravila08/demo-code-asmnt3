from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("inventory/<str:category>", views.displayItems),
    path("addItemToCart/<int:id>", views.add_to_cart),
    path('cart', views.myCart),
]