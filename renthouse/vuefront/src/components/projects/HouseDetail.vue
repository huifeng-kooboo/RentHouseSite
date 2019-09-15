<template>
  <div>
    <VNavbar></VNavbar>
    <div id="div_brief">
      <el-tag >房屋名称：</el-tag>
      <el-tag type="success">{{ house_title }}</el-tag>
      <el-divider></el-divider>
      <el-image :src="house_images" style="width: 300px;height: 300px"></el-image>
      <el-divider></el-divider>
      <el-tag>简单介绍：</el-tag>
      <el-tag type="success">{{ basic_interviews }}</el-tag>
      <el-divider></el-divider>
      <el-tag>房屋价格：</el-tag>
      <el-tag type="success">{{ house_price }}</el-tag>
      <el-divider></el-divider>
      <el-tag>房屋住址：</el-tag>
      <el-tag type="success">{{ house_position }}</el-tag>
      <el-divider></el-divider>
      <el-tag>联系方式：</el-tag>
      <el-tag type="success">{{ connect_phone }}</el-tag>
      <el-divider></el-divider>
      <el-tag> 业主姓名：</el-tag>
      <el-tag type="success">{{ renter_name }}</el-tag>
      <el-divider></el-divider>
      <el-button type="primary">立即联系</el-button>
    </div>

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
                house_title:'',
                house_images:'https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png',
                basic_interviews:'',
                house_price:'',
                house_position:'',
                connect_phone:'',

            }
        },
        mounted() {
            let that = this;
            //处理路由
            let house_title = this.$route.params.housetitle; //获取房源名称
            console.log(house_title);
            that.house_title = house_title;
            let json_data = {'house_title':house_title};
            //发送get请求
            this.$axios.get('http://localhost:8080/api/housedetail/', {
                params: json_data
            })
                .then(function (response) {
                    if (response.status == 200)
                    {
                        //获取数据显示到前端
                        that.house_images = response.data['results'][0]['house_images'];
                        that.basic_interviews = response.data['results'][0]['basic_interviews'];
                        that.house_price = response.data['results'][0]['house_price'];
                        that.house_position = response.data['results'][0]['house_position'];
                        that.connect_phone = response.data['results'][0]['connect_phone'];
                        that.renter_name = response.data['results'][0]['renter_name'];
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    }
</script>

<style scoped>

</style>
