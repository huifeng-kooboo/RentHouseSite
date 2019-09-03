<template>
    <!--添加房屋信息 展示给访客-->
  <div id="div_add_house">
    <!--主要为添加房源功能：针对于管理者，为项目特有，故放在projects模块-->
    <!--先放置常用导航栏模块-->
    <VNavbar></VNavbar>
    <h2>添加房源</h2>
    <p>上传图片</p>
    <!-- el-upload 上传
    limit:限制上传照片数量：5
    multiple：表示允许上传多张图片
    accept:允许上传的图片类型
    :action="UploadUrl" 自定义上传，这里使用先保存全局变量的方法,原因是，没法保存图片
    -->
    <el-upload
      class="upload_housejpg"
      action="https://jsonplaceholder.typicode.com/posts/"
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
            curVal:2
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
          console.log(file, fileList);
        },
        handlePreview(file) {
          console.log(file);
        },
        uploadExceed(){
          //超过5张图限制处理
          alert("上传数量超出限制，最多只允许5张图，联系QQ：942840260");
        },
        onBeforeUpload(file){
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
        onSuccessUpload(file,fileList){
          alert("恭喜上传成功");
          console.log(this.curVal);
        },
        UploadUrl(){

        },
        //功能
      }
    }
</script>

<style scoped>

</style>
