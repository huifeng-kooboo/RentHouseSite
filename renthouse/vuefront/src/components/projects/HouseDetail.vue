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
        },
        mounted() {
            //处理路由
            let house_title = this.$route.params.housetitle; //获取房源名称
            console.log(house_title);
            let json_data = {'house_title':house_title};
            //发送get请求
            this.$axios.get('http://localhost:8080/api/housedetail/', {
                params: json_data
            })
                .then(function (response) {
                    console.log(response);
                })
                .catch(function (error) {
                    console.log(error);
                });
            //发送get请求获取所有信息
            // this.$axios(
            //     {
            //         url:'http://localhost:8080/api/housedetail/',
            //         method:'get',
            //         params :JSON.stringify(json_data),
            //     }
            // ).then(
            //     function(res){
            //         console.log(res.data);
            //     }
            // );
        }
    }
</script>

<style scoped>

</style>
