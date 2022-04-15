<script>
import { HttpService } from "@/services/HttpService";

export default {
  name: "ReviewForm",
  data() {
    return {
      order: null,
      title: "",
      description: "",
      stars: 5,

      successNotification: "",
      errorNotification: "",

      httpService: new HttpService(),
    }
  },
  computed: {
    orderUserList() {
      return this.$store.getters.orderUserList;
    }
  },
  methods: {
    submitReview: function() {

      const reviewForm = {
        order: this.order,
        title: this.title,
        description: this.description,
        stars: this.stars
      }

      this.httpService.submitReview(reviewForm, this.successCallback, this.errorCallback);
    },
    successCallback: function(responseData) {
      this.errorNotification = "";
      this.successNotification = "Recensione eseguita con successo!";
    },
    errorCallback: function(error) {
      this.successNotification = "";
      this.errorNotification = "Qualcosa e' andato storto! Riprovare.";
      console.log(JSON.stringify(error));
    }
  }
}
</script>

<template>
  <v-card>
    <v-card-title>Recensioni</v-card-title>
    <v-card-subtitle>Lascia una recensione per un ordine</v-card-subtitle>
    <v-form>
      <v-row class="ma-2">
        <v-col cols="12">
          <v-autocomplete
            dense
            outlined
            label="Id ordine"
            v-model="order"
            v-bind:items="orderUserList"
            item-text="id"
          ></v-autocomplete>
        </v-col>
        <v-col cols="12">
          <v-text-field
            dense
            outlined
            label="Titolo recensione"
            v-model="title"
          ></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-textarea
            dense
            outlined
            auto-grow
            row="3"
            clearable
            label="Descrizione recensione"
            v-model="description"
          ></v-textarea>
        </v-col>
        <v-col cols="12" align="center">
          <v-rating
            v-model="stars"
            color="secondary"
            background-color="grey darken-1"
            empty-icon="$ratingFull"
            hover
            large
          ></v-rating>
        </v-col>
        <v-col cols="12" align="right">
          <v-btn
            color="secondary"
            dense
            v-on:click="submitReview"
          >
            Conferma
          </v-btn>
        </v-col>
      </v-row>

      <v-divider
        v-if="successNotification != ''"
        class="my-4"
      ></v-divider>
      <v-row
        v-if="successNotification != ''"
        class="px-4 py-2 v-row-sign-up"
      >
        <v-col cols="12"
          class="px-4 py-2 my-2 rounded accent"
        >
          {{ successNotification }}
        </v-col>
      </v-row>

      <v-divider
        v-if="errorNotification != ''"
        class="my-4"
      ></v-divider>
      <v-row
        v-if="errorNotification != ''"
        class="px-4 py-2 v-row-sign-up"
      >
        <v-col cols="12"
          class="px-4 py-2 my-2 rounded primary"
        >
          {{ errorNotification }}
        </v-col>
      </v-row>

    </v-form>
  </v-card>
</template>

<style scoped>

</style>