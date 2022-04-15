<script>
import {HttpService} from "@/services/HttpService";

export default {
  name: "ReviewUpdateDeleteForm",
  data() {
    return {
      reviewId: null,
      orderUpdate: null,
      titleUpdate: "",
      descriptionUpdate: "",
      starsUpdate: null,

      successUpdateNotification: "",
      errorUpdateNotification: "",

      httpService: new HttpService(),
    }
  },
  computed: {
    orderUserList() {
      return this.$store.getters.orderUserList;
    }
  },
  watch: {
    async orderUpdate(value) {
      this.reviewId = null;
      this.titleUpdate = "";
      this.descriptionUpdate = "";
      this.starsUpdate = null;

      if (value != null) {
        let review = await this.httpService.getReview(value);
        if (review != null) {
          this.reviewId = review.id;
          this.titleUpdate = review.title;
          this.descriptionUpdate = review.description;
          this.starsUpdate = review.stars;
        }
      }
    }
  },
  methods: {
    updateReview: function() {

      const reviewForm = {
        id: this.reviewId,
        order: this.orderUpdate,
        title: this.titleUpdate,
        description: this.descriptionUpdate,
        stars: this.starsUpdate
      }

      this.httpService.updateReview(reviewForm, this.successCallback, this.errorCallback);
    },
    deleteReview: function() {
      this.httpService.deleteReview(this.reviewId, this.successCallback, this.errorCallback);
    },
    successCallback: function(responseData) {
      this.orderUpdate = null,
      this.reviewId = null;
      this.titleUpdate = null;
      this.descriptionUpdate = null;
      this.starsUpdate = null;

      this.successUpdateNotification = "Recensione aggiornata con successo!";
      this.errorUpdateNotification = "";
    },
    errorCallback: function(error) {
      this.successUpdateNotification = "";
      this.errorUpdateNotification = "Qualcosa e' andato storto! Riprovare.";
      console.log(JSON.stringify(error));
    }
  }
}
</script>

<template>
  <v-card>
    <v-card-title>Modifica o Elimina Recensioni</v-card-title>
    <v-card-subtitle>Inserissci l'id dell'ordine della recensione che vuoi modificare</v-card-subtitle>
    <v-form>
      <v-row class="ma-2">
        <v-col cols="12">
          <v-autocomplete
            dense
            outlined
            label="Id ordine"
            v-model="orderUpdate"
            v-bind:items="orderUserList"
            item-text="id"
          ></v-autocomplete>
        </v-col>
        <v-col cols="12">
          <v-text-field
            dense
            outlined
            label="Titolo recensione"
            v-model="titleUpdate"
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
            v-model="descriptionUpdate"
          ></v-textarea>
        </v-col>
        <v-col cols="12" align="center">
          <v-rating
            v-model="starsUpdate"
            color="secondary"
            background-color="grey darken-1"
            empty-icon="$ratingFull"
            hover
            large
          ></v-rating>
        </v-col>
        <v-col cols="6" align="left">
          <v-btn
            color="primary"
            dense
            v-on:click="deleteReview"
          >
            Elimina
          </v-btn>
        </v-col>
        <v-col cols="6" align="right">
          <v-btn
            color="secondary"
            dense
            v-on:click="updateReview"
          >
            Modifica
          </v-btn>
        </v-col>
      </v-row>

      <v-divider
        v-if="successUpdateNotification != ''"
        class="my-4"
      ></v-divider>
      <v-row
        v-if="successUpdateNotification != ''"
        class="px-4 py-2 v-row-sign-up"
      >
        <v-col cols="12"
          class="px-4 py-2 my-2 rounded accent"
        >
          {{ successUpdateNotification }}
        </v-col>
      </v-row>

      <v-divider
        v-if="errorUpdateNotification != ''"
        class="my-4"
      ></v-divider>
      <v-row
        v-if="errorUpdateNotification != ''"
        class="px-4 py-2 v-row-sign-up"
      >
        <v-col cols="12"
          class="px-4 py-2 my-2 rounded primary"
        >
          {{ errorUpdateNotification }}
        </v-col>
      </v-row>

    </v-form>
  </v-card>
</template>

<style scoped>

</style>