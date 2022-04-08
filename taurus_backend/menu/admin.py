from django.contrib import admin

from . models import Ingredient, PizzaType, Size, Dough, MenuPizza, CustomPizza, HalfMeterPizza, Beverage

admin.site.register(Ingredient)
admin.site.register(PizzaType)
admin.site.register(Size)
admin.site.register(Dough)
admin.site.register(MenuPizza)
admin.site.register(CustomPizza)
admin.site.register(HalfMeterPizza)
admin.site.register(Beverage)



