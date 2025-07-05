from .models import Cart,CartItem
from .views import _cart_id



def counter(request):
    cart_count=0
    cart=Cart.objects.filter(cart_id=_cart_id(request))
    if cart:

        cartitem=CartItem.objects.filter(cart=cart.first())
        for cartitem in cartitem:
            cart_count+=cartitem.quantity

    return dict(cart_count=cart_count)
