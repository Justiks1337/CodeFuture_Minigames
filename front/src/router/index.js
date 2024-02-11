import { createRouter, createWebHistory } from 'vue-router';
import GameList from '@/components/Home/GameList/GameList.vue';

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: GameList,
    },
    {
      path: '/queue/:game',
      name: 'loading',
      component: () => import('@/components/Loading/LoadingPage.vue')
    },
    { 
      path: '/:pathMatch(.*)',
      name: 'error-page',
      component: () => import('@/components/ErrorPage/ErrorPage.vue') 
    },
  ],
})