<script>
import { HttpService } from "@/services/HttpService";
import store from "@/store";

export default {
  name: "MenuView",
  data () {
    return {
      dialog: false,
      selectedFilter: 'Pizze',
      filters: [
          'Pizze',
          'Calzoni',
          'Saltimbocca',
          'Bevande'
      ],
      httpService: new HttpService()
    }
  },
  computed: {
    menuPizzas() {
      return this.$store.getters.menuPizzas;
    },
    availableMenuPizzas() {
      return this.$store.getters.availableMenuPizzas;
    },
    pizzas() {
      let pizzas = [];
      const menuPizzas = this.availableMenuPizzas;
      for (const i in menuPizzas) {
        if (menuPizzas[i].pizza_type.code == "PZ") {
          pizzas.push(menuPizzas[i]);
        }
      }
      return pizzas;
    },
    calzoni() {
      let calzoni = [];
      const pizzas = this.availableMenuPizzas;
      for (const i in pizzas) {
        if (pizzas[i].pizza_type.code == "CA") {
          calzoni.push(pizzas[i]);
        }
      }
      return calzoni;
    },
    saltimbocca() {
      let saltimbocca = [];
      const pizzas = this.availableMenuPizzas;
      for (const i in pizzas) {
        if (pizzas[i].pizza_type.code == "SB") {
          saltimbocca.push(pizzas[i]);
        }
      }
      return saltimbocca;
    },
    pizzaTypes() {
      return this.$store.getters.pizzaTypes;
    },
    availableBeverages() {
      return this.$store.getters.availableBeverages;
    }
  },
  methods: {
    changeFilter(newFilter) {
      this.selectedFilter = newFilter;
      this.dialog = false;
    }
  },
  mounted() {
    document.title = "Menu | Taurus";
  }
}
</script>

