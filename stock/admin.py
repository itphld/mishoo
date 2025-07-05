from django.contrib import admin
from .models import Product,Variation
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
class VariationAdmin(admin.ModelAdmin):
    list_display=('product','variation_category','variation_value','is_active','created_on')
    list_display_links=('product','variation_category','created_on')
    list_editable=('is_active',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)
