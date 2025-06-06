import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Chat from '../views/Chat.vue'
import Chat2 from '../views/Chat2.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/chat', name: 'Chat', component: Chat },
  { path: '/chat2', name: 'Chat2', component: Chat2 },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
