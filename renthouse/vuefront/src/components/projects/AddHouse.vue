<template>
    <!--添加房屋信息 展示给访客-->
  <div id="div_add_house">
    <!--主要为添加房源功能：针对于管理者，为项目特有，故放在projects模块-->
    <!--先放置常用导航栏模块-->
    <VNavbar></VNavbar>
    <el-row :gutter="25">
      <el-col :span="3"> <p>  上传房源照片:</p></el-col>
      <!--限制只能传一张 保证不乱-->
      <el-col :span="6"><el-upload
        class="upload_housejpg"
        action="/api/addphoto/"
        :auto-upload="false"
        accept="image/jpeg,image/gif,image/png"
        :before-upload="onBeforeUpload"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :on-success = 'onSuccessUpload'
        :on-change = 'changeUploadFile'
        :file-list="fileList"
        ref = "uploadhousephoto"
        multiple
        :limit="1"
        :on-exceed="uploadExceed"
        list-type="picture">
        <el-button size="small" style="padding: 10px" type="primary">上传房源图片</el-button>
        <div slot="tip" class="el-upload__tip">格式允许jpg/png,最多允许上传1张图</div>
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
      <el-col :span="3" style="padding: 20px"><p>请输入房屋价格：</p></el-col>
      <el-col :span="6" style="padding: 10px;"><el-input id="input_price"   v-model="input_price" suffix-icon="el-icon-user" placeholder = "请输入房屋价格" clearable></el-input></el-col>
    </el-row>
    <el-row :gutter="25">
      <el-col :span="3" style="padding: 20px;"><p>请输入房屋住址：</p></el-col>
     <el-col :span="6" style="padding: 10px;"> <el-input id="input_address"   v-model="input_address" suffix-icon="el-icon-place" placeholder = "请输入房屋住址" clearable></el-input></el-col>
    </el-row>
    <el-row :gutter="25">
      <el-col :span="3" style="padding: 20px"><p>请输入联系手机号：</p></el-col>
      <el-col :span="6" style="padding: 10px;"> <el-input id="input_phone"   v-model="input_phone" suffix-icon="el-icon-phone" placeholder = "请输入联系手机号" clearable></el-input></el-col>
    </el-row>
    <el-row :gutter="25">
      <el-col :span="3" style="padding: 20px"><p>请输入业主姓名：</p></el-col>
      <el-col :span="6" style="padding: 10px">    <el-input id="input_name"  v-model="input_name" suffix-icon="el-icon-female" placeholder = "请输入业主姓名" clearable></el-input></el-col>
    </el-row>
    <el-tag type="warning">友情提示:房源名称不能相同，否则将无法添加房源信息成功</el-tag>
    <el-button type="primary"  id="post_add" @click="addPost">添加</el-button>
  </div>
</template>

<script>
     import Navbar from '../tools/Navbar'
    export default {
        name: "AddHouse",
      data(){
          return{
            //绑定相应的数据信息
            fileList:[],
           //相关需要post的参数
            input_title :'',
            input_interview:'',
            input_price:'',
            input_address:'',
            input_name:'',
            input_phone:'',
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
        },
        //@brief :点击图片事件
        handlePreview(file) {
          //@brief :前面
        },
        //@brief :超过限制事件
        uploadExceed(){
          //超过限制张数处理事件
          alert("上传数量超出限制，最多只允许1张图，联系QQ：942840260");
        },
        //@brief:改变移除文件 都会触发该事件
        changeUploadFile(file,fileList){

        },
        //上传前 ：也是主要上传处理逻辑的地方
        onBeforeUpload(file){
          const isIMAGE = file.type === 'image/jpeg'||'image/gif'||'image/png';
          const isLt5M = file.size / 1024 / 1024 < 5; //大小小于5M
          if (!isIMAGE) {
            alert('只允许上传图片');
            return isIMAGE;
          }
          if (!isLt5M) {
            alert('上传房源大小需要小于5M');
            return isLt5M;
          }

          //进行上传的功能
          //添加token
            let params = new FormData();//创建form对象
            params.append('file',file);
            params.append('house_title',this.input_title); //房源名字
            params.append('basic_interviews',this.input_interview); //简单介绍
            params.append('house_price',this.input_price); //房源价格
            params.append('house_position',this.input_address); //房源位置
            params.append('connect_phone',this.input_phone); //联系电话
            params.append('renter_name',this.input_name); //房东
            let config = {
                headers:{'Content-Type':'multipart/form-data','Authorization':"JWT " + localStorage.getItem('token')}
            }; //添加请求头
            this.$http.post('api/addhouse/',params,config)
                .then(response=>{
                    if(response.status == 200)
                    {
                        alert("上传失败！");
                        console.log(response.data);
                    }
                    else if(response.status == 201){
                        alert("添加成功！");
                        console.log(response.data);
                    }
                });
          return isIMAGE && isLt5M;
        },
        //上传成功
        onSuccessUpload(response,file,fileList){
          //上传成功处理事件
        },
        /*
        * end
        * */

        //提交到数据库添加
        addPost(){
            //调用另一个方法 发送数据
            this.$refs.uploadhousephoto.submit();
        },

       // post file 功能
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
