from django.shortcuts import render
from .models import Product
from category.models import Category

# Create your views here.
def product(request,cat_slug=None):
    if cat_slug!=None:

        product=Product.objects.all().filter(is_availabe=True,category__slug=cat_slug)

        product_count=product.count()
    else:
        product=Product.objects.all().filter(is_availabe=True)
        product_count=product.count()
    context={'products':product,'product_count':product_count}

    return render(request,'product/product.html',context)


def prodcut_detail(request,category_slug,product_slug):

    single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    context={'single_product':single_product}
    return render(request,'product\product_detail.html',context)
