from django.contrib import admin
from .models import Product
from django.utils.html import format_html
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src={} width=50>'.format(object.product_image.url))
    prepopulated_fields={'slug':('producat_name',)}
    list_display=('producat_name','category','description','is_availabe','thumbnail')
    list_display_links=('producat_name','category','description','thumbnail')
    list_editable=('is_availabe',)
    list_filter=('category',)

admin.site.register(Product,ProductAdmin)
