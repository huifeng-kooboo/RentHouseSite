<template>
  <div>
    <VNavbar></VNavbar>
    <h2>厦门第五房</h2>
    <!--房源图片-->
    <el-avatar shape="square" :size="size" :src="squareUrl"></el-avatar>
    <h3>房屋简单介绍如下：这房子很好看</h3>
    <h3>当前房价：900元</h3>
    <h3>房屋位置：广东省深圳</h3>
    <h3>手机号：13824464121</h3>
    <h3>房东名：正吃哈</h3>
    <el-button type="primary">联系房东</el-button>
  </div>

</template>

<script>
  import Navbar from "../tools/Navbar";
    export default {
        name: "HouseDetail",
        components:{
            'VNavbar':Navbar, //加载导航栏
        },
        data(){
            return{
                squareUrl:'https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png',
            }
        }
    }
</script>

<style scoped>

</style>
