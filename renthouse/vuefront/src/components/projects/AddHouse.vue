<template>
    <!--添加房屋信息 展示给访客-->
  <div id="div_add_house">
    <!--主要为添加房源功能：针对于管理者，为项目特有，故放在projects模块-->
    <!--先放置常用导航栏模块-->
    <VNavbar></VNavbar>
    <p>上传图片</p>
    <!-- el-upload 上传
    limit:限制上传照片数量：5
    multiple：表示允许上传多张图片
    accept:允许上传的图片类型
    :action="UploadUrl" 自定义上传，这里使用先保存全局变量的方法,原因是，没法保存图片
          action="https://jsonplaceholder.typicode.com/posts/"
    -->
    <el-upload
      class="upload_housejpg"
      action="/api/addphoto/"
      accept="image/jpeg,image/gif,image/png"
      :before-upload="onBeforeUpload"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :on-success = 'onSuccessUpload'
      :file-list="fileList"
      multiple
      :limit="5"
      :on-exceed="uploadExceed"
      list-type="picture">
      <el-button size="small" type="primary">上传房源图片</el-button>
      <div slot="tip" class="el-upload__tip">格式允许jpg/png,最多允许上传5张图</div>
    </el-upload>
    <el-input id="input_interview"  v-model="input_interview" suffix-icon="el-icon-message" placeholder = "请输入房源介绍" clearable></el-input>
    <el-input id="input_price"  v-model="input_price" suffix-icon="el-icon-user" placeholder = "请输入房屋价格" clearable></el-input>
    <el-input id="input_address"  v-model="input_address" suffix-icon="el-icon-place" placeholder = "请输入房屋住址" clearable></el-input>
    <el-input id="input_phone"  v-model="input_phone" suffix-icon="el-icon-phone" placeholder = "请输入联系手机号" clearable></el-input>
    <el-input id="input_name"  v-model="input_name" suffix-icon="el-icon-female" placeholder = "请输入业主姓名" clearable></el-input>
    <el-button type="primary" v-model="fileas" id="post_add" @click="addPost">添加</el-button>
  </div>
</template>

<script>
  import Navbar from '../tools/Navbar'
    export default {
        name: "AddHouse",
      data(){
          return{
            //绑定相应的数据信息
            fileList: [{name: 'food.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}, {name: 'food2.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}],
           //相关需要post的参数
            input_interview:'safsafsasf',
            input_price:'1331',
            input_address:'asfsasdsf',
            input_name:'asfsasfa',
            input_phone:'13332244',
          }
      },
       components:{
         VNavbar:Navbar,
      },
      created() {
      },
      mounted() {
      },
      destroyed() {
      },
      methods:{
          //存放各种方法类
        //此处存放上传图片各种操作
        handleRemove(file, fileList) {
          //@brief :移除图片事件
        },
        handlePreview(file) {
          //@brief :前面
        },
        uploadExceed(){
          //超过限制张数处理事件
          alert("上传数量超出限制，最多只允许5张图，联系QQ：942840260");
        },
        onBeforeUpload(file){
          //@brief:上传前处理事件
          //上传前，检查数据类型
          const isIMAGE = file.type === 'image/jpeg'||'image/gif'||'image/png';
          const isLt1M = file.size / 1024 / 1024 < 1; //大小小于1M
          if (!isIMAGE) {
            alert('只允许上传图片');
          }
          if (!isLt1M) {
            alert('上传照片大小需要小于1M');
          }
          return isIMAGE && isLt1M;
        },
        onSuccessUpload(response,file,fileList){
          //上传成功处理事件
        },
        //提交到数据库添加
        addPost(){
          const that = this; //that用于重定向页面时候调用
          //post数据整合
          //bug 就是处理House_images事件
          var post_data = {"house_images":"","basic_interviews":this.input_interview,"house_price":parseInt(this.input_price),
          "house_position":this.input_address,"connect_phone":this.input_phone,"renter_name":this.input_name};
          //使用axios发送
          this.$axios(
            {
              url:'api/addhouse/',
              method:'post',
              data:JSON.stringify(post_data),
            }
          ).then(
            //捕获添加房源成功信息
            function (res) {
              if (res.status == 201)
              {
                alert("添加房源成功！");
              }
            }
          ).catch(
            //捕获异常
            function (res) {
              alert("异常，请联系QQ:942840260");
            }
          )
        }
      }
    }
</script>

<style scoped>

</style>
