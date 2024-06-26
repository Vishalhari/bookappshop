from django.db import models
from adminpanelapp.models import Book

# Create your models here.
class Userprofile(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)


class Logins(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
    usertype = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)


class Carts(models.Model):
    user =  models.OneToOneField(Logins,on_delete=models.CASCADE)

    items = models.ManyToManyField(Book)


class Cartitems(models.Model):
    cart = models.ForeignKey(Carts,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='items')
    quantity = models.PositiveIntegerField(default=1)


