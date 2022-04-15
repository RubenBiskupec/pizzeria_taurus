# from datetime import datetime
# from datetime import date
import datetime
from pprint import pprint

from django_filters.utils import translate_validation
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from django.contrib.auth.models import User
from . models import User, Status, Order, Review
from . serializers import UserSerializer, StatusSerializer, OrderSerializer, ReviewSerializer
from . filters import OrderFilter


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):

    user_list = User.objects.all()
    serializer = UserSerializer(user_list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'UPDATE', 'DELETE'])
def user_details(request):

    user = request.user

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # TODO non so se va bene, da testare
    elif request.method == 'UPDATE':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def statuses(request):

    status_list = Status.objects.all()
    serializer = StatusSerializer(status_list, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def orders(request):

    if request.method == 'GET':

        user = request.user
        if not user.is_staff:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        filterset = OrderFilter(request.GET, queryset=Order.objects.all())

        if not filterset.is_valid():
            raise translate_validation(filterset.errors)

        serializer = OrderSerializer(filterset.qs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        user = request.user

        date_arr = request.data["delivery_date"].split("-")
        delivery_date = datetime.date(int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))

        time_arr = request.data["delivery_time"].split(":")
        delivery_time = datetime.time(int(time_arr[0]), int(time_arr[1]), 0)

        custom_pizzas = request.data.get('custom_pizzas', None)
        half_meter_pizzas = request.data.get('half_meter_pizzas', None)
        beverages = request.data.get('beverages', None)

        is_delivery = request.data["is_delivery"]
        total_price = float(request.data["total_price"])

        status_instance = Status.objects.get(id=1)

        order = Order.objects.create(user=user,
                                     delivery_date=delivery_date,
                                     delivery_time=delivery_time,
                                     total_price=total_price,
                                     status=status_instance,
                                     is_delivery=is_delivery
                                     )
        # TODO calculate is far based on distance from pizzeria, for now always false by default
        if custom_pizzas:
            order.custom_pizzas.set(custom_pizzas)
        if half_meter_pizzas:
            order.half_meter_pizzas.set(half_meter_pizzas)
        if beverages:
            order.beverages.set(beverages)

        if total_price != order.calculate_total_price():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_today_orders(request):

    today = datetime.date.today()
    order_list = Order.objects.filter(delivery_date=today, status=1).order_by('delivery_time')
    serializer = OrderSerializer(order_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def order_details(request, pk=None):

    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)

    if order.user_id != request.user.id:
        return Response({
            "response": "You do not have permission"
        }, status=status.HTTP_401_UNAUTHORIZED)

    serializer = OrderSerializer(order)
    return Response(serializer.data)


@api_view(['GET'])
def order_details_me(request):

    user = request.user.id

    try:
        order_list = Order.objects.all().filter(user=user)
    except Order.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(order_list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def complete_order(request, pk):

    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)

    order_status = Status.objects.get(id=3)
    order.status = order_status
    order.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def reviews(request):

    if request.method == 'GET':
        review_list = Review.objects.all()
        serializer = ReviewSerializer(review_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        user = request.user
        order = Order.objects.get(id=request.data["order"])

        review = Review(
            user=user,
            order=order
        )
        serializer = ReviewSerializer(review, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def review_details(request, pk=None):

    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)

    if review.user.id != request.user.id:
        return Response({
            "response": "You do not have permission"
        }, status=status.HTTP_401_UNAUTHORIZED)

    order_instance = Order.objects.get(id=review.order.id)
    review.order_id = order_instance
    review.set_order(order_instance)

    if request.method == 'PUT':
        request.data._mutable = True
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.update(review, request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def review_details_order(request, order=None):

    try:
        review = Review.objects.get(order__id=order)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if review.user.id != request.user.id:
        return Response({
            "response": "You do not have permission"
        }, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

