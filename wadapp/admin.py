from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.new_releases import New_releases

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminNew(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
# Register your models here.


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(New_releases, AdminNew)
