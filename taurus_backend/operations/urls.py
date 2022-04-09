from django.urls import path

from . import views


urlpatterns = [
    path('users/', views.users),
    path('users/<int:pk>/', views.user_details),
    path('statuses/', views.statuses),
    path('orders/', views.orders),
    path('orders/<int:pk>/', views.order_details),
    path('reviews/', views.reviews),
    path('reviews/<int:pk>', views.review_details),
]

