<template>
    <form @submit.prevent="submitForm">
        <div>
            <label for="username">이메일 : </label>
            <input type="text" id="username" v-model="username" />
        </div>
        <!--        <div>-->
        <!--            <label for="email">이메일 : </label>-->
        <!--            <input type="email" id="email" v-model="email" />-->
        <!--        </div>-->
        <div>
            <label for="nickname">닉네임 : </label>
            <input type="text" id="nickname" v-model="nickname" />
        </div>
        <div>
            <label for="password">비밀번호 : </label>
            <input type="password" id="password" v-model="password" />
        </div>
        <button type="submit" v-bind:disabled="!isUsernameValid">Signup</button>
        <p>{{ logMessage }}</p>
    </form>
</template>

<script>
import { registerUser } from '@/api/index';
import { validateEmail } from '@/util/validation';

export default {
    data() {
        return {
            username: '',
            // email: '',
            nickname: '',
            password: '',
            logMessage: '',
        };
    },
    methods: {
        async submitForm() {
            console.log(this.username);
            let userData = {
                username: this.username,
                // email: this.email,
                nickname: this.nickname,
                password: this.password,
            };
            const { data } = await registerUser(userData);
            console.log(data.username);
            this.logMessage = `${data.nickname} 님이 가입되었습니다! `;
            this.initForm();
            this.$router.push('/login');
        },
        initForm() {
            this.username = '';
            // this.email = '';
            this.nickname = '';
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
