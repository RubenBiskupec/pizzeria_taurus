from rest_framework import serializers

from . models import Ingredient, PizzaType, Size, Dough, MenuPizza, CustomPizza, HalfMeterPizza, Beverage


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            "name",
            "code",
            "description",
            "price",
            "is_in_stock",
            "is_lactose_free",
            "is_spicy",
            "is_vegetarian",
            "is_vegan"
        )


class PizzaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaType
        fields = (
            "name",
            "code",
            "description"
        )


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            "name",
            "code",
            "description",
            "price",
        )


class DoughSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dough
        fields = (
            "name",
            "code",
            "description",
            "price",
            "is_in_stock",
        )


class MenuPizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPizza
        fields = (
            "name",
            "code",
            "description",
            "pizza_type",
            "ingredients",
            "price",
        )
        depth = 2


class CustomPizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPizza
        fields = (
            "id",
            "menu_pizza",
            "dough",
            "size",
            "is_thick",
            "added_ingredients",
            "notes",
            "price"
        )

    # def create(self, validated_data):
    #     return CustomPizza.objects.create(**validated_data)


class HalfMeterPizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HalfMeterPizza
        fields = (
            "id",
            "name",
            "code",
            "custom_pizza_1",
            "custom_pizza_2",
            "custom_pizza_3",
            "notes",
            "price"
        )

    # def create(self, validated_data):
    #     return HalfMeterPizza.objects.create(**validated_data)


class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = (
            "name",
            "code",
            "description",
            "price",
            "size",
            "is_in_stock",
            "is_beer",
            "is_alcoholic"
        )



