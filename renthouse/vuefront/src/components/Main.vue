<!--主界面-->
<template>
    <div id = "main_page">
      <router-link to="/login"> <el-button type="primary" id="cur_jj">测试</el-button></router-link>
      <div id="app">
        小举动
      </div>
    </div>
</template>

<script>
    export default {
        name: "Main"
    }


</script>

<style scoped>
  #cur_jj {
    font-family:Consolas;
    font-size: 20px;
  }
</style>
