from django.db import models
from .product import Product
from .customer import Customer
from .usedbooks import Usedbook
from .new_releases import New_releases
import datetime


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)
    usedbook = models.ForeignKey(Usedbook, on_delete=models.CASCADE,default=150)
    newbook = models.ForeignKey(New_releases, on_delete=models.CASCADE,default=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    return_status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order \
            .objects \
            .filter(customer=customer_id) \
            .order_by('-date')

    @staticmethod
    def get_orders_by_id(ids):
        return Order.objects.filter(id__in=ids)
