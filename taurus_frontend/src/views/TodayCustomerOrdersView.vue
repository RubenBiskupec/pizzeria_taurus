<script>
import {HttpService} from "@/services/HttpService";

export default {
  name: "TodayCustomerOrdersView",
  data () {
    return {
      interval: null,
      todayOrders: [],
      httpService: new HttpService(),
    }
  },
  methods: {
    async getTodayOrders() {
      this.todayOrders = await this.httpService.getTodayOrders()
    },
    complete(order) {
      this.httpService.completeOrder(order, this.successCallback);
    },
    successCallback(responseData) {
      this.getTodayOrders();
    }
  },
  created() {
    this.getTodayOrders();
  },
  mounted() {
    let that = this;
    this.interval = setInterval(
        that.getTodayOrders(), 60000
    )
  },
  beforeDestroy() {
    clearInterval(this.interval);
  }
}
</script>

<template>
  <v-container>
    <v-row>
      <v-col
        v-for="order in todayOrders"
        v-bind:key="order.id"
        cols="12"
        sm="6"
        md="4"
      >
        <v-card v-show="order.status">
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
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              v-on:click="complete(order)"
              color="secondary"
            >
              Completa
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>

</style>