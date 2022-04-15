<script>
import {HttpService} from "@/services/HttpService";

export default {
  name: "Order.vue",
  data() {
    return {
      httpService: new HttpService(),
      tab: 0,
      tabs: [
          'Pizze',
          'Mezzi Metri',
          'Bevande'
      ],
      pizzaType: {},
      basePizza: {},
      addedIngredients: [],
      dough: {},
      size: {},
      is_thick: false,
      notes: " ",

      createPizzaErrorMessage: "",
    }
  },
  computed: {
    availableMenuPizzas() {
      return this.$store.getters.availableMenuPizzas;
    },
    pizzas() {
      let pizzas = [];
      const menuPizzas = this.availableMenuPizzas;
      for (const i in menuPizzas) {
        if (menuPizzas[i].pizza_type.code == "PZ") {
          pizzas.push(menuPizzas[i]);
        }
      }
      return pizzas;
    },
    calzoni() {
      let calzoni = [];
      const pizzas = this.availableMenuPizzas;
      for (const i in pizzas) {
        if (pizzas[i].pizza_type.code == "CA") {
          calzoni.push(pizzas[i]);
        }
      }
      return calzoni;
    },
    saltimbocca() {
      let saltimbocca = [];
      const pizzas = this.availableMenuPizzas;
      for (const i in pizzas) {
        if (pizzas[i].pizza_type.code == "SB") {
          saltimbocca.push(pizzas[i]);
        }
      }
      return saltimbocca;
    },
    pizzaTypes() {
      return this.$store.getters.pizzaTypes;
    },
    availableIngredients() {
      return this.$store.getters.availableIngredients;
    },
    availableDoughs() {
      return this.$store.getters.availableDoughs;
    },
    sizes() {
      return this.$store.getters.sizes;
    },
    availableBeverages() {
      return this.$store.getters.availableBeverages;
    },
    price() {
      let price = 0;
      if (this.basePizza.price != null) {
        price += parseFloat(this.basePizza.price);
      }
      if (this.addedIngredients != null) {
        for (let i in this.addedIngredients) {
          if (this.addedIngredients[i].price != null) {
            price += parseFloat(this.addedIngredients[i].price);
          }
        }
      }
      if (this.dough.price != null) {
        price += parseFloat(this.dough.price);
      }
      if (this.size.price != null) {
        price += parseFloat(this.size.price);
      }
      if (this.is_thick) {
        price += 1;
      }
      return price;
    },
    cart() {
      return this.$store.getters.cart;
    }
  },
  methods: {
    addPizzaToOrder: function() {
      let added_ingredients_ids = [];
      for(let i in this.addedIngredients) {
        added_ingredients_ids.push(this.addedIngredients[i].id);
      }

      const customPizza = {
        menu_pizza: this.basePizza.id,
        dough: this.dough.id,
        size: this.size.id,
        is_thick: this.is_thick,
        added_ingredients: added_ingredients_ids,
        notes: this.notes,
        price: this.price,
      }

      const customPizzaLong = {
        menu_pizza: this.basePizza,
        dough: this.dough,
        size: this.size,
        is_thick: this.is_thick,
        added_ingredients: this.addedIngredients,
        notes: this.notes,
        price: this.price,
      }
      this.httpService.createCustomPizza(customPizza, customPizzaLong, this.createCustomPizzaSuccessCallback, this.createCustomPizzaErrorCallback);
    },
    createCustomPizzaSuccessCallback: function(responseData, customPizzaLong) {
      this.createPizzaErrorMessage = "";
      customPizzaLong["id"] = responseData.id;
      this.$store.dispatch('addCustomPizzaToCart', customPizzaLong)
      this.resetCustomPizzaFields();
    },
    resetCustomPizzaFields: function() {
      this.pizzaType = {};
      this.basePizza = {};
      this.addedIngredients = [];
      this.dough = {};
      this.size = {};
      this.is_thick = false;
      this.notes = "";
    },
    createCustomPizzaErrorCallback: function(error) {
      this.createPizzaErrorMessage = "Errore nella creazione della pizza, per favore riprovare."
    },
  }
}
</script>

