import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Chat from '@/components/Room'
import Profile from '@/components/Profile'

Vue.use(Router)

export default new Router({
    mode: "history",
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '/chat',
            name: 'chat',
            component: Chat
        },
        {
            path: '/profile',
            name: 'profile',
            component: Profile
        },
    ]
})
