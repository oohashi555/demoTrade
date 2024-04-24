import { createRouter, createWebHistory } from 'vue-router';
import LoginView from '../components/LoginView';
import TopView from '../components/TopView';
import UserListView from '../components/UserListView';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {name: 'login',  path: '/',  component: LoginView},
    {name: 'top',  path: '/top',  component: TopView},
    {name: 'userList',  path: '/userList',  component: UserListView}
  ],
});

export default router
