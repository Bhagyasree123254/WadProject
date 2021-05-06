from django.db import models

class Review(models.Model):
    emailid = models.EmailField(max_length=50,default='Anonymous')
    bookname = models.CharField(max_length=50,default='',blank=True,null=True)
    reviews = models.CharField(max_length=500)
    rating = models.IntegerField(default=4)
    def register(self):
        self.save()

    @staticmethod
    def get_all_reviews():
        return Review.objects.all()

    @staticmethod
    def get_review_by_email(emailid):
        return Review.objects.filter(emailid=emailid)
