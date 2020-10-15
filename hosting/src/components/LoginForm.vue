<template>
    <div>
        <p><b>{{title}}</b></p>
        <form>
            <span>ID : </span>
            <input
                type="text"
                placeholder="input your id"
                v-model="loginForm.loginId"
            >
                <p>
                    Input loginId is {{ loginForm.loginId }}
                </p>
        </form>
    </div>
</template>

<script>
import LoginVue from '../views/Login.vue'
export default {
    props:{
        title: String
    },
    data: function(){
        return{
            loginForm:{
                loginId:null
            },
            Validation:{
                loginResult: ''
            }
        }
    },
    methods: {
        checkFrom: function(event) {
            var LoginId = false
            
            if (!this.loginForm.loginId) {
                this.Validation.loginResult="ログインIDを入力してください"
            } else if(!this.checkString(this.loginForm.loginId)){
                this.Validation.loginResult="半角英数で入力してください"
            } else{
                LoginId = true
            }

            if(LoginId == true){
                this.Validation.loginResult=""
                alert('Hello,' + this.loginForm.loginId + '!');
            }
            event.preventDefault()
        },
        checkString: function(inputdata){
            var re = /^[A-Za-z0-9]*$/
            return re.test(inputdata)
        }
    }
}
</script>

<style lang="stylus">
.error
    collor red
</style>