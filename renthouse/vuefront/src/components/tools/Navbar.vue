<template>
  <!--tools 主要存放相关可复用的组件包-->
  <!--导航栏组件-->
  <div id="div_navbar_person">

    <!--普通租户展示的导航栏-->
  <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" >
    <el-menu-item index="1"><a href="/main" target="blank">主页</a></el-menu-item>
    <el-submenu index="2">
      <template slot="title">个人中心</template>
      <el-menu-item index="2-1"><a id="a_myinfo" href="/myinfo">个人信息设置</a></el-menu-item>
      <el-menu-item index="2-2"><a id="a_modify" href="/modifypassword">修改密码</a></el-menu-item>
      <el-menu-item index="2-4" @click="clearToken">退出登录</el-menu-item>
    </el-submenu>
    <el-submenu index="3">
      <template slot="title" >租户缴费</template>
      <el-menu-item index="3-1"><a id="a_feelist" href="/feelist">费用清单</a></el-menu-item>
      <el-menu-item index="3-2">立即缴费</el-menu-item>
    </el-submenu>
  </el-menu>

    <!--游客专用导航栏-->
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" hidden>
      <el-menu-item index="1"><a href="/main" target="blank">主页</a></el-menu-item>
      <el-link type="primary" href="/login" id="link_login">用户登录</el-link>
      <el-link type="success" href="/register" id="link_register">用户注册</el-link>
    </el-menu>

    <!--管理员导航栏-->
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" hidden>
      <el-menu-item index="1"><a href="/main" target="blank">主页</a></el-menu-item>
      <el-submenu index="2">
        <template slot="title">个人中心</template>
        <el-menu-item index="2-1"><a id="a_myinfo" href="/myinfo">个人信息设置</a></el-menu-item>
        <el-menu-item index="2-2"><a id="a_modify" href="/modifypassword">修改密码</a></el-menu-item>
        <el-menu-item index="2-3"><a href="/logout">注销</a></el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">管理中心</template>
        <el-menu-item index="3-1"><a href="/tenant">租户管理</a></el-menu-item>
        <el-menu-item index="3-2">房源管理</el-menu-item> <!--修改提交的房源信息等-->
        <el-menu-item index="3-3"><a href="/addhouse">添加房源</a></el-menu-item> <!--此处为房东增加房源功能-->
      </el-submenu>
    </el-menu>

  </div>
</template>
<script>
    export default {
        name: "Navbar",
      data() {
        return {
          activeIndex: '1',
        };
      },
      methods:{
          handleSelect(){

          },
        //注销功能
         clearToken(){
            localStorage.removeItem('token'); //清除token；
            window.location.href='/main'; //重新返回主页
          }
      }
    }
</script>

<style scoped>
#a_login{
  color:black;
}
#link_login{
  position: relative;
  top:20px;
  left: 10px;
}
#link_register{
  position: relative;
  top:20px;
  left:20px;
}
</style>
