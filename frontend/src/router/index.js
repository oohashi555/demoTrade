import { createRouter, createWebHistory } from 'vue-router';
import LoginView from '../components/LoginView';
import TopView from '../components/TopView';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {name: 'login',  path: '/',  component: LoginView},
    {name: 'top',  path: '/top',  component: TopView}
  ],
});

export default router
