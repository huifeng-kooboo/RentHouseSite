<!--主界面-->
<template>
    <div id = "main_page">
      <!-- VNavbar 引入导航栏模块-->
      <VNavbar></VNavbar>
      <!--添加走马灯，用于展示最新房源信息-->
      <el-carousel trigger="click" height="300px">
        <el-carousel-item v-for="(jpgurl,index) in jpgurls" :key="jpgurl">
          <el-image
            :src="jpgurl.cur_url"
            :fit="cover"></el-image>
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
            jpgurls:[
                {
                    cur_url:'',
                }
            ],
       //   input_username:this.$route.params.phone_number, //此处可以设置 获取传值信息 直接绑定到输入框
        }
        },
      created(){
          //渲染模板前进行操作
      },
      mounted(){
            let that = this;
            //尽量都添加token
          let cur_headers = {'Authorization':"JWT " + localStorage.getItem('token')};//暂时不加 主要是用于游客访问 怕有bug
          //对dom进行操作，即赋值等操作
          this.$axios({
              url:'api/ads/',
              method:'get',
          }).then(
              function (res) {
                  let cur_count = res.data['count'];
                  console.log(res.data['results']);
                  let i = 0;
                  for (;i<cur_count;i++)
                  {
                      let push_data = {'cur_url':res.data['results'][i]['adphoto']};
                      that.jpgurls.unshift(push_data);
                  }
                  that.jpgurls.pop();
              }
          ).catch(
              function (res) {
                  //异常处理
              }
          )
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
