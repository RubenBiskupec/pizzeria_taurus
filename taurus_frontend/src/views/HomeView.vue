<script>
  export default {
    name: 'HomeView',
    mounted() {
      document.title = "Home | Taurus";
    }
  }
</script>

<template>
  <v-container class="home">

      <v-row>
        <v-col align="left">
          <v-card class="home-card">
             <v-card-title class="home-card">Pizzeria Taurus </v-card-title>
            <v-card-subtitle class="home-card">dal 1995</v-card-subtitle>
            <v-divider class="my-4"></v-divider>
            <v-card-text class="home-card">
              Pizza da asporto e a domicilio
            </v-card-text>
            <v-card-text class="home-card">
              327 8639759
            </v-card-text>
            <v-card-text class="home-card">
              370 3795657
            </v-card-text>
            <v-card-text class="home-card">
              Giorni lavorativi: Martedi' - Domenica
            </v-card-text>
            <v-card-text class="home-card">
              Orari lavorativi: 18:30 - 22:00
            </v-card-text>
            <v-card-text class="home-card">
              Via Fratelli Rosselli 227 - Modena
            </v-card-text>
            <v-card-text class="home-card">
              Tanti impasti alternativi su richiesta: Integrale biologico, Senatore Cappelli, Multicereali e tanti altri
            </v-card-text>
            <v-card-text class="home-card">
              Ampia selezione di birre artigianali
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

  </v-container>
</template>

<style scoped>

.home-card {
  font-size: 1.1em !important;
}
</style>