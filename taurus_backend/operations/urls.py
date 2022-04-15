from django.urls import path

from . import views


urlpatterns = [
    path('users/', views.get_users),
    path('users/', views.create_user),
    path('users/me/', views.user_details),
    path('statuses/', views.statuses),
    path('orders/', views.orders),
    path('orders/today/', views.get_today_orders),
    path('orders/<int:pk>/', views.order_details),
    path('orders/<int:pk>/complete/', views.complete_order),
    path('orders/me/', views.order_details_me),
    path('reviews/', views.reviews),
    path('reviews/<int:pk>', views.review_details),
    path('reviews/orders/<int:order>', views.review_details_order),
]

