import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
    {
        path: '*',
        component: () => import('@/views/NotFoundPage.vue'),
    },
    {
        path: '/',
        redirect: '/login',
    },
    {
        path: '/login',
        component: () => import('@/views/LoginPage.vue'),
    },
    {
        path: '/signup',
        component: () => import('@/views/SignupPage.vue'),
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
