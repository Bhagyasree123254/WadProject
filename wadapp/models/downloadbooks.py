from django.db import models
from .category import Category



class DownloadBook(models.Model):
    name=models.CharField(max_length=50)
    dlprice=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='download_books/')
    preview = models.FileField(upload_to='download_books_previews/')
    download = models.FileField(upload_to='download_books_pdf/')

    @staticmethod
    def get_all_downloadbooks():
        return DownloadBook.objects.all()

    @staticmethod
    def get_downloadbooks_by_name(name):
        if name:
            return DownloadBook.objects.filter(name=name)
        else:
            return DownloadBook.get_all_downloadbooks()