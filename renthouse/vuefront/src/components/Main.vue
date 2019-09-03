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
          //渲染模板前进行操作
      },
      mounted(){
        //设置请求类型：get/json,方便服务端检查
          var get_data = {'house_data':'1'}; //发送get_data =1 请求得到所有房源信息
          //对dom进行操作，即赋值等操作
        this.$axios(
          {
            url:"api/addhouse/", //请求的url 由于跨域
            method:'get',
            data:JSON.stringify(get_data),
          }
        );
      },
      watch(){
          //监听相关
      },
      destroyed()
      {
      },
      //方法类
      methods:{
      }
    }
</script>

<style scoped>
</style>
