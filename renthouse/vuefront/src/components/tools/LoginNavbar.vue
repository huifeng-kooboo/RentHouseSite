<template>
  <div id="div_login_nav">
    <!--tools 主要存放相关可复用的组件包-->
    <!--导航栏组件-->
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1"><a href="/main" target="blank">主页</a></el-menu-item>
      <el-menu-item index="2" id="el_login"><a href="/login" target="blank">租户登录</a></el-menu-item>
    </el-menu>
  </div>
</template>

<script>
    export default {
        name: "LoginNavbar"
    }
</script>

<style scoped>
#el_login{
  position:absolute;
  right:10px;
}
</style>
