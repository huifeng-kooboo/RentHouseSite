<template>
  <div id="div_login_nav">
    <!--tools 主要存放相关可复用的组件包-->
    <!--导航栏组件-->
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1"><a href="/main" target="blank">主页</a></el-menu-item>
      <el-menu-item index="2" id="el_login"><a :href ="link_address"  id="a_tag_login" target="blank">{{link_title}}</a></el-menu-item>
    </el-menu>
  </div>
</template>

<script>
    export default {
      name: "LoginNavbar",
      props:["link_address","link_title"],
      methods:{
      }
    }


</script>

<style scoped>
#el_login{
  position:absolute;
  right:10px;
}
</style>
