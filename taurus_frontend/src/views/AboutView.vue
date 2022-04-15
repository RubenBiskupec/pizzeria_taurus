<script>

import { HttpService } from "@/services/HttpService";

export default {
  name: 'AboutView',
  data() {
    return {
      reviews: [],
      httpService: new HttpService(),
    }
  },
  async created() {
    this.reviews = await this.httpService.getReviews();
  },
  mounted() {
    document.title = "About | Taurus";
  }
}
</script>

<template>
  <v-container class="about">
    <v-row>
      <v-col
        v-for="review in reviews"
        v-bind:key="review.id"
      >
        <v-card max-width="300">
          <v-card-title>{{ review.title }}</v-card-title>
          <v-card-text>
            <v-row
              align="center"
              class="mx-0"
            >
              <v-rating
                v-bind:value="review.stars"
                color="secondary"
                dense
                readonly
                size="14"
              ></v-rating>
            </v-row>
            <v-row class="py-2 px-4">
              {{ review.description }}
            </v-row>
            <v-row>
              <v-col align="right">
                - {{ review.user.first_name }} {{ review.user.last_name }}
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
