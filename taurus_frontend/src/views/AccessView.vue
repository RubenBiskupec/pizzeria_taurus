<script>

import LogIn from "@/components/LogIn";
import SignUp from "@/components/SignUp";

export default {
  name: "AccessView",
  components: {
    LogIn, SignUp
  },
  data() {
    return {
      tab: 0,
      tabs: [
          'Accedi', 'Registrati'
      ],
    }
  },
  methods: {
    setTab(tab) {
      this.tab = tab;
    }
  },
  mounted() {
    document.title = "Accedi | Taurus";
  }
}
</script>

<template>
  <v-container>

    <v-row>
      <v-spacer></v-spacer>
      <v-col
        cols="12"
        sm="10"
        md="8"
      >
        <v-card
          flat
        >
          <v-tabs
            v-model="tab"
            background-color="secondary"
            centered
          >
            <v-tabs-slider color="primary"></v-tabs-slider>
            <v-tab
              v-for="tab in tabs"
              v-bind:key="tab"
              color="secondary"
            >
              {{ tab }}
            </v-tab>
          </v-tabs>

          <LogIn
            v-show="tab==0"
            v-on:setTab="setTab"
          ></LogIn>

          <SignUp
            v-show="tab==1"
            v-on:setTab="setTab"
          ></SignUp>

        </v-card>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>

  </v-container>
</template>

<style scoped>

</style>