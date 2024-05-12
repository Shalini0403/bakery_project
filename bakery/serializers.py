from rest_framework import serializers
from .models import Ingredient, BakeryItem, Order, CustomUser


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class BakeryItemSerializer(serializers.ModelSerializer):
    ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = BakeryItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

