from django.db import models
from django.urls import reverse
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    category_image=models.ImageField(upload_to='photos/category/')
    description=models.CharField(max_length=300)
    created_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.category_name
    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

# Create your models here.
