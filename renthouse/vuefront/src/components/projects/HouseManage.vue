<template>
    <!--房源管理，方便房东进行修改或者删除房源-->
  <div>
   <VNavbar></VNavbar>
   <h2>房源管理界面</h2>
  </div>
</template>

<script>
    import Navbar from "../tools/Navbar";

    export default {
        name: "HouseManage",
      components:{
          VNavbar:Navbar,
      }
    }
</script>

<style scoped>

</style>
