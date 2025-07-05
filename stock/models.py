from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    producat_name=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.CharField(max_length=300)
    product_image=models.ImageField(upload_to='photos/product/')
    stock=models.IntegerField(default=1)
    price=models.IntegerField()
    is_availabe=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.producat_name
    
    def get_url(self):
        return reverse ('product_deatil',args=[self.category.slug,self.slug])

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variation_category='color',is_active=True)
    def sizes(self):
        return super(VariationManager,self).filter(variation_category='size',is_active=True)
variation_category_choise=(('color','color'),('size','size'),
)

class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=50,choices=variation_category_choise)
    variation_value=models.CharField(max_length=50)
    is_active=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    objects=VariationManager()

    def __str__(self):
        return self.variation_value
