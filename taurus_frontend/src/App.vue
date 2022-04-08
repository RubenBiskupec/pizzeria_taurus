<script>

import ToolBar from "@/components/ToolBar";

export default {
  name: 'App',
  components: {
    ToolBar
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
