from django.contrib import admin

from . models import User, Review, Status, Order

admin.site.register(User)
admin.site.register(Review)
admin.site.register(Status)
admin.site.register(Order)
