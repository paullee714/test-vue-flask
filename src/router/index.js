import Vue from 'vue';
import VueRouter from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import SignupPage from '@/views/SignupPage';

Vue.use(VueRouter);

const routes = [
    {
        path: '/login',
        component: LoginPage,
    },
    {
        path: '/signup',
        component: SignupPage,
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
