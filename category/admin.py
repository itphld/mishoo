from django.contrib import admin
from .models import Category
from django.utils.html import format_html
class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src={} width=50>'.format(object.category_image.url))
    prepopulated_fields={'slug':('category_name',)}
    list_display=('category_name','description','created_on','thumbnail')
    ordering=('-category_name',)

# Register your models here.
admin.site.register(Category,CategoryAdmin)
