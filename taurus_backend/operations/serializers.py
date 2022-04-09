from rest_framework import serializers

from django.contrib.auth.models import User
from . models import Customer, Status, Order, Review

from pprint import pprint


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        field = (
            "username",
            "password",
            "first_name",
            "last_name"
        )

    def save(self):
        user = User(
            username=self.validated_data["username"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            password=self.validated_data["password"]
        )

        u = user.save()
        pprint(u)
        return user
        # customer = self.context["customer"]
        # self.email_address = customer["email_address"]
        # self.address = customer["address"]
        # self.cellphone_number = customer["cellphone_number"]
        # #super(UserSerializer).save(self, **kwargs)
        # super(UserSerializer, self).save()

    # def create(self, validated_data):
    #     user = User(
    #         username=validated_data["username"],
    #     )
    #     user.set_password(validated_data["password"])
    #     user_id = user.save()
    #     Customer.objects.create(
    #         user=user_id,
    #         email=validated_data["email"],
    #         address=validated_data["address"],
    #         cellphone_number=validated_data["cellphone_number"]
    #     )
    #     return validated_data


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        depth = 3
        fields = '__all__'
        field = (
            "user",
            "email",
            "address",
            "cellphone_number"
        )


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        field = (
            "name",
            "code",
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        field = (
            "id",
            "customer_id",
            "is_delivery",
            "address",
            "is_far",
            "order_date_time",
            "delivery_data",
            "delivery_time",
            "custom_pizzas",
            "half_meter_pizzas",
            "beverages",
            "status",
            "notes",
            "total_price"
        )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        field = (
            "customer_id",
            "order_id",
            "title",
            "description",
            "stars"
        )

