from rest_framework import serializers

from . models import Customer, Status, Order, Review


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        field = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
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

