<script>

import {HttpService} from "@/services/HttpService";

export default {
  name: "AllCustomerOrdersView",
  data () {
    return {
      orders: [],
      start_date: null,
      end_date: null,
      httpService: new HttpService(),
    }
  },
  methods: {
    async fetchOrdersByDate() {
      this.orders = await this.httpService.getOrdersByDate(this.start_date, this.end_date);
    }
  }
}
</script>

<template>
  <v-container>
    <v-card class="ma-4">
      <v-row class="pa-4">
        <v-col cols="6">
          <v-text-field
            v-model="start_date"
            label="Data di inizio"
            required
            outlined
            dense
            hint="in formato YYYY-MM-DD"
          ></v-text-field>
        </v-col>
        <v-col cols="6">
          <v-text-field
            v-model="end_date"
            label="Data di fine"
            required
            outlined
            dense
            hint="in formato YYYY-MM-DD"
          ></v-text-field>
        </v-col>
        <v-col cols="12" align="right">
          <v-btn
            v-on:click="fetchOrdersByDate"
            color="secondary"
          > Ricerca </v-btn>
        </v-col>
      </v-row>

      <v-row>
        <v-col
          v-for="order in orders"
          v-bind:key="order.id"
          cols="12"
          sm="6"
          md="4"
        >
          <v-card>
            <v-card-title>
              Ordine di {{ order.user.first_name }} {{ order.user.last_name }}
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text>
              Pizze: <br/><br/>
              <div
                v-for="pizza in order.custom_pizzas"
                v-bind:key="pizza.id"
              >
                Base: {{ pizza.menu_pizza.name }} <br/>
                Tipologia: {{ pizza.menu_pizza.pizza_type.name }} <br/>
                Impasto: {{ pizza.dough.name }} <br/>
                Dimensione: {{ pizza.size.name }} <br/>
                <div v-if="pizza.added_ingredients.length">
                  Ingredienti aggiuntivi:
                  <span
                    v-for="ingredient in pizza.added_ingredients"
                    v-bind:key="ingredient.id"
                  > {{ ingredient.name }} </span>
                </div>
                <div v-if="pizza.notes != ''">
                  Note pizza: {{ pizza.notes }}
                </div>
                <br/>
              </div>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-text>

            </v-card-text>
            <v-card-text>
              Data: {{ order.delivery_date }} <br/>
              Orario: {{ order.delivery_time }}
            </v-card-text>
            <v-card-text v-if="order.is_delivery">
              Consegna a domicilio <br/>
              Indirizzo: {{ order.address }} <br/>
              Telefono: {{ order.user.cellphone_number }}
            </v-card-text>
            <v-card-text v-else>
              Da asporto <br/>
              Telefono: {{ order.user.cellphone_number }}
            </v-card-text>
            <v-card-text>
              Totale: {{ order.total_price }}
            </v-card-text>
            <v-card-text v-if="order.notes != ''">
              Note: {{ order.notes }}
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

    </v-card>
  </v-container>
</template>

<style scoped>

</style>