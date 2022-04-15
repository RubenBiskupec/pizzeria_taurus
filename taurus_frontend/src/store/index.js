import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import { HttpService } from "@/services/HttpService";
import axios from "axios";
import order from "@/components/Order";

const httpService = new HttpService();

export default new Vuex.Store({
  state: {
    userInfo: {},
    ingredients: [],
    pizzaTypes: [],
    sizes: [],
    doughs: [],
    menuPizzas: [],
    beverages: [],
    cart: {
      custom_pizzas: [],
      custom_pizzas_long: [],
      half_meter_pizzas: [],
      half_meter_pizzas_long: [],
      beverages: [],
      beverages_long: [],
    },
    orderUserList: [],
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
    userInfo(state) {
      return state.userInfo;
    },
    ingredients(state) {
      return state.ingredients;
    },
    availableIngredients(state) {
      if (state.ingredients != null) {
        return state.ingredients.filter(ingredient => ingredient.is_in_stock);
      } else {
        return state.ingredients;
      }
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
      if (state.doughs != null) {
        return state.doughs.filter(dough => dough.is_in_stock);
      } else {
        return state.doughs;
      }
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
      if (state.beverages != null) {
        return state.beverages.filter(beverage => beverage.is_in_stock);
      } else {
        return state.beverages;
      }
    },
    cart(state) {
      return state.cart;
    },
    orderUserList(state) {
      return state.orderUserList;
    }
  },
  mutations: {
    INITIALIZE(state) {
      if(localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        axios.defaults.headers.common["Authorization"] = "Token " + state.token;
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
        axios.defaults.headers.common["Authorization"] = "";
      }
    },
    SET_TOKEN(state, token) {
      state.token = token;
      state.isAuthenticated = true;
      localStorage.setItem("token", token);
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    },
    REMOVE_TOKEN (state) {
      state.token = "";
      state.isAuthenticated = false;
      localStorage.removeItem("token");
      axios.defaults.headers.common["Authorization"] = "";
    },
    SET_USER_INFO(state, userInfo) {
      state.userInfo = userInfo;
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
    },
    ADD_CUSTOM_PIZZA_TO_CART(state, customPizza) {
      // deve aggiungere solo l'ID
      state.cart.custom_pizzas.push(customPizza["id"]);
      state.cart.custom_pizzas_long.push(customPizza);
    },
    // todo aggiungi bevande e mezzi metri
    SET_ORDER_USER_LIST(state, orderUserList) {
      state.orderUserList = orderUserList;
    }
  },
  actions: {
    initialize({commit}) {
      commit('INITIALIZE');
    },
    setToken({commit}, token) {
      commit('SET_TOKEN', token);
    },
    removeToken({commit}) {
      commit('REMOVE_TOKEN');
    },
    async fetchUserInfo({commit}) {
      const data = await httpService.getUserInfo();
      commit('SET_USER_INFO', data)
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
    },
    addCustomPizzaToCart({commit}, customPizza) {
      commit('ADD_CUSTOM_PIZZA_TO_CART', customPizza);
    },
    async fetchOrderUserList({commit}) {
      const data = await httpService.getOrderUserList();
      commit('SET_ORDER_USER_LIST', data);
    },
    async fetchTodayOrders({commit}) {
      const data = await httpService.getTodayOrders();
      commit('SET_TODAY_ORDERS', data);
    }
  },
  modules: {
  }
})
