from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from . models import Customer, Status, Order, Review
from . serializers import UserSerializer, CustomerSerializer, StatusSerializer, OrderSerializer, ReviewSerializer

from pprint import pprint


@api_view(['POST'])
def users(request):
    print("REUQETS", request)
    print("REUQETS DATA", request.data)
    serializer = UserSerializer(
        data=request.data,
        context=request.data["customer"]
    )

    if serializer.is_valid():
        # instance = user_serializer.save()
        # Customer.objects.create(user=instance)

        user_instance = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # print("Instance")
        # pprint(vars(user_instance))
    #
    #     request.data["customer"]["user"] = user_instance.id
    #     # request.data["customer"]["user"]["id"] = user_instance.id
    #     #
    #     pprint(request.data["customer"])
    #
    #     customer_serializer = CustomerSerializer(data=request.data["customer"])
    #     if customer_serializer.is_valid():
    #         customer_serializer.save()
    #         return Response(customer_serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def customers(request):

    if request.method == 'GET':
        customer_list = Customer.objects.all()
        serializer = CustomerSerializer(customer_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'UPDATE', 'DELETE'])
def customer_details(request, pk=None):

    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    # TODO non so se va bene, da testare
    elif request.method == 'UPDATE':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer .delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def statuses(request):
    status_list = Status.objects.all()
    serializer = StatusSerializer(status_list, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def orders(request):
    if request.method == 'GET':
        order_list = Order.objects.all()
        serializer = OrderSerializer(order_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_details(request, pk=None):

    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(order)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def reviews(request):

    if request.method == 'GET':
        review_list = Review.objects.all()
        serializer = ReviewSerializer(review_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'UPDATE', 'DELETE'])
def review_details(request, pk=None):

    try:
        review = Review.objects.get(pk=pk)
    except Review.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(review)
        return Response(serializer.data)

    # TODO non so se va bene, da testare
    elif request.method == 'UPDATE':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

