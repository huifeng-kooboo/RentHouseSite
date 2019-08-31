<template>
   <div>
     <!-- 引入登录导航栏，后面登录成功后替换-->
     <VNavbar></VNavbar>
     <VLoginForm></VLoginForm>
   </div>
</template>

<script>
    import LoginNavbar from '../tools/LoginNavbar'
    import LoginForm from '../tools/LoginForm'
    export default {
        name: "Login",
        components:{
        VNavbar:LoginNavbar,
        VLoginForm:LoginForm,
      }
    }
</script>

<style scoped>

</style>
