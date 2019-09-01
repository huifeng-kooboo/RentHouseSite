<!--主界面-->
<template>
    <div id = "main_page">
      <!-- VNavbar 引入导航栏模块-->
      <VNavbar></VNavbar>
      <el-input id="username" class="username" v-model="input_username" suffix-icon="el-icon-user" placeholder = "请输入用户名"></el-input>
    </div>
</template>
<script>
     import LoginNavbar from './tools/LoginNavbar'
    export default {
        name: "Main",
        components:{
        VNavbar:LoginNavbar,
        },
      data(){
        return{
          input_username:this.$route.params.phone_number, //此处可以设置 获取传值信息 直接绑定到输入框
        }
        }
    }
</script>

<style scoped>
</style>
