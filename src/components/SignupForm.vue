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
        <button type="submit">Signup</button>
        <p>{{ logMessage }}</p>
    </form>
</template>

<script>
import { registerUser } from '@/api/index';

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
        },
        initForm() {
            this.username = '';
            // this.email = '';
            this.nickname = '';
            this.password = '';
        },
    },
};
</script>

<style></style>
