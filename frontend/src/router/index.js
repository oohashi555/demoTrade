import { createRouter, createWebHistory } from 'vue-router';
import LoginView from '../components/LoginView';
import TestView from '../components/TestView';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {name: 'Login',  path: '/',  component: LoginView},
    {name: 'Test',  path: '/test',  component: TestView},
  ],
});

export default router;