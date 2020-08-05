<template>
    <header>
        <div>
            <router-link to="/login">로그인</router-link> |
            <router-link to="/signup">회원가입</router-link>

            <span> {{ $store.state.username }}</span>
        </div>
    </header>
</template>

<script>
export default {};
</script>
