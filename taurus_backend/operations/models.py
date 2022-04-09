from django.db import models
from django.contrib.auth import models as auth_models
from django.template.defaultfilters import last

from menu.models import CustomPizza, HalfMeterPizza, Beverage
from pprint import pprint


class UserManager(auth_models.BaseUserManager):

    def create_user(self, email, password, first_name, last_name, is_staff=False, is_superuser = False):
        if not email:
            raise ValueError("User must have an email")

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user

    def create_superuser(self, email, password, first_name="", last_name=""):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        user.save()
        return user


class User(auth_models.AbstractUser):
    # TODO validate email with regex
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    username = None
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    cellphone_number = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        # TODO aggiungi nome cliente
        return "Cliente " + self.first_name + " " + self.last_name


class Status(models.Model):
    # ex. to do, doing, delivered
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True, null=True)

    def __str__(self):
        return "Stato " + self.name


class Order(models.Model):
    user_id = models.ForeignKey(
        User,
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
    user_id = models.ForeignKey(
        User,
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
        return "Recensione " + self.title
