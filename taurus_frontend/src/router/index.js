import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import MenuView from "@/views/MenuView";
import OrderView from "@/views/OrderView";
import AccessView from "@/views/AccessView";
import AccountView from "@/views/AccountView";
import store from "@/store";
import CustomerOrders from "@/views/TodayCustomerOrdersView";


Vue.use(VueRouter)

const routes = [
  {
    path: '*',
    name: 'default',
    component: HomeView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/menu',
    name: 'menu',
    component: MenuView
  },
  {
    path: '/order',
    name: 'order',
    component: OrderView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/admin/orders/today',
    name: 'customerOrders',
    component: CustomerOrders,
  },
  ,
  {
    path: '/admin/orders',
    name: 'customerAllOrders',
    component: CustomerAllOrders,
  },
  {
    path: '/access',
    name: 'access',
    component: AccessView
  },
  {
    path: '/account',
    name: 'account',
    component: AccountView,
    meta: {
      requireLogin: true
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.getters.isAuthenticated){
    next({
      name: "access",
      query: { to: to.path }
    });
  } else {
    next();
  }
})

export default router
