from django.urls import path
from .import views

urlpatterns = [
    path('',views.product,name='product'),
    path('<slug:cat_slug>/',views.product,name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.prodcut_detail,name='product_deatil')

]
