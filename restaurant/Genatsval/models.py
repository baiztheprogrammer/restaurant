from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Meal(models.Model):
    rate = (
        ('5/5','5/5'),
        ('4/5','4/5'),
        ('3/5','3/5'),
        ('2/5','2/5'),
        ('1/5','1/5'),
    )

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    rate = models.CharField(max_length=20,choices=rate)
    image = models.ImageField()
    sale = models.BooleanField()

    def __str__(self):
        return self.meal.name

class Order(models.Model):
    status = (
        ('Ready','Ready'),
        ('In_process','In_process'),
        ('Not_ready','Not_ready'),
    )
    meal = models.ForeignKey(Meal,on_delete=models.SET_NULL,null=True,related_name='orders')
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=status)
    table = models.IntegerField()
    staff = models.ForeignKey('Staff',on_delete=models.SET_NULL,null=True,related_name='staff')

class Staff(models.Model):
    role = (
        ('Chef','Chef'),
        ('Waiter','Waiter'),
        ('Manager','Manager'),
    )

    exp = (
        ('Beginner','Beginner'),
        ('Intermediate','Intermediate'),
        ('Master','Master'),
    )

    user = models.OneToOneField(User,on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20,choices=role)
    exp = models.CharField(max_length=20,choices=exp)
    image = models.ImageField()
    date_entry = models.DateTimeField(auto_now_add=True)

