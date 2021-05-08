from django.db import models

class Customer(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    pswd1 =models.CharField(max_length=50)
    pswd2 =models.CharField(max_length=50)
    def register(self):
        self.save()
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False
    @staticmethod
    def get_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False
    @staticmethod
    def get_by_password(pswd1):
        return Customer.objects.filter(pswd1=pswd1)

