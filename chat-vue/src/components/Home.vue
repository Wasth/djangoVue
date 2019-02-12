<template>
    <div id="home">
        <h1>Чат на Vue js</h1>
        <button v-if="!auth" @click="signin">Sign in</button>
        <button v-else @click="logout">Sign out</button>
        <room v-if="auth"></room>
    </div>
</template>

<script>
    import Room from './Room'

    export default {
        name: "Home",
        components:{
            Room
        },
        computed:{
            auth(){
                if(sessionStorage.getItem('auth_token')){
                    return true
                }
            }
        },
        methods: {
            signin() {
                this.$router.push({name: 'login'})
            },
            logout(){
                sessionStorage.removeItem('auth_token')
                window.location = '/'
            }
        }
    }
</script>

<style scoped>

</style>
