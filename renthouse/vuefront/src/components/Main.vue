<!--主界面-->
<template>
    <div id = "main_page">
      <!--引入导航栏组件-->
      <router-link to="/login"> <el-button type="primary" id="cur_jj">用户登录</el-button></router-link>
    </div>
</template>
<script>
     //import Navbar from './tools/Navbar'
    export default {
        name: "Main"
    }
</script>

<style scoped>
</style>
