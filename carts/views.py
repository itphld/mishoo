from django.shortcuts import render,redirect
from stock.models import Product,Variation
from carts.models import Cart,CartItem
from django.http import HttpResponse
# Create your views here.
def _cart_id(request):
    if request.user.is_authenticated:
        try:
            cart=Cart.objects.get(user=request.user, is_active=True)
        except Cart.DoesNotExist:
            cart=Cart.objects.create(user=request.user, is_active=True)


        return cart
    else:
        # unique session identifier
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
            
        cart, created = Cart.objects.get_or_create(cart_id=session_key, user__isnull=True, is_active=True)
        return cart

def add_cart(request,product_id):

    product=Product.objects.get(id=product_id)

    product_variation=[]
    if request.method == 'POST':
        #for item in request.POST:
            #key=item
            #value=request.POST[key]


        for key, value in request.POST.items():
            print(f"{key}: {value}")

            try:
                variation=Variation.objects.get(product=product,variation_category__iexact=key,variation_value__iexact=value)
                #print(variation)
                product_variation.append(variation)
            except:
                pass

        #color=request.POST['color']
        #size=request.POST['size']
        #print(color,size)
    #color=request.GET['color']
    #size=request.GET['size']
    #return HttpResponse(color+' '+size)


    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))



    except Cart.DoesNotExist:
        cart=Cart.objects.create(
        cart_id=_cart_id(request),
        )
        cart.save()
    cart_items = CartItem.objects.filter(product=product, cart=cart)


    for item in cart_items:

        existing_variations = list(item.variations.all())
        if set(existing_variations) == set(product_variation):

            item.quantity += 1
            item.save()
            break
    else:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
            )
        if product_variation:
            cart_item.variations.set(product_variation)
        cart_item.save()
    return redirect('cart')
def delete_cart(request,product_id,cart_item_id):
    product=Product.objects.get(id=product_id)
    cart=Cart.objects.get(cart_id=_cart_id(request))
    cartitem=CartItem.objects.get(product=product,cart=cart,id=cart_item_id)


    if cartitem.quantity>0:
        cartitem.quantity-=1
        cartitem.save()
    else:
        cartitem.delete()
    return redirect('cart')

def remove_cart(request,product_id,cart_item_id):
    product=Product.objects.get(id=product_id)
    cart=Cart.objects.get(cart_id=_cart_id(request))
    cartitem=CartItem.objects.get(product=product,cart=cart,id=cart_item_id)
    cartitem.delete()
    return redirect('cart')
def cart (request):
    total=0
    tax=0
    g_total=0
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cartitems=CartItem.objects.filter(cart=cart)
        for cartitem in cartitems:
            total+=(cartitem.product.price*cartitem.quantity)
        tax=total*0.2
        g_total=total+tax
        context={'cartitem':cartitems,'total':total,'tax':tax,'g_total':g_total}
        return render (request,'product/cart.html',context)


    except Cart.DoesNotExist:
        pass
        return render(request,'product/cart.html')
