from django.db import models
from django import forms

def uploaded_location(instance, filename):
    return ("%s/%s") %(instance.car_name,filename)

class Car(models.Model):
    image = models.ImageField(upload_to=uploaded_location,null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    car_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    num_of_seats = models.IntegerField()
    cost_par_day = models.CharField(max_length=50)
    content = models.TextField()
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return "/car/%s/" % (self.id)

class Order(models.Model):
    car_name = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    cell_no = models.CharField(max_length=15)
    address = models.TextField()
    date = models.DateTimeField()
    to = models.DateTimeField()

    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return "/car/detail/%s/" % (self.id)

class PrivateMsg(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()