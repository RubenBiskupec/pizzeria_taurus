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
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    navigateToAccessView: function(){
      if (this.$route.name != "access"){
        this.$router.push("access");
      }
    },
    navigateToAccountView: function(){
      if (this.$route.name != "account"){
        this.$router.push("account");
      }
    }
  }
}
</script>

<template>
  <v-btn
    v-if="isAuthenticated"
    v-on:click="navigateToAccountView"
    small
    depressed
    color="secondary"
    class="ml-4 px-3 py-1"
  >
    <v-icon left>
      mdi-account
    </v-icon>
    Account
  </v-btn>
  <v-btn
    v-else
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