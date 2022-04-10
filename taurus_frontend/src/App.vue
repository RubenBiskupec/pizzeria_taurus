<script>
import mapActions from 'vuex'

import ToolBar from "@/components/ToolBar";
import axios from "axios";

export default {
  name: 'App',
  components: {
    ToolBar
  },
  methods: {

  },
  beforeCreate() {
    this.$store.dispatch("initialize");
    // const token = this.$store.getters.token;
    // if (token) {
    //   axios.defaults.headers.common["Authorization"] = "Token " + token;
    // } else {
    //   axios.defaults.headers.common["Authorization"] = ""
    // }
  },
  async created() {
    await this.$store.dispatch("fetchIngredients");
    await this.$store.dispatch("fetchPizzaTypes");
    await this.$store.dispatch("fetchSizes");
    await this.$store.dispatch("fetchDoughs");
    await this.$store.dispatch("fetchMenuPizzas");
    await this.$store.dispatch("fetchBeverages");
  }

};
</script>

<template>
  <v-app>

    <ToolBar></ToolBar>
      <v-main>
        <router-view/>
      </v-main>
  </v-app>
</template>

<style>



</style>
