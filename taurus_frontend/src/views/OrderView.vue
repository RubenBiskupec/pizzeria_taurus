<script>

import Order from "@/components/Order";
import Cart from "@/components/Cart";
import OrderInfo from "@/components/OrderInfo";
import OrderList from "@/components/OrderList";
import ReviewForm from "@/components/ReviewForm";

export default {
  name: "OrderPage",
  components: { Order, Cart, OrderInfo, OrderList, ReviewForm },
  async beforeCreate() {
    await this.$store.dispatch("fetchIngredients");
    await this.$store.dispatch("fetchPizzaTypes");
    await this.$store.dispatch("fetchSizes");
    await this.$store.dispatch("fetchDoughs");
    await this.$store.dispatch('fetchUserInfo');
    await this.$store.dispatch('fetchOrderUserList');
  },
  mounted() {
    document.title = "Order | Taurus";
  },
}

</script>

<template>
  <v-container>

    <v-row>
      <v-col
        cols="12"
        lg="6"
        xl="4"
      >
        <Order></Order>
      </v-col>

      <v-col
        cols="12"
        lg="6"
        xl="4"
      >
            <!--    TODO, aggiungi checkbox alta-->
    <!--    aggiungi crud delete-->
        <Cart></Cart>
      </v-col>

      <v-col
        cols="12"
        lg="6"
        xl="4"
      >
        <OrderInfo></OrderInfo>
      </v-col>

      <v-col
        cols="12"
        lg="6"
        xl="4"
      >
        <OrderList></OrderList>
      </v-col>

      <v-col
        cols="12"
        lg="6"
        xl="4"
      >
        <ReviewForm></ReviewForm>
      </v-col>

    </v-row>

  </v-container>
</template>

<style scoped>

</style>