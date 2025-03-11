import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/order',
      name: 'create order',
      component: () => import('../views/CreateOrderView.vue'),
    },
    {
      path: '/waypoint',
      name: 'create waypoint',
      component: () => import('../views/CreateWaypointView.vue'),
    },
  ],
})

export default router
