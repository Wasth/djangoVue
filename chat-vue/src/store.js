import Vue from "vue";
import Vuex from "vuex";
import $ from 'jquery';


Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        url: 'http://localhost:8000/',
        user_token: sessionStorage.getItem('auth_token') || ''
    },
    getters: {
        getVal(state) {
            return state.url;
        },
        getToken(state) {
            return state.user_token
        },
        checkUser(state) {
            return state.user_token !== null;
        }
    },
    mutations: {
        SET_TOKEN(state, payload) {
            state.user_token = payload
        }
    },
    actions: {
        AUTH_USER({commit}, {login, pass}) {
            new Promise((resolve, reject) => {
                $.ajax({
                    url: this.getters.getVal + 'auth/token/create/',
                    type: 'POST',
                    async: false,
                    data: {
                        username: login,
                        password: pass
                    },
                    success: (response) => {
                        sessionStorage.setItem('auth_token', response.data.attributes.auth_token),
                            commit('SET_TOKEN', response.data.attributes.auth_token);
                        return response.status;
                    },
                    error: (response) => {
                        sessionStorage.removeItem('auth_token')
                        return response.status;
                    }
                })
            });
        },
    }
});
