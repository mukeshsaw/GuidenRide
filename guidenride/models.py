from django.db import models
from datetime import datetime
# from django.db import migrations, models

class DateTime(models.Model):
    id = models.AutoField
    day = models.IntegerField(default="")
    month = models.IntegerField(default="")
    year = models.IntegerField(default="")
    second = models.IntegerField(default="")
    minute = models.IntegerField(default="")
    hour = models.IntegerField(default="")

    # def __str__(self):
    #     return self.product_name

class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,default="")
    email = models.CharField(max_length=50, default="")
    day = models.IntegerField(default="")
    month = models.IntegerField( default="")
    year = models.IntegerField(default="")
    phone = models.CharField(max_length=10, default="")
    country = models.CharField(max_length=25, default="")
    desc = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.name

# class OurTours(models.Model):
#     id = models.AutoField
#     passenger = models.IntegerField(default="")
#     date = models.DateField(blank=True, null=True)
#     time = models.TimeField(default="")
#     tour = models.CharField(max_length=50, default="")
#     price = models.CharField(max_length=50,default="")
#     total = models.CharField(max_length=50, default="")
#
#     def __str__(self):
#         return "OurTours"


class Book(models.Model):
    id = models.AutoField
    # tour_id = models.IntegerField(default="")
    passenger = models.IntegerField(default="")
    date = models.DateField(default="")
    time = models.TimeField(default="")
    tour = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=50, default="")
    total = models.CharField(max_length=50, default="")

    def __str__(self):
        return "Book"

class Tour(models.Model):
    tour_id = models.AutoField(primary_key=True)
    passenger = models.IntegerField(default="")
    tour = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=50, default="")
    total = models.CharField(max_length=50, default="")

    def __str__(self):
        return "Tour"

class BookTour(models.Model):
    booktour_id = models.AutoField(primary_key=True)
    passenger = models.IntegerField(default="")
    tour = models.CharField(max_length=50, default="")
    date = models.DateField(default="")
    time = models.TimeField(default="")
    price = models.CharField(max_length=50, default="")
    total = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=10, default="")
    country = models.CharField(max_length=25, default="")
    desc = models.CharField(max_length=500, default="")
    def __str__(self):
        return name