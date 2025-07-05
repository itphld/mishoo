from django.shortcuts import render
from .models import Product
from category.models import Category
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.
def product(request,cat_slug=None):
    if cat_slug!=None:

        product=Product.objects.all().filter(is_availabe=True,category__slug=cat_slug)
        paginator=Paginator(product,3)
        page_number = request.GET.get("page")
        paginated_product=paginator.get_page(page_number)
        product_count=product.count()
    else:
        product=Product.objects.all().filter(is_availabe=True)
        paginator=Paginator(product,3)
        page_number = request.GET.get("page")
        paginated_product=paginator.get_page(page_number)
        product_count=product.count()

    context={'products':paginated_product,'product_count':product_count}

    return render(request,'product/product.html',context)


def prodcut_detail(request,category_slug,product_slug):

    single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    context={'single_product':single_product}
    return render(request,'product\product_detail.html',context)

def search(request):
    #return HttpResponse('search apge')
    keyword=request.GET['keyword']
    if keyword:
        products=Product.objects.order_by('-created_on').filter(Q(description__icontains=keyword)|Q(producat_name__icontains=keyword))
        paginator=Paginator(products,3)
        page_number = request.GET.get("page")
        paginated_product=paginator.get_page(page_number)
        product_count=products.count()
        context={'products':paginated_product,'product_count':product_count}
    return render(request,'product/product.html',context)
