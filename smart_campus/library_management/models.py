from django.db import models


class books_to_be_bought(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=40, choices=[("approved", "approved"), ("pending", "pending")], default="pending")
    remarks = models.CharField(max_length=2000, default="nothing")


class Inventory(models.Model):
    Budget = models.IntegerField(default=50000)


class Books(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
