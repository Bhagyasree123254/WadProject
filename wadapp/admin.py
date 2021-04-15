from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.main_books import Main_book
from .models.customer import Customer
from .models.new_releases import New_releases
from .models.downloadbooks import DownloadBook

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

class AdminMainBooks(admin.ModelAdmin):
    list_display = ['name', 'category']

class AdminNew(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminDownloadBooks(admin.ModelAdmin):
    list_display = ['name','dlprice', 'category']

admin.site.register(Customer)
# Register your models here.


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Main_book, AdminMainBooks)
admin.site.register(New_releases, AdminNew)
admin.site.register(DownloadBook,AdminDownloadBooks)
