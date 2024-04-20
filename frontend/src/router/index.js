import { createRouter, createWebHistory } from 'vue-router';
import LoginView from '../components/LoginView';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {name: 'Login',  path: '/',  component: LoginView}
  ],
});

export default router;
