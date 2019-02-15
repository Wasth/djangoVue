<template>
    <div id="app">
        <nav class="navbar navbar-dark bg-dark">
            <router-link class="navbar-brand" to="/">Чат на Vue js</router-link>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText"
                    aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav mr-auto">
                    <li v-for="(item, i) in menu" :key="i" data-toggle="collapse" data-target="#navbarText"
                        @click="clickMenu"
                        :class=" i == 0 ? 'nav-item active' : 'nav-item'">
                        <router-link class="nav-link" :to="item.route">{{item.title}}</router-link>
                    </li>
                </ul>
            </div>
        </nav>
        <div class="card">
            <router-view/>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'App',
        computed: {
            menu() {
                return [
                    {
                        title: 'Главная',
                        route: '/'
                    },
                    {
                        title: 'Чат',
                        route: '/chat'
                    },
                    {
                        title: 'Профиль',
                        route: '/profile'
                    },
                ]
            }
        },
        methods: {
            clickMenu(e) {
                $(".nav-item").removeClass('active');
                $(e.target).addClass('active');
            }
        }
    }
</script>

<style>
    .card {
        margin: 10px 15px 0 15px;
        padding: 10px;
    }

    .a {
        color: hsla(0, 0%, 100%, .5);
    }
</style>
