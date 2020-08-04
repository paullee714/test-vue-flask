<template>
    <div class="home">
        <img alt="Vue logo" src="../assets/logo.png" />
        <HelloWorld msg="Welcome to Your Vue.js App" />
    </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';

export default {
    name: 'Home',
    components: {
        HelloWorld,
    },
    created() {
        // let a = 10; // veu.config.js로 에러를 back에서 확인
        // console.log("hi") // eslintrc.js 에서 console.log 환경설
    },
};
</script>
