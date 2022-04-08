from django.contrib import admin

from . models import Customer, Review, Status, Order

admin.site.register(Customer)
admin.site.register(Review)
admin.site.register(Status)
admin.site.register(Order)