<template>
  <v-card>
    <v-tabs
      v-model="tab"
      background-color="secondary"
      centered
    >
      <v-tabs-slider color="primary"></v-tabs-slider>
      <v-tab
        v-for="tab in tabs"
        v-bind:key="tab"
        color="secondary"
      >
        {{ tab }}
      </v-tab>
    </v-tabs>

    <v-card-title>Ordine</v-card-title>

    <v-form>

      <v-card-text v-show="tab==0">
        <v-row>

          <v-col
            cols="12"
            sm="6"
            md="4"
          >
            <v-select
              dense
              outlined
              label="Tipologia"
              v-model="pizzaType"
              v-bind:items="pizzaTypes"
              item-text="name"
              return-object
            ></v-select>
          </v-col>

          <v-col
            v-show="pizzaType.name != 'Pizza'
                      && pizzaType.name != 'Calzone'
                      && pizzaType.name != 'Saltimbocca'"
            cols="12"
            sm="6"
            md="4"
          >
            <v-autocomplete
              dense
              outlined
              label="Base"
              v-model="basePizza"
              v-bind:items="pizzas"
              item-text="name"
              return-object
            ></v-autocomplete>
          </v-col>

          <v-col
            v-show="pizzaType.name == 'Pizza'"
            cols="12"
            sm="6"
            md="4"
          >
            <v-autocomplete
              dense
              outlined
              label="Base"
              v-model="basePizza"
              v-bind:items="pizzas"
              item-text="name"
              return-object
            ></v-autocomplete>
          </v-col>

          <v-col
            v-show="pizzaType.name == 'Saltimbocca'"
            cols="12"
            sm="6"
            md="4"
          >
            <v-autocomplete
              dense
              outlined
              label="Base"
              v-model="basePizza"
              v-bind:items="saltimbocca"
              item-text="name"
              return-object
            ></v-autocomplete>
          </v-col>

          <v-col
            v-show="pizzaType.name == 'Calzone'"
            cols="12"
            sm="6"
            md="4"
          >
            <v-autocomplete
              dense
              outlined
              label="Base"
              v-model="basePizza"
              v-bind:items="calzoni"
              item-text="name"
              return-object
            ></v-autocomplete>
          </v-col>

          <v-col
            cols="12"
            sm="6"
            md="4"
          >
            <v-select
              dense
              outlined
              readonly
              label="Ingredienti base"
              v-model="basePizza.ingredients"
              v-bind:items="availableIngredients"
              item-text="name"
              return-object
              multiple
              chips
              small-chips
            ></v-select>
          </v-col>

          <v-col
            cols="12"
            sm="6"
            md="4"
          >
            <v-autocomplete
              dense
              outlined
              label="Ingredienti aggiuntivi"
              v-model="addedIngredients"
              v-bind:items="availableIngredients"
              item-text="name"
              return-object
              multiple
              chips
              small-chips
            ></v-autocomplete>
          </v-col>


<!--            TODO, se impasto speciale, no alte e tirate-->
          <v-col
            cols="12"
            sm="6"
            md="4"
          >
            <v-select
              dense
              outlined
              label="Impasto"
              v-model="dough"
              v-bind:items="availableDoughs"
              item-text="name"
              return-object
            ></v-select>
          </v-col>


          <v-col
            cols="12"
            sm="6"
            md="4"
          >
            <v-row>
              <v-col cols="8">
                <v-select
                  dense
                  outlined
                  label="Dimensione"
                  v-model="size"
                  v-bind:items="sizes"
                  item-text="name"
                  return-object
                ></v-select>
              </v-col>
              <v-col cols="4">
                <v-checkbox
                  class="mt-1"
                  v-model="is_thick"
                  label="Alta"
                ></v-checkbox>
              </v-col>
            </v-row>

          </v-col>

          <v-col
            cols="12"
          >
            <v-text-field
              dense
              outlined
              label="Note"
              hint="es. rimozione ingredienti, pizza ben cotta, ecc."
              v-model="notes"
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            align="right"
            class="price"
          >
            Prezzo: € {{ price }}
          </v-col>

          <v-col
            cols="12"
            align="right"
          >
            <v-btn
              v-on:click="addPizzaToOrder"
              color="secondary"
            >Aggiungi all'ordine</v-btn>
          </v-col>

        </v-row>

        <v-divider
          v-if="createPizzaErrorMessage != ''"
          class="my-4"
        ></v-divider>
        <v-row
          v-if="createPizzaErrorMessage != ''"
          class="px-4 py-2 notification-message"
        >
          <v-col cols="12"
            class="px-4 py-2 my-2 rounded primary"
          >
            {{ createPizzaErrorMessage }}
          </v-col>
        </v-row>


      </v-card-text>

    </v-form>
  </v-card>
</template>

<style scoped>
.price {
  font-size: 1.2em;
}

.notification-message {
  color: white;
  padding: 12px !important;
}
</style>