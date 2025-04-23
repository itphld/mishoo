from django.shortcuts import render
from stock.models import Product
def home(request):
    product=Product.objects.all().filter(is_availabe=True)
    context={'products':product}
    return render(request,'home.html',context)
