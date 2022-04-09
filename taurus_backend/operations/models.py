from django.db import models

from django.contrib.auth.models import User, AbstractBaseUser
from menu.models import CustomPizza, HalfMeterPizza, Beverage


# class Customer(AbstractBaseUser):
#     is_staff = models.BooleanField(default=False)
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     # TODO validate email with regex
#     email = models.CharField(max_length=50)
#     address = models.CharField(max_length=100)
#     cellphone_number = models.CharField(max_length=20)
#
#     # TODO change username field to email
#     USERNAME_FIELD = "username"


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # TODO validate email with regex
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    cellphone_number = models.CharField(max_length=20)

    # TODO change username field to email
    # USERNAME_FIELD = "username"


class Status(models.Model):
    # ex. to do, doing, delivered
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True, null=True)


class Order(models.Model):
    customer_id = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    is_delivery = models.BooleanField(default=True)
    address = models.CharField(max_length=100)
    is_far = models.BooleanField(default=False)
    order_date_time = models.DateTimeField()
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    custom_pizzas = models.ManyToManyField(CustomPizza)
    half_meter_pizzas = models.ManyToManyField(HalfMeterPizza)
    beverages = models.ManyToManyField(Beverage)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )
    notes = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)


class Review(models.Model):
    customer_id = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    order_id = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    stars = models.IntegerField()
