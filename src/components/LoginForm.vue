<template>
    <form @submit.prevent="submitForm">
        <div>
            <label for="username">username : </label>
            <input type="text" id="username" v-model="username" />
        </div>
        <div>
            <label for="password">password : </label>
            <input type="password" id="password" v-model="password" />
        </div>
        <button v-bind:disabled="!isUsernameValid" type="submit">Login</button>
        <p>{{ logMessage }}</p>
    </form>
</template>

<script>
import { loginUser } from '@/api/index';
import { validateEmail } from '@/util/validation';

export default {
    data() {
        return {
            username: '',
            password: '',
            logMessage: '',
        };
    },
    methods: {
        async submitForm() {
            try {
                let userData = {
                    username: this.username,
                    password: this.password,
                };
                let { data } = await loginUser(userData);
                this.$store.commit('setusername', data.user.nickname);
                console.log(data.user.nickname);
                this.$router.push('/main');
                // this.logMessage = `${data.user.nickname} 님 환영합니다`;
            } catch (error) {
                console.log(error);
            } finally {
                this.initForm();
            }
        },
        initForm() {
            this.username = '';
            this.password = '';
        },
    },
    computed: {
        isUsernameValid() {
            return validateEmail(this.username);
        },
    },
};
</script>

<style></style>
