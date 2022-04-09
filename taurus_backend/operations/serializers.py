from rest_framework import serializers

from django.contrib.auth.models import User
from . models import User, Status, Order, Review

from pprint import pprint


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        field = (
            "email",
            "address",
            "cellphone_number",
            "first_name",
            "last_name"
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