<template>
  <v-container>

    <div
      class="hidden-md-and-down"
    >

      <v-navigation-drawer
        permanent
        class="menu-navigation absolute-left secondary"
      >
        <v-list class="pa-4">
          <v-list-item-title class="mb-3 color-primary text-h5">
            Menu'
          </v-list-item-title>
          <v-list-item
            v-for="filter in filters"
            v-bind:key="filter"
            class="color-primary"
          >
            <span class="px-2 py-1 rounded selected-filter" v-if="filter == selectedFilter">
              {{ filter }}
            </span>
            <span
              class="px-2 py-1 rounded menu-item"
              v-else
              v-on:click="changeFilter(filter)"
            >
              {{ filter }}
            </span>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-row
        class="menu-content"
        v-show="selectedFilter=='Pizze'"
      >
        <v-col
          v-for="menuPizza in pizzas"
          v-bind:key="menuPizza.code"
          cols="12"
          xs="12"
          sm="6"
          md="4"
          lg="3"
          xl="2"
        >
          <v-card>
            <v-card-title>
              {{ menuPizza.name }}
            </v-card-title>
            <v-divider></v-divider>
            <v-card-subtitle class="text-small text-subtitle-2">
              {{ menuPizza.description }}
            </v-card-subtitle>
            <v-card-text class="text-subtitle-2">
              Ingredienti:
              <span
                v-for="ingredient in menuPizza.ingredients"
              >
                {{ ingredient.name}}<span v-if="ingredient != menuPizza.ingredients[menuPizza.ingredients.length -1]">,</span>
              </span>
            </v-card-text>
            <v-card-text align="right">
              € {{ menuPizza.price }}
            </v-card-text>
          </v-card>
          <h3></h3>
          <h3></h3>
        </v-col>
      </v-row>

      <v-row
        class="menu-content"
        v-show="selectedFilter=='Calzoni'"
      >
        <v-col
          v-for="menuPizza in calzoni"
          v-bind:key="menuPizza.code"
          cols="12"
          xs="12"
          sm="6"
          md="4"
          lg="3"
          xl="2"
        >
          <v-card>
            <v-card-title>
              {{ menuPizza.name }}
            </v-card-title>
            <v-divider></v-divider>
            <v-card-subtitle class="text-small text-subtitle-2">
              {{ menuPizza.description }}
            </v-card-subtitle>
            <v-card-text class="text-subtitle-2">
              Ingredienti:
              <span
                v-for="ingredient in menuPizza.ingredients"
              >
                {{ ingredient.name}}<span v-if="ingredient != menuPizza.ingredients[menuPizza.ingredients.length -1]">,</span>
              </span>
            </v-card-text>
            <v-card-text align="right">
              € {{ menuPizza.price }}
            </v-card-text>
          </v-card>
          <h3></h3>
          <h3></h3>
        </v-col>
      </v-row>

      <v-row
        class="menu-content"
        v-show="selectedFilter=='Saltimbocca'"
      >
        <v-col
          v-for="menuPizza in saltimbocca"
          v-bind:key="menuPizza.code"
          cols="12"
          xs="12"
          sm="6"
          md="4"
          lg="3"
          xl="2"
        >
          <v-card>
            <v-card-title>
              {{ menuPizza.name }}
            </v-card-title>
            <v-divider></v-divider>
            <v-card-subtitle class="text-small text-subtitle-2">
              {{ menuPizza.description }}
            </v-card-subtitle>
            <v-card-text class="text-subtitle-2">
              Ingredienti:
              <span
                v-for="ingredient in menuPizza.ingredients"
              >
                {{ ingredient.name}}<span v-if="ingredient != menuPizza.ingredients[menuPizza.ingredients.length -1]">,</span>
              </span>
            </v-card-text>
            <v-card-text align="right">
              € {{ menuPizza.price }}
            </v-card-text>
          </v-card>
          <h3></h3>
          <h3></h3>
        </v-col>
      </v-row>

      <v-row
        class="menu-content"
        v-show="selectedFilter=='Bevande'"
      >
        <v-col
          v-for="beverage in availableBeverages"
          v-bind:key="beverage.code"
          cols="12"
          xs="12"
          sm="6"
          md="4"
          lg="3"
          xl="2"
        >
          <v-card>
            <v-card-title>
              {{ beverage.name }}
            </v-card-title>
            <v-divider></v-divider>
            <v-card-subtitle class="text-small text-subtitle-2">
              {{ beverage.description }} - {{ beverage.size }}
            </v-card-subtitle>
            <v-card-text align="right">
              € {{ beverage.price }}
            </v-card-text>
          </v-card>
          <h3></h3>
          <h3></h3>
        </v-col>
      </v-row>

    </div>

    <div
      class="hidden-lg-and-up"
    >

      <v-row class="secondary">
        <v-spacer></v-spacer>
        <v-col align="center"
          cols="10"
        >
          <v-dialog
            v-model="dialog"
            transition="dialog-bottom-transition"
            max-width="300"
          >
            <template v-slot:activator="{ on, attrs}">
              <v-btn
                v-bind="attrs"
                v-on="on"
                depressed
                large
                color="primary"
              >
                <v-icon left> mdi-menu </v-icon>
                Menu - {{ selectedFilter }}
              </v-btn>
            </template>
            <template v-slot:default="dialog">
              <v-card
                max-height="600"
              >
                <v-list class="secondary pa-4">
                  <v-list-item-title class="mb-3 color-primary text-h5">
                    Menu'
                  </v-list-item-title>
                  <v-list-item
                    v-for="filter in filters"
                    v-bind:key="filter"
                    class="color-primary"
                  >
                    <span class="px-2 py-1 rounded selected-filter" v-if="filter == selectedFilter">
                      {{ filter }}
                    </span>
                    <span
                      class="px-2 py-1 rounded menu-item"
                      v-else
                      v-on:click="changeFilter(filter)"
                    >
                      {{ filter }}
                    </span>
                  </v-list-item>
                </v-list>
              </v-card>
            </template>
          </v-dialog>

        </v-col>
        <v-spacer></v-spacer>
      </v-row>

      <v-row
        v-show="selectedFilter=='Pizze'"
      >
        <v-col
          v-for="menuPizza in pizzas"
          v-bind:key="menuPizza.code"
          cols="12"
          xs="12"
          sm="6"
          md="4"
          lg="3"
          xl="2"
        >
          <v-card>
            <v-card-title>
              {{ menuPizza.name }}
            </v-card-title>
            <v-divider></v-divider>
            <v-card-subtitle class="text-small text-subtitle-2">
              {{ menuPizza.description }}
            </v-card-subtitle>
            <v-card-text class="text-subtitle-2">
              Ingredienti:
              <span
                v-for="ingredient in menuPizza.ingredients"
              >
                {{ ingredient.name}}<span v-if="ingredient != menuPizza.ingredients[menuPizza.ingredients.length -1]">,</span>
              </span>
            </v-card-text>
            <v-card-text align="right">
              € {{ menuPizza.price }}
            </v-card-text>
          </v-card>
          <h3></h3>
          <h3></h3>
        </v-col>
      </v-row>

      <v-row
        v-show="selectedFilter=='Calzoni'"
      >
        <v-col
          v-for="menuPizza in calzoni"
          v-bind:key="menuPizza.code"
          cols="12"
          xs="12"
          sm="6"
          md="4"
          lg="3"
          xl="2"
        >
          <v-card>
            <v-card-title>
              {{ menuPizza.name }}
            </v-card-title>
            <v-divider></v-divider>
            <v-card-subtitle class="text-small text-subtitle-2">
              {{ menuPizza.description }}
            </v-card-subtitle>
            <v-card-text class="text-subtitle-2">
              Ingredienti:
              <span
                v-for="ingredient in menuPizza.ingredients"
              >
                {{ ingredient.name}}<span v-if="ingredient != menuPizza.ingredients[menuPizza.ingredients.length -1]">,</span>
              </span>
            </v-card-text>
            <v-card-text align="right">
              € {{ menuPizza.price }}
            </v-card-text>
          </v-card>
          <h3></h3>
          <h3></h3>
        </v-col>
      </v-row>

      <v-row
        v-show="selectedFilter=='Saltimbocca'"
      >
        <v-col
          v-for="menuPizza in saltimbocca"
          v-bind:key="menuPizza.code"
          cols="12"
          xs="12"
          sm="6"
          md="4"
          lg="3"
          xl="2"
        >
          <v-card>
            <v-card-title>
              {{ menuPizza.name }}
            </v-card-title>
            <v-divider></v-divider>
            <v-card-subtitle class="text-small text-subtitle-2">
              {{ menuPizza.description }}
            </v-card-subtitle>
            <v-card-text class="text-subtitle-2">
              Ingredienti:
              <span
                v-for="ingredient in menuPizza.ingredients"
              >
                {{ ingredient.name}}<span v-if="ingredient != menuPizza.ingredients[menuPizza.ingredients.length -1]">,</span>
              </span>
            </v-card-text>
            <v-card-text align="right">
              € {{ menuPizza.price }}
            </v-card-text>
          </v-card>
          <h3></h3>
          <h3></h3>
        </v-col>
      </v-row>

      <v-row
        v-show="selectedFilter=='Bevande'"
      >
        <v-col
          v-for="beverage in availableBeverages"
          v-bind:key="beverage.code"
          cols="12"
          xs="12"
          sm="6"
          md="4"
          lg="3"
          xl="2"
        >
          <v-card>
            <v-card-title>
              {{ beverage.name }}
            </v-card-title>
            <v-divider></v-divider>
            <v-card-subtitle class="text-small text-subtitle-2">
              {{ beverage.description }} - {{ beverage.size }}
            </v-card-subtitle>
            <v-card-text align="right">
              € {{ beverage.price }}
            </v-card-text>
          </v-card>
          <h3></h3>
          <h3></h3>
        </v-col>
      </v-row>

    </div>


  </v-container>
</template>

<style scoped>

.absolute-left {
  position: absolute;
  left: 0;
  top: 0;
}

.text-small {
  font-size: 0.85em !important;
}

.menu-navigation {
  width: 15% !important;
}

.color-primary {
  font-weight: bold;
  font-size: 1.2em;
  color: #D31837 !important;
}

.menu-content {
  position: absolute;
  right: 2%;
  width: 83% !important;
}

.selected-filter {
  background: #D31837;
  color: #DDB752;
}

.menu-item:hover {
  cursor: pointer;
  background: #D31837;
  color: #DDB752;
}

</style>