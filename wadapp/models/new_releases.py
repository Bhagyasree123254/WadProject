from django.db import models
from .category import Category


class New_releases(models.Model):
    id = models.IntegerField(primary_key=True)
    id_number = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=2000000, default='', null=True, blank=True)
    about_author = models.CharField(max_length=2000000, default='')
    image = models.ImageField(upload_to='new_releases/')
    preview = models.FileField(upload_to='new_releases_previews/')

    @staticmethod
    def get_all_newreleases():
        return New_releases.objects.all()

    @staticmethod
    def get_newreleases_by_name(name):
        if name:
            return New_releases.objects.filter(name=name)
        else:
            return New_releases.get_all_newreleases();

    @staticmethod
    def get_newreleases_by_id(ids):
        return New_releases.objects.filter(id__in=ids)
