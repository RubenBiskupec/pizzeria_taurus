<script>
export default {
  name: "AccessButton",
  data() {
    return {
      dialog: false,
      tab: 0,
      tabs: [
          'Accedi', 'Registrati'
      ]
    }
  },
  methods: {
    navigateToAccessView: function(){
      if (this.$route.name != "access"){
        this.$router.push("access");
      }
    }
  }
}
</script>

<template>
  <v-btn
    v-on:click="navigateToAccessView"
    small
    depressed
    color="secondary"
    class="ml-4 px-3 py-1"
  >
    <v-icon left>
      mdi-account
    </v-icon>
    Accedi
  </v-btn>
</template>

<style scoped>

</style>