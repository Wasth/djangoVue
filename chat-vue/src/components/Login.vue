<template>
    <div id="login">
        <input v-model="login" type="text">
        <input v-model="password" type="password">
        <button @click="signin">Enter</button>
        <br>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "login",
        data() {
            return {
                login: '',
                password: ''
            }
        },
        methods: {
            signin() {
                this.$store.dispatch('AUTH_USER', {login: this.login, pass: this.password}).then(() => {
                    if (this.$store.getters.getToken.trim() !== '') {
                        this.$router.push({name: 'home'});
                    } else {
                        console.log('y');
                        this.showFalse = true;
                    }


                });
            }
        }
    }
</script>

<style scoped>

</style>
