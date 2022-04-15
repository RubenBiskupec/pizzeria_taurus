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
        fields = '__all__'
        field = (
            "name",
            "code",
        )


class OrderSerializer(serializers.ModelSerializer):

    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())

    class Meta:
        model = Order
        fields = '__all__'
        depth = 3
        field = (
            "id",
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
        read_only_fields = ["user"]


class ReviewSerializer(serializers.ModelSerializer):

    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

    class Meta:
        model = Review
        depth = 2
        fields = '__all__'
        field = (
            "user",
            "order",
            "title",
            "description",
            "stars"
        )
        read_only_fields = ["user"]

    def create(self, validated_data):
        print("validated_data create", validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        print("validated_data update", validated_data)
        # a volte e' order, a volte order_id
        # if (validated_data.)
        order_data = validated_data.pop("order")
        print("order_data", order_data)

        if isinstance(order_data, int):
            order = Order.objects.get(pk=order_data)
        elif isinstance(order_data, list):
            order = Order.objects.get(pk=order_data[0])
        else:
            order = Order.objects.get(pk=order_data.id)
        instance.order = order
        return super().update(instance, validated_data)



