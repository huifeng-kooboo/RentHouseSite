<!--主界面-->
<template>
    <div id = "main_page">
      <!-- VNavbar 引入导航栏模块-->
      <VNavbar></VNavbar>
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
