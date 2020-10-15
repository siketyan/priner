<template>
    <div class="login">
        <LoginForm title="propでtitleに渡す"></LoginForm>
        <hr>
        <button @click="login">Log In</button>
    </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'

export default {
    name: 'login',
    data(){
        return{
            username: '',
            password: ''
        }
    },
    methods:{
        login: function(){
            this.$router.push('/')
        }
    },
    components: {
        LoginForm
    }
}
</script>