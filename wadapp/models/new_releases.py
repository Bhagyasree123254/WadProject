from django.db import models
from .category import Category



class New_releases(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='',null=True,blank=True)
    about_author=models.CharField(max_length=200,default='')
    image=models.ImageField(upload_to='uploads/new_releases/')


    @staticmethod
    def get_all_newreleases():
        return New_releases.objects.all()
