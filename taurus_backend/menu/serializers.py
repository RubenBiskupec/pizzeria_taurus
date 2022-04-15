from pprint import pprint

from rest_framework import serializers

from . models import Ingredient, PizzaType, Size, Dough, MenuPizza, CustomPizza, HalfMeterPizza, Beverage


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            "id",
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
            "id",
            "name",
            "code",
            "description"
        )


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = (
            "id",
            "name",
            "code",
            "description",
            "price",
        )


class DoughSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dough
        fields = (
            "id",
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
            "id",
            "name",
            "code",
            "description",
            "pizza_type",
            "ingredients",
            "price",
        )
        depth = 2


class CustomPizzaSerializer(serializers.ModelSerializer):

    # read_only=True
    dough = serializers.PrimaryKeyRelatedField(queryset=Dough.objects.all())
    menu_pizza = serializers.PrimaryKeyRelatedField(queryset=MenuPizza.objects.all())
    size = serializers.PrimaryKeyRelatedField(queryset=Size.objects.all())
    # added_ingredients = IngredientSerializer(many=True)

    class Meta:
        model = CustomPizza
        depth = 3
        fields = (
            "id",
            "dough",
            "menu_pizza",
            "size",
            "is_thick",
            "added_ingredients",
            "notes",
            "price"
        )


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


class BeverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beverage
        fields = (
            "id",
            "name",
            "code",
            "description",
            "price",
            "size",
            "is_in_stock",
            "is_beer",
            "is_alcoholic"
        )



