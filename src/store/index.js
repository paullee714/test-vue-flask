import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        username: '',
    },
    mutations: {
        setusername(state, username) {
            state.username = username;
        },
    },
    actions: {},
    modules: {},
});
