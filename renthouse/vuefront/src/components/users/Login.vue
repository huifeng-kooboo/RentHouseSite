<template>
   <div>
    <h2>登录界面</h2>

  <form action="api/login/" method="post">
     用户名:<input type="text" name="username"/>
    密码:<input type="password" name="password">
    <input type="submit" value="提交"/>
  </form>
   </div>
</template>

<script>
    export default {
        name: "Login"
    }
</script>

<style scoped>

</style>
