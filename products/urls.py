from django.urls import path
from .views import product_list, product_detail, add_to_cart, user_cart, delete_cart


urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('user-cart/', user_cart, name='user_cart'),
    path('delete-cart/', delete_cart, name='delete_cart')
]