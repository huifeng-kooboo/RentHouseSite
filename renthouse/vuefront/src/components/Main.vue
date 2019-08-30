<!--主界面-->
<template>
    <div id = "main_page">
      <VNavbar></VNavbar>
      <!--引入导航栏组件-->
      <router-link to="/login"> <el-button type="primary" id="cur_jj">用户登录</el-button></router-link>
    </div>
</template>
<script>
     import LoginNavbar from './tools/LoginNavbar'
    export default {
        name: "Main",
        components:{
        VNavbar:LoginNavbar,
        },
    }
</script>

<style scoped>
</style>
