<script>

import AccessButton from "@/components/AccessButton";


export default {
  name: "ToolBar",
  components: {
    AccessButton,
  },
  data () {
    return {
      dialog: false,
      drawer: false,
      items: [
        {
          icon: 'mdi-home',
          text: 'Home',
          routerLink: 'home'
        },
        {
          icon: 'mdi-information',
          text: 'About',
          routerLink: 'about'
        },
        {
          icon: 'mdi-pizza',
          text: 'Menu',
          routerLink: 'menu'
        },
        {
          icon: 'mdi-moped',
          text: 'Ordina',
          routerLink: 'order'
        }
      ]
    }
  },
  methods: {
    navigateTo: function (routerLink){
      if (this.$route.name != routerLink){
        this.$router.push(routerLink);
      }
      this.dialog = false;
    }
  }
}
</script>


<template>
  <v-card
    flat
    height="48px"
    tile
    >
      <v-toolbar
        dense
        color="primary"
        class="hidden-sm-and-down golden-color"
      >
        <v-img
          src="../assets/logo_taurus_transparent.png"
          v-on:click="navigateTo('home')"
          max-height="40px"
          max-width="40px"
          class="logo"
        ></v-img>
        <v-toolbar-title class="pl-4 navbar-title">Pizzeria Taurus</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn
            v-for="item in items"
            v-bind:key="item.text"
            v-on:click="navigateTo(item.routerLink)"
            class="navbar-item golden-color"
            text
            small
          >
            {{ item.text }}
          </v-btn>
        </v-toolbar-items>
        <v-spacer></v-spacer>
        <AccessButton></AccessButton>
      </v-toolbar>

    <v-toolbar
        dense
        color="primary"
        class="hidden-md-and-up hidden-xs-only golden-color"
      >
        <v-img
          src="../assets/logo_taurus_transparent.png"
          max-height="40px"
          max-width="40px"
        ></v-img>
        <v-toolbar-title class="pl-4 navbar-title">Pizzeria Taurus</v-toolbar-title>
        <v-spacer></v-spacer>
        <AccessButton></AccessButton>
        <v-dialog
          v-model="dialog"
          hide-overlay
          transition="dialog-bottom-transition"
        >
          <template dark v-slot:activator="{ on, attrs }">
            <v-btn
              icon
              color="secondary"
              v-bind="attrs"
              v-on="on"
            >
              <v-icon>mdi-menu</v-icon>
            </v-btn>
          </template>
          <v-card class="custom-drawer">
            <v-list dense>
              <v-list-item
                v-for="(item, index) in items"
                v-bind:key="index"
                to="#"
                v-on:click="navigateTo(item.routerLink)"
              >
                <v-list-item-action>
                  <v-icon v-if="item.icon">{{item.icon}}</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    {{ item.text }}
                  </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-dialog>
      </v-toolbar>

    <v-toolbar
        dense
        color="primary"
        class="hidden-sm-and-up golden-color"
      >
        <v-img
          src="../assets/logo_taurus_transparent.png"
          max-height="40px"
          max-width="40px"
        ></v-img>
        <v-spacer></v-spacer>
        <AccessButton></AccessButton>
        <v-dialog
          v-model="dialog"
          hide-overlay
          transition="dialog-bottom-transition"
        >
          <template dark v-slot:activator="{ on, attrs }">
            <v-btn
              icon
              color="secondary"
              v-bind="attrs"
              v-on="on"
            >
              <v-icon>mdi-menu</v-icon>
            </v-btn>
          </template>
          <v-card class="custom-drawer">
            <v-list dense>
              <v-list-item
                v-for="(item, index) in items"
                v-bind:key="index"
                to="#"
                v-on:click="navigateTo(item.routerLink)"
              >
                <v-list-item-action>
                  <v-icon v-if="item.icon">{{item.icon}}</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    {{ item.text }}
                  </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-dialog>
      </v-toolbar>

    </v-card>
</template>


<style scoped>

.logo:hover {
  cursor: pointer;
}

.golden-color {
  color: #DDB752 !important;
}

.navbar-title {
  font-weight: bold;
  font-size: 1.5em;
}

.navbar-item {
  font-weight: bold;
  font-size: 0.9em !important;
}

.custom-drawer {
  position: absolute;
  top: 48px;
  right: 0;
  width: 250px;
}

</style>