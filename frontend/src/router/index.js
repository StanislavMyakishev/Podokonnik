import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/auth/Login.vue'
import Registration from '../components/auth/Registration.vue'
import Categories from '../components/pages/Categories.vue'
import Test from '../components/test/Test.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '',
            name: 'Home',
            component: Home
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/registartion',
            name: 'Registration',
            component: Registration
        },
        {
            path: '/categories',
            name: 'Categories',
            component: Categories
        },
        {
            path: '/test',
            name: 'Test',
            component: Test
        },
    ],
    mode: 'history',
})