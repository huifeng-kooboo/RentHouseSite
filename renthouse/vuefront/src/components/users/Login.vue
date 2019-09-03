<template>
   <div>
     <!-- 引入登录导航栏，后面登录成功后替换-->
     <VNavbar link_address="/login" link_title="租户登录"></VNavbar>
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
      },
      created() {
          //这里发送get请求 调用数据
      }
    }
</script>

<style scoped>

</style>
