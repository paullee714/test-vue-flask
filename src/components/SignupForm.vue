<template>
    <form @submit.prevent="submitForm">
        <div>
            <label for="username">이름 : </label>
            <input type="text" id="username" v-model="username" />
        </div>
        <div>
            <label for="email">이메일 : </label>
            <input type="email" id="email" v-model="email" />
        </div>
        <div>
            <label for="nickname">닉네임 : </label>
            <input type="text" id="nickname" v-model="nickname" />
        </div>
        <div>
            <label for="password">비밀번호 : </label>
            <input type="password" id="password" v-model="password" />
        </div>
        <button type="submit">Signup</button>
    </form>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            email: '',
            nickname: '',
            password: '',
        };
    },
    methods: {
        submitForm() {
            console.log(this.username);
        },
    },
};
</script>

<style></style>
