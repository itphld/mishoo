from django.urls import path
from .import views

urlpatterns = [
    path('',views.product,name='product'),
    path('category/<slug:cat_slug>/',views.product,name='product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/',views.prodcut_detail,name='product_deatil'),
    path('search/',views.search,name='search')

]
