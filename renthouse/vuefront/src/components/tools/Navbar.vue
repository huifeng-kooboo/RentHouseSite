<template>
  <!--tools 主要存放相关可复用的组件包-->
  <!--导航栏组件-->
  <div id="div_navbar_person">

    <!--普通租户展示的导航栏-->
  <el-menu id="nav_normal" v-if="showNormal" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" >
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
      <!--<el-menu-item index="3-2">立即缴费</el-menu-item>-->
    </el-submenu>
  </el-menu>

    <!--游客专用导航栏-->
    <el-menu id="nav_visitor" v-if="showVisitor" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1"><a href="/main" target="blank">主页</a></el-menu-item>
      <el-link type="primary" href="/login" id="link_login">用户登录</el-link>
      <el-link type="success" href="/register" id="link_register">用户注册</el-link>
    </el-menu>

    <!--管理员导航栏-->
    <el-menu id="nav_admin" v-if="showAdmin" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" >
      <el-menu-item index="1"><a href="/main" target="blank">主页</a></el-menu-item>
      <el-submenu index="2">
        <template slot="title">个人中心</template>
        <el-menu-item index="2-1"><a id="a_myinfo" href="/myinfo">个人信息设置</a></el-menu-item>
        <el-menu-item index="2-2"><a id="a_modify" href="/modifypassword">修改密码</a></el-menu-item>
        <el-menu-item index="2-3" @click="clearToken">注销</el-menu-item>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">管理中心</template>
        <el-menu-item index="3-1"><a href="/tenant">添加租户</a></el-menu-item>
        <el-menu-item index="3-2"><a href="/allrenters">租户管理</a></el-menu-item> <!--修改提交的房源信息等-->
        <el-menu-item index="3-3"><a href="/addhouse">添加房源</a></el-menu-item> <!--此处为房东增加房源功能-->
        <el-menu-item index="3-4"><a href="/housemanage">房源管理</a></el-menu-item> <!--此处为房东增加房源功能-->
        <el-menu-item index="3-5"><a href="/adphoto">广告投放管理</a></el-menu-item>
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
          showNormal:false,
          showVisitor:false,
          showAdmin:false,
        };
      },
      mounted(){
          //发送请求 判断等级
         let that = this;
          let token_data = localStorage.getItem('token'); //判断是否有token数据
        //token为空 说明是未登录状态 展示游客菜单栏
         if (token_data == null)
         {
           this.showVisitor = true; //展示游客模式
           return;
         }
         //token存在 请求获取用户信息及权限
         let json_token = {'token':token_data};
         this.$axios(
           {
             url:'http://localhost:8080/api/anatoken/', //解决housedetail问题
             method: 'post',
             data:JSON.stringify(json_token),
           }
         ).then(
           function (res) {
            let permission = res.data['permission'];
            console.log(permission);
             if(permission == "admin")
             {
              that.showAdmin = true;
             }
             else if(permission == "visitor")
             {
               that.showVisitor = true;
             }
             else{
               that.showNormal = true;
             }
           }
         );
      },
      methods:{
          handleSelect(){

          },
        //注销功能
         clearToken(){
            localStorage.removeItem('token'); //清除token；
            window.location.href='/main'; //重新返回主页
          }
      },
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
