# bakery_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class BakeryItem(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='BakeryItemIngredient')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class BakeryItemIngredient(models.Model):
    bakery_item = models.ForeignKey(BakeryItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_percentage = models.FloatField()

    def __str__(self):
        return f"{self.bakery_item.name} - {self.ingredient.name}"


class Order(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    items = models.ManyToManyField(BakeryItem)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"


class CustomUser(AbstractUser):
    # Add fields as needed for your user model
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    def __str__(self):
        return self.username
