from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from menu.models import CustomPizza, HalfMeterPizza, Beverage
from pprint import pprint

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
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="customer"
    )
    # TODO validate email with regex
    email_address = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    cellphone_number = models.CharField(max_length=20)

    def __str__(self):
        # TODO aggiungi nome cliente
        return "Cliente " + self.user.first_name + self.user.last_name


@receiver(post_save, sender=User)
def create_user_customer(sender, instance, created, **kwargs):
    if created:
        print("post_save instance ROBBEN")
        pprint(vars(instance))
        prova = Customer.objects.create(
            user=instance
        )
        pprint(vars(prova))


@receiver(post_save, sender=User)
def save_user_customer(sender, instance, **kwargs):
    instance.customer.save()


class Status(models.Model):
    # ex. to do, doing, delivered
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True, null=True)

    def __str__(self):
        return "Stato " + self.name


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

    def __str__(self):
        return "Ordine " + self.id


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

    def __str__(self):
        return "Recensione " + self.id
