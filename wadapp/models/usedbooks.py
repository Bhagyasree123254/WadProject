from django.db import models
from .category import Category



class Usedbook(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=1000000, default='',null=True, blank=True)
    aboutauthor = models.CharField(max_length=1000000, default='',null=True, blank=True)
    image = models.ImageField(upload_to='usedbooks/')
    preview = models.FileField(upload_to='usedbooks_previews/')

    @staticmethod
    def get_all_usedbooks():
        return Usedbook.objects.all()

    @staticmethod
    def get_all_usedbooks_by_id(category_id):
        if category_id:
            return Usedbook.objects.filter(category=category_id)
        else:
            return Usedbook.get_all_usedbooks();

    @staticmethod
    def get_usedbooks_by_name(name):
        if name:
            return Usedbook.objects.filter(name=name)
        else:
            return Usedbook.get_all_usedbooks();


    @staticmethod
    def get_usedbooks_by_id(ids):
        return Usedbook.objects.filter(id__in=ids)

