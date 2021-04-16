from django.db import models
from .category import Category

class Main_book(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='main_books')

    @staticmethod
    def get_all_main_books():
        return Main_book.objects.all()