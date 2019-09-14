<!--主界面-->
<template>
    <div id = "main_page">
      <!-- VNavbar 引入导航栏模块-->
      <VNavbar></VNavbar>
      <!--添加走马灯，用于展示最新房源信息-->
      <el-carousel trigger="click" height="300px">
        <el-carousel-item v-for="item in 4" :key="item">
          <h3 class="small">{{ item }}</h3>
        </el-carousel-item>
      </el-carousel>
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
       //   input_username:this.$route.params.phone_number, //此处可以设置 获取传值信息 直接绑定到输入框
        }
        },
      created(){
          //渲染模板前进行操作
      },
      mounted(){
          //对dom进行操作，即赋值等操作
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

  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

</style>
