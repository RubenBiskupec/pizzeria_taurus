<script>
import {HttpService} from "@/services/HttpService";

export default {
  name: "OrderInfo",
  data() {
    return {
      httpService: new HttpService(),

      order: {
        is_delivery: true,
        address: "",
        delivery_date: null,
        delivery_time: null,
        custom_pizzas: [],
        half_meter_pizzas: [],
        beverages: [],
        notes: "",
        total_price: null,
      },
      taurusAddress: "Via Fratelli Rosselli, 227, 41125 Modena MO",

      orderSuccessNotification: "",
      orderErrorNotification: "",

    }
  },
  computed: {
    userInfo() {
      return this.$store.getters.userInfo;
    },
    cart() {
      return this.$store.getters.cart;
    },
    totalPrice() {
      let totalPrice = 0;
      for(let i in this.cart.custom_pizzas_long) {
        totalPrice += this.cart.custom_pizzas_long[i]["price"];
      }
      for(let i in this.cart.half_meter_pizzas_long) {
        totalPrice += this.cart.half_meter_pizzas_long[i]["price"];
      }
      for(let i in this.cart.beverages_long) {
        totalPrice += this.cart.beverages_long[i]["price"];
      }
      if (this.order.is_delivery) {
        totalPrice += 2;
      }
      return totalPrice;
    }
  },
  methods: {
    confirmOrder() {
      this.order.address = this.userInfo.address;

      // TODO change total price
      const orderForm = {
        is_delivery: this.order.is_delivery,
        address: this.order.address,
        delivery_date: this.order.delivery_date,
        delivery_time: this.order.delivery_time,
        custom_pizzas: this.cart.custom_pizzas,
        half_meter_pizzas: [],
        beverages: [],
        status: 1,
        notes: this.order.notes,
        total_price: this.totalPrice
      }
      this.httpService.createOrder(orderForm, this.createOrderSuccessCallback, this.createOrderFailureCallback);
    },
    createOrderSuccessCallback: function(responseData) {
      this.orderSuccessNotification = "Ordine creato con successo!";
      this.orderErrorNotification = "";
    },
    createOrderFailureCallback: function(responseData) {
      this.orderErrorNotification = "Qualcosa e' andato storto nella creazione dell'ordine, per favore riprova."
    },
    allowedHours(hour){
      const allowedHours = [18, 19, 20, 21];
      return allowedHours.includes(hour);
    },
    allowedMinutes(minute) {
      const allowedMinutes = [0, 15, 30, 45];
      return allowedMinutes.includes(minute);
    }
  },
}
</script>

<template>
  <v-card>
    <v-card-title>Informazioni ordine</v-card-title>
    <v-form>
      <v-card-text>
        <v-row>
          <v-col
            cols="12"
            sm="6"
          >
            <v-checkbox
              v-model="order.is_delivery"
              label="Consegna a domicilio"
            ></v-checkbox>
          </v-col>

          <v-col
            cols="12"
            sm="6"
          >
            <v-text-field
              v-if="order.is_delivery"
              dense
              outlined
              label="Indirizzo"
              v-model="userInfo.address"
            ></v-text-field>
            <v-text-field
              v-else
              dense
              outlined
              readonly
              v-model="taurusAddress"
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            sm="6"
          >
            <v-date-picker
              v-model="order.delivery_date"
              full-width
              color="primary"
              header-color="secondary"
            ></v-date-picker>
          </v-col>

  <!--            TODO RESTRINGI A INTERVALLI DI 15 MINUTI-->
  <!--            E PERMETTI LA SELEZIONE IN BASE ALLA DISPONIBILITA'-->
          <v-col
            cols="12"
            sm="6"
          >
            <v-time-picker
              v-model="order.delivery_time"
              full-width
              color="primary"
              header-color="secondary"
              v-bind:allowed-hours="allowedHours"
              v-bind:allowed-minutes="allowedMinutes"
              format="24hr"
            ></v-time-picker>
          </v-col>

          <v-col
            cols="12"
          >
            <v-text-field
              dense
              outlined
              label="Note"
              hint="es. indicazioni su come trovare l'apparmento ecc."
              v-model="order.notes"
            ></v-text-field>
          </v-col>

          <v-col
            cols="12"
            align="right"
            class="price"
          >
            Totale ordine: € {{ totalPrice }}
          </v-col>

          <v-col
            cols="12"
            align="right"
          >
            <v-btn
              v-on:click="confirmOrder"
              color="secondary"
            >Conferma ordine</v-btn>
          </v-col>

        </v-row>

        <v-divider
            v-if="orderErrorNotification != '' || orderSuccessNotification != ''"
            class="my-4"
          ></v-divider>

        <v-row class="ma-1">
          <v-col
            v-if="orderErrorNotification != ''"
            cols="12"
            class="px-4 py-2 my-2 rounded primary"
          >
            {{ orderErrorNotification }}
          </v-col>
          <v-col
            v-if="orderSuccessNotification != ''"
            cols="12"
            class="px-4 py-2 my-2 notification-message rounded accent"
          >
            {{ orderSuccessNotification }}
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