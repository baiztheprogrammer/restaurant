from .models import Meal
from rest_framework import serializers
from .models import Order


class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = '__all__'

    def get_price_sale(self,to_representation):
        pass

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'




