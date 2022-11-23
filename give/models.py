from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=125)

class Institution(models.Model):
    name=models.CharField(max_length=125)
    description=models.CharField(max_length=125)
    type=models.Choices
    categories=models.ManyToManyField(Category)

class Donation(models.Model):
    quantity=models.IntegerField
    categories=models.ManyToManyField(Category)
    adress=models.CharField(max_length=125)
    phone_number=models.IntegerField
    city=models.CharField(max_length=125)
    zip_code=models.IntegerField
    pick_up_date=models.IntegerField
    pick_up_time=models.IntegerField
    pick_up_comment=models.CharField(max_length=125)
    user=models.ForeignKey()