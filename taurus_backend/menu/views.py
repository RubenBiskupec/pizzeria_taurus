from pprint import pprint

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response

from . models import Ingredient, PizzaType, Size, Dough, MenuPizza, CustomPizza, HalfMeterPizza, Beverage
from . serializers import IngredientSerializer, PizzaTypeSerializer, SizeSerializer, DoughSerializer, MenuPizzaSerializer, CustomPizzaSerializer, HalfMeterPizzaSerializer, BeverageSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def ingredients(request):
    ingredient_list = Ingredient.objects.all()
    serializer = IngredientSerializer(ingredient_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def pizza_types(request):
    pizza_type_list = PizzaType.objects.all()
    serializer = PizzaTypeSerializer(pizza_type_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def sizes(request):
    size_list = Size.objects.all()
    serializer = SizeSerializer(size_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def doughs(request):
    dough_list = Dough.objects.all()
    serializer = DoughSerializer(dough_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def menu_pizzas(request):
    menu_pizza_list = MenuPizza.objects.all()
    serializer = MenuPizzaSerializer(menu_pizza_list, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def custom_pizzas(request):

    if request.method == 'GET':
        custom_pizza_list = CustomPizza.objects.all()
        serializer = CustomPizzaSerializer(custom_pizza_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        #
        # {
        #     "menu_pizza": 4,
        #     "dough": 1,
        #     "size": 1,
        #     "added_ingredients": [
        #         4
        #     ],
        #     "notes": " aaa",
        #     "price": 7
        # }

        menu_pizza_id = data["menu_pizza"]
        menu_pizza = MenuPizza.objects.get(id=menu_pizza_id)
        dough_id = data["dough"]
        dough = Dough.objects.get(id=dough_id)
        size_id = data["size"]
        size = Size.objects.get(id=size_id)
        notes = data["notes"]
        added_ingredients = data["added_ingredients"]
        price = data["price"]
        is_thick = data["is_thick"]

        custom_pizza = CustomPizza.objects.create(
            menu_pizza=menu_pizza,
            dough=dough,
            size=size,
            notes=notes,
            price=price,
            is_thick=is_thick
        )
        custom_pizza.added_ingredients.set(added_ingredients)

        if custom_pizza.calculate_price() != custom_pizza.price:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = CustomPizzaSerializer(custom_pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def custom_pizza_details(request, pk=None):

    try:
        custom_pizza = CustomPizza.objects.get(pk=pk)
    except CustomPizza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CustomPizzaSerializer(custom_pizza)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def half_meter_pizzas(request):

    if request.method == 'GET':
        half_meter_pizza_list = HalfMeterPizza.objects.all()
        serializer = HalfMeterPizzaSerializer(half_meter_pizza_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HalfMeterPizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def half_meter_pizza_details(request, pk=None):

    try:
        half_meter_pizza = HalfMeterPizza.objects.get(pk=pk)
    except HalfMeterPizza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = HalfMeterPizzaSerializer(half_meter_pizza)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def beverages(request):
    beverage_list = Beverage.objects.all()
    serializer = BeverageSerializer(beverage_list, many=True)
    return Response(serializer.data)



