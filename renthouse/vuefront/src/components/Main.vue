<!--主界面-->
<template>
    <div id = "main_page">
      <!-- VNavbar 引入导航栏模块-->
      <VNavbar></VNavbar>
      <el-input id="username" class="username" v-model="input_username" suffix-icon="el-icon-user" placeholder = "请输入用户名"></el-input>
      <VHouse></VHouse>
    </div>
</template>
<script>
     import LoginNavbar from './tools/LoginNavbar'
     import Navbar from './tools/Navbar'
     import HousesInfo from './projects/HousesInfo'
    export default {
        name: "Main",
        components:{
          VNavbar:Navbar,
          VHouse:HousesInfo
        },
      // 数据
      data(){
        return{
          input_username:this.$route.params.phone_number, //此处可以设置 获取传值信息 直接绑定到输入框
        }
        },
      created(){
          //初始化
        if (this.$route.params.phone_number)
        {
          alert("存在电话号码");
        }
        else {
          alert("不存在号码");
        }
      },
      //方法类
      methods:{
      }
    }
</script>

<style scoped>
</style>
