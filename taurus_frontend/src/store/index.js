import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import { HttpService } from "@/services/HttpService";

const httpService = new HttpService();

export default new Vuex.Store({
  state: {
    ingredients: [],
    pizzaTypes: [],
    sizes: [],
    doughs: [],
    menuPizzas: [],
    beverages: [],
    isAuthenticated: false,
    token: '',
  },
  getters: {
    token(state) {
      return state.token;
    },
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
    ingredients(state) {
      return state.ingredients;
    },
    availableIngredients(state) {
      return state.ingredients.filter(ingredient => ingredient.is_in_stock);
    },
    pizzaTypes(state) {
      return state.pizzaTypes;
    },
    sizes(state) {
      return state.sizes;
    },
    doughs(state) {
      return state.doughs;
    },
    availableDoughs(state) {
      return state.doughs.filter(dough => dough.is_in_stock);
    },
    menuPizzas(state) {
      return state.menuPizzas;
    },
    availableMenuPizzas(state) {
      let availableMenuPizzas = []
      for(const i in state.menuPizzas) {
        let areAllAvailable = true;
        for(const j in state.menuPizzas[i].ingredients) {
          if (!state.menuPizzas[i].ingredients[j].is_in_stock) {
            areAllAvailable = false;
          }
        }
        if(areAllAvailable) {
          availableMenuPizzas.push(state.menuPizzas[i]);
        }
      }
      return availableMenuPizzas;
    },
    beverages(state) {
      return state.beverages;
    },
    availableBeverages(state) {
      return state.beverages.filter(beverage => beverage.is_in_stock);
    }
  },
  mutations: {
    INITIALIZE(state) {
      if(localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }
    },
    SET_TOKEN(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    REMOVE_TOKEN (state, token) {
      state.token = "";
      state.isAuthenticated = false;
    },
    SET_INGREDIENTS(state, ingredients) {
      state.ingredients = ingredients;
    },
    SET_PIZZA_TYPES(state, pizzaTypes) {
      state.pizzaTypes = pizzaTypes;
    },
    SET_SIZES(state, sizes) {
      state.sizes = sizes;
    },
    SET_DOUGHS(state, doughs) {
      state.doughs = doughs;
    },
    SET_MENU_PIZZAS(state, menuPizzas) {
      state.menuPizzas = menuPizzas;
    },
    SET_BEVERAGES(state, beverages) {
      state.beverages = beverages;
    }
  },
  actions: {
    initialize({commit}) {
      commit('INITIALIZE');
    },
    setToken({commit}, token) {
      commit('SET_TOKEN', token);
    },
    async fetchIngredients({commit}) {
      const data = await httpService.getMenuEntity("Ingredient");
      commit('SET_INGREDIENTS', data);
    },
    async fetchPizzaTypes({commit}) {
      const data = await httpService.getMenuEntity("PizzaType");
      commit('SET_PIZZA_TYPES', data);
    },
    async fetchSizes({commit}) {
      const data = await httpService.getMenuEntity("Size");
      commit('SET_SIZES', data);
    },
    async fetchDoughs({commit}) {
      const data = await httpService.getMenuEntity("Dough");
      commit('SET_DOUGHS', data);
    },
    async fetchMenuPizzas({commit}) {
      const data = await httpService.getMenuEntity("MenuPizza");
      commit('SET_MENU_PIZZAS', data);
    },
    async fetchBeverages({commit}) {
      const data = await httpService.getMenuEntity("Beverage");
      commit('SET_BEVERAGES', data);
    }

  },
  modules: {
  }
})
