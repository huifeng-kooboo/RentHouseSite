<template>
  <!--费用清单List-->
    <div>
      <!--添加常规导航栏-->
      <VNavbar></VNavbar>
      <h2>费用清单</h2>
    </div>
</template>

<script>
  import Navbar from '../tools/Navbar'
    export default {
        name: "FeeList",
      components:{
          VNavbar:Navbar,
      },
    }
</script>

<style scoped>

</style>
