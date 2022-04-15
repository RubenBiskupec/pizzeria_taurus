<script>
export default {
  name: "OrderList",
  data () {
    return {
      orderTableHeaders: [
        {
          text: 'Id ordine',
          align: 'start',
          sortable: true,
          value: 'id',
        },
        { text: 'Data consegna', sortable: true, value: 'delivery_date' },
        { text: 'Ora consegna', value: 'delivery_time' },
        { text: 'Indirizzo', value: 'address' },
        { text: 'Totale', align: 'end', sortable: true, value: 'total_price' },
      ],
    }
  },
  computed: {
    orderUserList() {
      return this.$store.getters.orderUserList;
    }
  }
}
</script>

<template>
  <v-card>
    <v-card-title>Lista ordini</v-card-title>
    <v-data-table
      v-bind:headers="orderTableHeaders"
      v-bind:items="orderUserList"
      v-bind:items-per-page="5"
    ></v-data-table>
  </v-card>
</template>

<style scoped>

</style>