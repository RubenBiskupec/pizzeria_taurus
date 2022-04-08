from django.urls import path

from . import views


urlpatterns = [
    path('ingredients/', views.ingredients),
    path('pizza_types/', views.pizza_types),
    path('sizes/', views.sizes),
    path('doughs/', views.doughs),
    path('menu_pizzas/', views.menu_pizzas),
    path('custom_pizzas/', views.custom_pizzas),
    path('custom_pizzas/<int:pk>/', views.custom_pizza_details),
    path('half_meter_pizzas/', views.half_meter_pizzas),
    path('half_meter_pizzas/<int:pk>/', views.half_meter_pizza_details),
    path('beverages/', views.beverages)
]

