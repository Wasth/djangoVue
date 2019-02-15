<template>
    <div id="login">
        <form id="signin_form">
            <div class="card">
                <div class="card-body">
                    <h1 class="card-title">Sign in</h1>
                    <input label="Login" v-model="login" type="text" placeholder="Login" />
                    <input label="Password" v-model="password" type="password" placeholder="Password" />
                </div>
            </div>
        </form>
        <button @click="cancel">Cancel</button>
        <button @click="signin">Enter</button>
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
            },
            cancel() {
                this.$router.push({name: 'home'})
            }
        }
    }
</script>

<style scoped>
    #signin_form {
        margin-left: 25%;
        margin-right: 25%;
    }
</style>
