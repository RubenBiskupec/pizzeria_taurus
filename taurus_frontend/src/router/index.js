import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import MenuView from "@/views/MenuView";
import OrderView from "@/views/OrderView";
import AccessView from "@/views/AccessView";

Vue.use(VueRouter)

const routes = [
  {
    path: '*',
    name: 'home',
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
    component: OrderView
  },
    {
    path: '/access',
    name: 'access',
    component: AccessView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
