<template>
    <div class="login">
        <button @click="login">Log In</button>
    </div>
</template>

<script>
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
    }
}
</script>