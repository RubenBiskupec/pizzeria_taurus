from django.db import models


class Ingredient(models.Model):
    # for example: tomato sauce, mozzarella cheese, pepperoni
    name = models.CharFiled(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True, null=True)
    description = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_in_stock = models.BooleanField(default=True)
    is_lactose_free = models.BooleanField(default=False)
    is_spicy = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)

    def get_price(self):
        return self.price

    def __str__(self):
        return "Ingrediente " + self.name

class PizzaType(models.Model):
    # for example: pizza, saltimbocca, calzone
    name = models.CharFiled(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True, null=True)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "Tipologia " + self.name


class Size(models.Model):
    # for example: small, regular, large
    name = models.CharFiled(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True, null=True)
    description = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_price(self):
        return self.price

    def __str__(self):
        return "Grandezza " + self.name


class Dough(models.Model):
    # for example: senatore cappelli, integrale
    name = models.CharFiled(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True, null=True)
    description = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_in_stock = models.BooleanField(default=True)

    def get_price(self):
        return self.price

    def __str__(self):
        return "Impasto " + self.name


class MenuPizza(models.Model):
    # pizzas available on the menu, es. margherita, napoli
    name = models.CharFiled(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True, null=True)
    description = models.CharField(max_length=255, null=True)
    pizza_type = models.ForeignKey(
        PizzaType,
        on_delete=models.CASCADE
    )
    ingredients = models.ManyToManyField(Ingredient)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_price(self):
        return self.price

    def __str__(self):
        return "Pizza da Menu' " + self.name


class CustomPizza(models.Model):
    menu_pizza = models.ForeignKey(
        MenuPizza,
        on_delete=models.CASCADE
    )
    dough = models.ForeignKey(
        Dough,
        on_delete=models.CASCADE
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE
    )
    is_thick = models.BooleanField(default=False)
    added_ingredients = models.ManyToManyField(Ingredient)
    notes = models.CharField(max_length=255, null=True)

    @property
    def price(self):
        return self.calculate_price(self)

    def calculate_price(self):
        menu_pizza_price = self.menu_pizza.get_price(self.menu_pizza)
        added_ingredients_price = 0
        for added_ingredient in self.added_ingredients:
            added_ingredients_price += added_ingredient.get_price(added_ingredient)
        addons_price = self.dough.get_price(self.dough)
        addons_price += self.size.get_price(self.size)
        # FIXME, hardcoded 1, hard to change
        if self.is_thick:
            addons_price += 1
        return menu_pizza_price + added_ingredients_price + addons_price

    def get_price(self):
        return self.price

    def __str__(self):
        return "Pizza Personalizzata"


class HalfMeterPizza(models.Model):
    name = models.CharFiled(max_length=50, null=True)
    code = models.CharField(max_length=10, null=True)
    dough = models.ForeignKey(
        Dough,
        on_delete=models.SET_NULL
    )
    custom_pizza_1 = models.ForeignKey(
        CustomPizza,
        on_delete=models.SET_NULL
    )
    custom_pizza_2 = models.ForeignKey(
        CustomPizza,
        on_delete=models.SET_NULL,
        null=True
    )
    custom_pizza_3 = models.ForeignKey(
        CustomPizza,
        on_delete=models.SET_NULL,
        null=True
    )
    notes = models.CharField(max_length=255, null=True)

    @property
    def price(self):
        return self.calculate_price(self)

    def calculate_price(self):
        pizza_price = 0
        if self.custom_pizza_3 is None and self.custom_pizza_2 is None:
            pizza_price += self.custom_pizza_1.get_price(self.custom_pizza_1)
            pizza_price *= 3
        elif self.custom_pizza_3 is None:
            pizza_price += self.custom_pizza_1.get_price(self.custom_pizza_1)
            pizza_price += self.custom_pizza_2.get_price(self.custom_pizza_2)
            pizza_price *= 1.5
        else:
            pizza_price += self.custom_pizza_1.get_price(self.custom_pizza_1)
            pizza_price += self.custom_pizza_2.get_price(self.custom_pizza_2)
            pizza_price += self.custom_pizza_3.get_price(self.custom_pizza_3)
        dough_price = self.dough.get_price(self.dough) * 3
        return pizza_price + dough_price

    def get_price(self):
        return self.price

    def __str__(self):
        return "Mezzo Metro"


class Beverage(models.Model):
    # for example, coca-cola, water, beer
    name = models.CharFiled(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True, null=True)
    description = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # ex. 0.33l, 0.66l, 1.5l
    size = models.CharField(max_length=20)
    is_in_stock = models.BooleanField(default=True)
    is_beer = models.BooleanField(default=False)
    is_alcoholic = models.BooleanField(default=False)

    def __str__(self):
        return "Bevanda " + self.name


