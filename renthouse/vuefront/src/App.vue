<template>

  <!--导航栏-->
  <div id="div_init">
    <!--主要入口处，即为所有网页的入口-->
    <!-- router-view 为替换后面模块的地方 -->
    <router-view/>
  </div>
</template>
<script>
  // <!--引入相关库-->
  import 'bootstrap/dist/css/bootstrap.min.css'
  import 'bootstrap/dist/js/bootstrap'
  import 'at-ui'
  import 'at-ui-style'
export default {
  name: 'App',
}
</script>
<style scoped>
/*#app {*/
/*  font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
/*  -webkit-font-smoothing: antialiased;*/
/*  -moz-osx-font-smoothing: grayscale;*/
/*  text-align: center;*/
/*  color: #2c3e50;*/
/*  margin-top: 60px;*/
/*}*/
</style>
