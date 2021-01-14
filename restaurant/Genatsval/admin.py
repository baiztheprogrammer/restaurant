from django.contrib import admin
from .models import Meal
from .models import Order
from .models import Staff


# Register your models here.
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(Staff)


