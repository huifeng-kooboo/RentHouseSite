<template>
  <!--tools 主要存放相关可复用的组件包-->
  <!--导航栏组件-->
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-menu-item index="1"><a href="/main" target="blank">主页</a></el-menu-item>
    <el-submenu index="2">
      <template slot="title">个人中心</template>
      <el-menu-item index="2-1">个人信息设置</el-menu-item>
      <el-menu-item index="2-2">修改密码</el-menu-item>
      <el-menu-item index="2-3">退出登录</el-menu-item>
      <!-- 添加子导航栏方法
      <el-submenu index="2-4">
        <template slot="title">选项4</template>
        <el-menu-item index="2-4-1">选项1</el-menu-item>
        <el-menu-item index="2-4-2">选项2</el-menu-item>
        <el-menu-item index="2-4-3">选项3</el-menu-item>
      </el-submenu>
      -->
    </el-submenu>
    <!-- <el-menu-item index="3" disabled>消息中心</el-menu-item> disabled表示不可选 -->
    <!--  百度导航栏<el-menu-item index="4"><a href="https://www.baidu.com" target="blank">百度</a></el-menu-item> -->
  </el-menu>
</template>

<script>
    export default {
        name: "Navbar"
    }
</script>

<style scoped>

</style>
