<template>
    <!--添加房屋信息 展示给访客-->
  <div id="div_add_house">
    <!--主要为添加房源功能：针对于管理者，为项目特有，故放在projects模块-->
    <!--先放置常用导航栏模块-->
    <VNavbar></VNavbar>
    <!-- el-upload 上传
    limit:限制上传照片数量：5
    multiple：表示允许上传多张图片
    accept:允许上传的图片类型
    :action="UploadUrl" 自定义上传，这里使用先保存全局变量的方法,原因是，没法保存图片
          action="https://jsonplaceholder.typicode.com/posts/"
    -->
    <el-row :gutter="25">
      <el-col :span="3"><p>上传房源照片:</p></el-col>
      <el-col :span="6"><el-upload
        class="upload_housejpg"
        action="/api/addphoto/"
        accept="image/jpeg,image/gif,image/png"
        :before-upload="onBeforeUpload"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :on-success = 'onSuccessUpload'
        :on-change = 'changeUploadFile'
        :file-list="fileList"
        multiple
        :limit="5"
        :on-exceed="uploadExceed"
        list-type="picture">
        <el-button size="small" style="padding: 10px" type="primary">上传房源图片</el-button>
        <div slot="tip" class="el-upload__tip">格式允许jpg/png,最多允许上传5张图</div>
      </el-upload></el-col>
    </el-row>

    <el-row :gutter="25">
      <el-col :span="3" style="padding: 20px"><p>请输入房源名字：</p></el-col>
      <el-col :span="6" style="padding: 10px">  <el-input id="input_title" v-model="input_title" suffix-icon="el-icon-message" placeholder = "请输入房源名字" clearable></el-input></el-col>
    </el-row>
    <el-row :gutter="25">
      <el-col :span="3" style="padding: 20px"><p>请输入房源介绍：</p></el-col>
      <el-col :span="6" style="padding: 10px">  <el-input id="input_interview" v-model="input_interview" suffix-icon="el-icon-message" placeholder = "请输入房源介绍" clearable></el-input></el-col>
    </el-row>
    <el-row :gutter="25">
      <el-col :span="3" style="padding: 20px">请输入房屋价格：</el-col>
      <el-col :span="6" style="padding: 10px;"><el-input id="input_price"   v-model="input_price" suffix-icon="el-icon-user" placeholder = "请输入房屋价格" clearable></el-input></el-col>
    </el-row>
    <el-row :gutter="25">
      <el-col :span="3" style="padding: 20px;">请输入房屋住址：</el-col>
     <el-col :span="6" style="padding: 10px;"> <el-input id="input_address"   v-model="input_address" suffix-icon="el-icon-place" placeholder = "请输入房屋住址" clearable></el-input></el-col>
    </el-row>
    <el-row :gutter="25">
      <el-col :span="3" style="padding: 20px">请输入联系手机号：</el-col>
      <el-col :span="6" style="padding: 10px;"> <el-input id="input_phone"   v-model="input_phone" suffix-icon="el-icon-phone" placeholder = "请输入联系手机号" clearable></el-input></el-col>
    </el-row>
    <el-row :gutter="25">
      <el-col :span="3" style="padding: 20px">请输入业主姓名：</el-col>
      <el-col :span="6" style="padding: 10px">    <el-input id="input_name"  v-model="input_name" suffix-icon="el-icon-female" placeholder = "请输入业主姓名" clearable></el-input></el-col>
    </el-row>
    <el-button type="primary"  id="post_add" @click="addPost">添加</el-button>
  </div>
</template>

<script>
     import Navbar from '../tools/Navbar'
     let FILES_LIST ;//主要是存放所有的文件列表，用于发送数据
    export default {
        name: "AddHouse",
      data(){
          return{
            //绑定相应的数据信息
            fileList: [{name: 'food.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}, {name: 'food2.jpeg', url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100'}],
           //相关需要post的参数
            input_title :'房源名字',
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
          /*
          * begin
          * @brief:存放所有的上传图片类的方法
          *
          * */
          //移除方法
        handleRemove(file, fileList) {
          FILES_LIST = fileList;
        },
        //@brief :点击图片事件
        handlePreview(file) {
          //@brief :前面
        },
        //@brief :超过限制事件
        uploadExceed(){
          //超过限制张数处理事件
          alert("上传数量超出限制，最多只允许5张图，联系QQ：942840260");
        },
        //改变移除 都会触发该事件
        changeUploadFile(file,fileList){
          FILES_LIST = fileList;
          console.log(typeof FILES_LIST);
        },
        //上传前
        onBeforeUpload(file){
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
        //上传成功
        onSuccessUpload(response,file,fileList){
          FILES_LIST = fileList;
          //上传成功处理事件
        },
        /*
        * end
        * */

        //提交到数据库添加
        addPost(){
          var reader = new FileReader();
          reader.readAsBinaryString(FILES_LIST[0]);
          console.log(FILES_LIST[0]);
          let params = new FormData();//创建form对象
          params.append('file',reader.result);
          params.append('basic_interviews',this.input_interview);
          params.append('house_price',this.input_price);
          params.append('house_position',this.input_address);
          params.append('connect_phone',this.input_phone);
          params.append('renter_name',this.input_name);
          let config = {
            headers:{'Content-Type':'multipart/form-data'}
          }; //添加请求头
          this.$http.post('api/addhouse/',params,config)
            .then(response=>{
              console.log(response.data);
              //添加成功后返回当前界面
            });
        },
      }
    }
</script>

<style scoped>
#post_add{
  display:block;
  position: relative;
  top: 30px;
  left: 100px;
}
</style>
