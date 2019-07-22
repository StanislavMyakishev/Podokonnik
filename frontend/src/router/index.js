import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/auth/Login.vue'
import Registration from '../components/auth/Registration.vue'

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

    ],
    mode: 'history',
})