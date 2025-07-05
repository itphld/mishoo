from django.db import models
from stock.models import Product,Variation
from account.models import Account
# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=300,blank=True)
    user = models.ForeignKey(Account, null=True, blank=True, on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    variations=models.ManyToManyField(Variation,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.product.producat_name
    def sub_total(self):
        return self.product.price*self.quantity
