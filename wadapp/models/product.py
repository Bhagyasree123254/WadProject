from django.db import models
from .category import Category


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=1000000, default='', null=True, blank=True)
    aboutauthor = models.CharField(max_length=1000000, default='', null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    preview = models.FileField(upload_to='previews/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products();

    @staticmethod
    def get_products_by_name(name):
        if name:
            return Product.objects.filter(name=name)
        else:
            return Product.get_all_products();

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
