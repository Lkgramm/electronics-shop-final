from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('category/<slug:category_slug>/', views.product_list, name='product-list-by-category'),
    path('product/<int:pk>/', views.product_detail, name='product-detail'),
]