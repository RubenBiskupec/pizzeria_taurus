<script>
import ToolBar from "@/components/ToolBar";

export default {
  name: 'App',
  components: {
    ToolBar
  },
  methods: {

  },
  beforeCreate() {
    this.$store.dispatch("initialize");
  },
  async created() {
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
