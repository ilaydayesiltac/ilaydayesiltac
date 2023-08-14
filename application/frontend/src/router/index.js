import VueRouter, { createRouter, createWebHashHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import ResultView from '@/views/ResultView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/result',
    name: 'result',
    component: ResultView,
  },
  {
    path: '/about/:input',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import('../components/Signup.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../components/Login.vue'),
  },
  {
    path: '/ForgotPassword',
    name: 'ForgotPassword',
    component: () => import('../components/ForgotPassword.vue'),
  },
];


const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
