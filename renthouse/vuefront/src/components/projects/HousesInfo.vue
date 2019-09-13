<template>
<!--房源信息模块-->
  <!--Project包主要存放各种项目需要的安装模块-->
  <el-main>
    <!--房源名-->
    <h2>厦门第五房</h2>
    <!--房源图片-->
    <el-avatar shape="square" :size="size" :src="squareUrl"></el-avatar>
    <a href="/housedetail">点击查看详情</a>
  </el-main>
</template>

<script>
    export default {
        name: "HousesInfo",
      methods:{
      },
        created(){

        },
      mounted(){
            //请求api/briefhouseinfo接口get请求 获取数据 展示
          this.$axios(
              {
                  url:"api/briefhouseinfo/", //请求的url 由于跨域
                  method:'get',
              }
          ).then(
              function (return_data) {
              }
          ).catch(
          )
      },
      watch:{
      },
        data(){
            return{
                squareUrl:'https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png'
            }
        },
    }
</script>

<style scoped>

</style>
