from decimal import Decimal

import pytest

from rest_framework.test import APIClient

from menu.models import Dough, MenuPizza, CustomPizza
from menu.serializers import DoughSerializer, SizeSerializer, IngredientSerializer, PizzaTypeSerializer, \
    MenuPizzaSerializer, CustomPizzaSerializer
from operations.serializers import OrderSerializer, StatusSerializer

client = APIClient()


@pytest.mark.django_db
def test_create_review():
    # register user
    register_payload = dict(
        first_name="Mario",
        last_name="Rossi",
        email="mario.rossi@gmail.com",
        password="hciusdyt736873gdshgsd73",
        address="Viale Italia, 1, Modena",
        cellphone_number="371897446"
    )
    client.post("/api/v1/auth/users/", register_payload, format="json")

    # log in (get auth token)
    payload = dict(
        email="mario.rossi@gmail.com",
        password="hciusdyt736873gdshgsd73"
    )
    response = client.post("/api/v1/auth/token/login", payload, format="json")
    data = response.data
    auth_token = data["auth_token"]

    dough_dict = dict(
        name="Classico",
        code="C",
        description="Description",
        price=0
    )
    dough_serializer = DoughSerializer(data=dough_dict)
    if dough_serializer.is_valid():
        dough = dough_serializer.save()

    size_dict = dict(
        name="Normale",
        code="NM",
        description="Grandezza classica, 33x33cm",
        price=0
    )
    size_serializer = SizeSerializer(data=size_dict)
    if size_serializer.is_valid():
        size = size_serializer.save()

    ingredient_dict = dict(
        name="Pomodoro",
        code="PM",
        description="Pomodoro",
        price=1,
        is_in_stock=True,
        is_lactose_free=True,
        is_spicy=False,
        is_vegetarian=True,
        is_vegan=True
    )
    ingredient_serializer = IngredientSerializer(data=ingredient_dict)
    if ingredient_serializer.is_valid():
        ingredient_serializer.save()

    ingredient_dict = dict(
        name="Mozzarella",
        code="MZ",
        description="Mozzarella",
        price=1.5,
        is_in_stock=True,
        is_lactose_free=False,
        is_spicy=False,
        is_vegetarian=True,
        is_vegan=False
    )
    ingredient_serializer = IngredientSerializer(data=ingredient_dict)
    if ingredient_serializer.is_valid():
        ingredient_serializer.save()

    ingredient_dict = dict(
        name="Rucola",
        code="RC",
        description="Rucola fresca, aggiunta fuori forno",
        price=1,
        is_in_stock=True,
        is_lactose_free=True,
        is_spicy=False,
        is_vegetarian=True,
        is_vegan=True
    )
    ingredient_serializer = IngredientSerializer(data=ingredient_dict)
    if ingredient_serializer.is_valid():
        ingredient_serializer.save()

    pizza_type_dict = dict(
        name="Pizza",
        code="PZ",
        description="Pizza tonda",
    )
    pizza_type_serializer = PizzaTypeSerializer(data=pizza_type_dict)
    if pizza_type_serializer.is_valid():
        pizza_type = pizza_type_serializer.save()

    status_dict = dict(
        name="Da fare",
        code="TODO"
    )
    status_serializer = StatusSerializer(data=status_dict)
    if status_serializer.is_valid():
        status = status_serializer.save()

    menu_pizza = MenuPizza.objects.create(
        pizza_type=pizza_type,
        price=5
    )
    menu_pizza_dict = dict(
        name="Margherita",
        code="MA",
        description="margherita pizza",
        ingredients=[1, 2],
    )
    menu_pizza_serializer = MenuPizzaSerializer(menu_pizza, data=menu_pizza_dict)
    if menu_pizza_serializer.is_valid():
        menu_pizza = menu_pizza_serializer.save()

    notes = "Custom Pizza notes"
    custom_pizza = CustomPizza.objects.create(
        menu_pizza=menu_pizza,
        dough=dough,
        size=size,
        notes=notes,
        price=Decimal(6),
        is_thick=False
    )
    added_ingredients = [3]
    custom_pizza.added_ingredients.set(added_ingredients)
    assert custom_pizza.calculate_price() == custom_pizza.price
    custom_pizza_dict = dict(
        menu_pizza=1,
        dough=1,
        size=1,
        added_ingredients=[3],
        notes="Notes",
        price=6
    )
    custom_pizza_serializer = CustomPizzaSerializer(custom_pizza, data=custom_pizza_dict)
    if custom_pizza_serializer.is_valid():
        custom_pizza = custom_pizza_serializer.save()

    order_payload = dict(
        address="Via Brescia, 19",
        beverages=[],
        custom_pizzas=[1],
        delivery_date="2022-04-15",
        delivery_time="19:45:00",
        half_meter_pizzas=[],
        is_delivery=True,
        notes="",
        status=1,
        total_price=Decimal(8),
        user=1
    )

    response = client.post("/api/v1/orders/", order_payload, HTTP_AUTHORIZATION='Token {}'.format(auth_token))
    assert response.status_code == 201

    review_payload = dict(
        description="Review",
        order=1,
        stars=5,
        title="Title"
    )
    response = client.post("/api/v1/reviews/", review_payload, HTTP_AUTHORIZATION='Token {}'.format(auth_token))
    assert response.status_code == 201

    review_payload_update = dict(
        description="Updated Review",
        order=1,
        stars=5,
        title="Title"
    )
    response_update = client.put("/api/v1/reviews/1", review_payload_update, HTTP_AUTHORIZATION='Token {}'.format(auth_token))
    assert response_update.status_code == 200

    response_delete = client.delete("/api/v1/reviews/1", HTTP_AUTHORIZATION='Token {}'.format(auth_token))
    assert response_delete.status_code == 204

