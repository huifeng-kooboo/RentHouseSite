<template>
   <div>
     <!-- 引入登录导航栏，后面登录成功后替换-->
     <VNavbar></VNavbar>
  <form action="api/login/" method="post">
     用户名:<input type="text" name="username"/>
    密码:<input type="password" name="password">
    <input type="submit" value="提交"/>
  </form>
   </div>
</template>

<script>
    import LoginNavbar from '../tools/LoginNavbar'
    export default {
        name: "Login",
        components:{
        VNavbar:LoginNavbar,
      },
    }
</script>

<style scoped>

</style>
