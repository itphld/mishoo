from django.urls import path
from .import views

urlpatterns = [
path('',views.cart,name='cart'),
path('add_cart/<int:product_id>/',views.add_cart,name='add_cart'),
path('delete_cart/<int:product_id>/<int:cart_item_id>/',views.delete_cart,name='delete_cart'),
path('remove_cart/<int:product_id>/<int:cart_item_id>/',views.remove_cart,name='remove_cart'),
]
