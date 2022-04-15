<script>
import { HttpService } from "@/services/HttpService";
import OrderList from "@/components/OrderList";
import ReviewForm from "@/components/ReviewForm";
import ReviewUpdateDeleteForm from "@/components/ReviewUpdateDeleteForm";

export default {
  name: "AccountView",
  components: { OrderList, ReviewForm, ReviewUpdateDeleteForm },
  data () {
    return {
      logOutErrorMessage: "",
      httpService: new HttpService(),
    }
  },
  computed: {
    userInfo() {
      return this.$store.getters.userInfo;
    }
  },
  methods: {
    logOut() {
      this.httpService.logOut(this.successCallback, this.errorCallback);
    },
    successCallback(responseData) {
      this.$store.dispatch("removeToken");
      this.$router.push("access");
    },
    errorCallback(error) {
      this.logOutErrorMessage = "Qualcosa e' andato storto, riprova";
    },

    async getUserInfo() {
      this.userInfo = await this.httpService.getUserInfo()
    }
  },
  async created() {
    await this.$store.dispatch('fetchUserInfo');
    await this.$store.dispatch('fetchOrderUserList');
  },
}
</script>

<template>
  <v-container>

    <v-row class="ma-2">
      <v-col
        cols="12"
        lg="6"
        xl="4"
      >
        <v-card class="pa-2 my-4">
          <v-card-title>Il mio Account</v-card-title>
          <v-divider></v-divider>
          <v-card-subtitle></v-card-subtitle>
          <v-card-text>
            <v-text-field
              dense
              outlined
              readonly
              label="Email"
              v-bind:value="userInfo.email"
            ></v-text-field>
            <v-text-field
              dense
              outlined
              readonly
              label="Nome"
              v-bind:value="userInfo.first_name"
            ></v-text-field>
            <v-text-field
              dense
              outlined
              readonly
              label="Cognome"
              v-bind:value="userInfo.last_name"
            ></v-text-field>
            <v-text-field
              dense
              outlined
              readonly
              label="Indirizzo"
              v-bind:value="userInfo.address"
            ></v-text-field>
            <v-text-field
              dense
              outlined
              readonly
              label="Telefono"
              v-bind:value="userInfo.cellphone_number"
            ></v-text-field>
            <v-row>

            <v-col align="right">
              <v-btn
                color="primary"
                v-on:click="logOut"
              >Log Out</v-btn>
            </v-col>
          </v-row>

          </v-card-text>
        </v-card>
      </v-col>

      <v-col
        cols="12"
        lg="6"
        xl="4"
      >
        <OrderList class="pa-2 my-4"></OrderList>
      </v-col>

      <v-col
        cols="12"
        lg="6"
        xl="4"
      >
        <ReviewForm class="pa-2 my-4"></ReviewForm>
      </v-col>

      <v-col
        cols="12"
        lg="6"
        xl="4"
      >
        <ReviewUpdateDeleteForm class="pa-2 my-4"></ReviewUpdateDeleteForm>
      </v-col>

    </v-row>
  </v-container>
</template>

<style scoped>

</style>