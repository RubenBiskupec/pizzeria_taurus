<script>
export default {
  name: "Cart",
  data() {
    return {
      pizzaTableHeaders: [
        {
          text: 'Base',
          align: 'start',
          sortable: false,
          value: 'menu_pizza.name',
        },
        { text: 'Impasto', value: 'dough.name' },
        { text: 'Dimensione', value: 'size.name' },
        { text: 'Alta', value: 'is_thick' },
        { text: 'Prezzo', value: 'price' },
      ],
    }
  },
  computed: {
    cart() {
      return this.$store.getters.cart;
    }
  }
}
</script>

<template>
  <v-card>
    <v-card-title>Carrello</v-card-title>
    <v-data-table-header>Pizze</v-data-table-header>
    <v-data-table
      v-bind:headers="pizzaTableHeaders"
      v-bind:items="cart.custom_pizzas_long"
      v-bind:items-per-page="5"
    ></v-data-table>

<!--    <v-data-table-header>Mezzi Metri</v-data-table-header>-->
<!--    <v-data-table-->
<!--      v-bind:headers="pizzaTableHeaders"-->
<!--      v-bind:items="order.custom_pizzas"-->
<!--      v-bind:items-per-page="5"-->
<!--    ></v-data-table>-->
<!--    -->

<!--    <v-data-table-header>Bevande</v-data-table-header>-->
<!--    <v-data-table-->
<!--      v-bind:headers="pizzaTableHeaders"-->
<!--      v-bind:items="order.custom_pizzas"-->
<!--      v-bind:items-per-page="5"-->
<!--    ></v-data-table>-->

  </v-card>
</template>

<style scoped>

</style>