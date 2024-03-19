import Vue from 'vue'
import VueRouter from 'vue-router'
import { createRouter, createWebHistory } from "vue-router";

import TripCalculatorPage from '@/views/TripCalculatorPage.vue'
import Home from '@/views/Home.vue'
Vue.use(VueRouter)

const routes = [
    { path: '/', component: Home },
    { path: '/trips', component: TripCalculatorPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router
