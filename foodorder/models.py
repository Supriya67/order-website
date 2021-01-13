from django.db import models
from useraccounts.models import UserProfile
import datetime
# Create your models here.
class OurSpeciality(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    veg = models.BooleanField(default=False)
    non_veg = models.BooleanField(default=False)
    best_seller=models.BooleanField(default=True)
    cart = models.BooleanField(default=False)
    order = models.BooleanField(default=False)


class TodaySpecial(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    veg = models.BooleanField(default=False)
    non_veg = models.BooleanField(default=False)
    best_seller=models.BooleanField(default=True)
    cart = models.BooleanField(default=False)
    order = models.BooleanField(default=False)


class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

class Product(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category , on_delete=models.CASCADE, default=1)
    veg=models.BooleanField(default=False)
    non_veg = models.BooleanField(default=False)
    bestseller = models.BooleanField(default=False)
    offerzone = models.BooleanField(default=False)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()



class Orders(models.Model):
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=500,default="")
    phone = models.CharField(max_length=50,default="")
    date=models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeorder(self):
        self.save()

    @staticmethod
    def get_orders_by_user(user_id):
        return Orders.objects.filter(user_id=user_id).order_by('-date')