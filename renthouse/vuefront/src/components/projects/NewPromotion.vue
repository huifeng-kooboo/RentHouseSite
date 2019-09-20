<template>
    <!--最新活动页面：主要展示最新活动信息，
    后续完善-->
  <div>
    <!--添加常规导航栏-->
    <VNavbar></VNavbar>
  <h2>展示最新活动信息</h2>
  </div>
</template>

<script>
  //import Navbar from './tools/Navbar'
  import Navbar from '../tools/Navbar'
    export default {
        name: "NewPromotion",
        components:{
          VNavbar:Navbar,
        }
    }
</script>

<style scoped>

</style>
