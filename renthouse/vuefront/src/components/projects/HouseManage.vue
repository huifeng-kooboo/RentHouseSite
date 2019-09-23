<template>
    <!--房源管理，方便房东进行修改或者删除房源-->
  <div>
   <VNavbar></VNavbar>
    <el-table
      :data="tableData"
      style="width: 100%">

      <!--添加选择框，用于批量删除房源使用-->
      <el-table-column
        type="selection"
        width="55">
      </el-table-column>

      <!--房屋图片-->
      <el-table-column
      label="房屋图片"
      width="100">
        <template slot-scope="scope">
          <el-image
            style="width: 100px; height: 100px"
            :src="scope.row.house_images"
            :fit="fit"></el-image>
        </template>
      </el-table-column>

      <!--房源名称 不可删除-->
      <el-table-column
        label="房源名称"
        width="180">
        <template slot-scope="scope">
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.house_title }}</el-tag>
            </div>
        </template>
      </el-table-column>

      <!--房源简单介绍-->
      <el-table-column
        label="简单介绍"
        width="180">
        <template slot-scope="scope">
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.basic_interviews }}</el-tag>
          </div>
        </template>
      </el-table-column>

      <!--房屋价格-->
      <el-table-column
        label="房屋价格"
        width="100">
        <template slot-scope="scope">
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.house_price }}</el-tag>
          </div>
        </template>
      </el-table-column>

      <!--房屋位置-->
      <el-table-column
        label="房屋位置"
        width="100">
        <template slot-scope="scope">
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.house_position }}</el-tag>
          </div>
        </template>
      </el-table-column>

      <!--联系手机号-->
      <el-table-column
        label="联系手机号"
        width="100">
        <template slot-scope="scope">
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.connect_phone }}</el-tag>
          </div>
        </template>
      </el-table-column>

      <!--租户名-->
      <el-table-column
        label="租户名"
        width="100">
        <template slot-scope="scope">
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.renter_name }}</el-tag>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-divider></el-divider>
    <el-button type="danger" round>批量删除</el-button>
    <el-tag @click="batchDelete" type="warning">友情提示：批量删除默认删除勾选部分</el-tag>

    <!--编辑框部分-->
    <el-dialog title="房源信息修改" style="font-size: 12px;" :visible.sync="dialogTableVisible">
      <!--修改自AddHouse.vue中的表单-->
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
        <el-col :span="6" style="padding: 10px">  <el-input :disabled="true" id="input_title" v-model="house_title" suffix-icon="el-icon-message" placeholder = "请输入房源名字" clearable></el-input></el-col>
      </el-row>
      <el-row :gutter="25">
        <el-col :span="3" style="padding: 20px"><p>请输入房源介绍：</p></el-col>
        <el-col :span="6" style="padding: 10px">  <el-input id="input_interview" v-model="basic_interviews" suffix-icon="el-icon-message" placeholder = "请输入房源介绍" clearable></el-input></el-col>
      </el-row>
      <el-row :gutter="25">
        <el-col :span="3" style="padding: 20px"><p>请输入房屋价格：</p></el-col>
        <el-col :span="6" style="padding: 10px;"><el-input id="input_price"   v-model="house_price" suffix-icon="el-icon-user" placeholder = "请输入房屋价格" clearable></el-input></el-col>
      </el-row>
      <el-row :gutter="25">
        <el-col :span="3" style="padding: 20px;"><p>请输入房屋住址：</p></el-col>
        <el-col :span="6" style="padding: 10px;"> <el-input id="input_address"   v-model="house_position" suffix-icon="el-icon-place" placeholder = "请输入房屋住址" clearable></el-input></el-col>
      </el-row>
      <el-row :gutter="25">
        <el-col :span="3" style="padding: 20px"><p>请输入联系手机号：</p></el-col>
        <el-col :span="6" style="padding: 10px;"> <el-input id="input_phone"   v-model="connect_phone" suffix-icon="el-icon-phone" placeholder = "请输入联系手机号" clearable></el-input></el-col>
      </el-row>
      <el-row :gutter="25">
        <el-col :span="3" style="padding: 20px"><p>请输入业主姓名：</p></el-col>
        <el-col :span="6" style="padding: 10px"><el-input id="input_name"  v-model="renter_name" suffix-icon="el-icon-female" placeholder = "请输入业主姓名" clearable></el-input></el-col>
      </el-row>
      <el-tag type="warning">提示:房源名称不可修改</el-tag>
      <el-button type="primary"  id="post_add" @click="putModify">确认更改</el-button>
    </el-dialog>

  </div>
</template>

<script>
    import Navbar from "../tools/Navbar";

    export default {
        name: "HouseManage",
      //绑定参数
      data(){
          return{
            tableData: [{
              house_title: '王小虎',
              house_images:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
              basic_interviews:'春暖怀开的佳佳基大声说撒所撒所所付所',
              house_price : 11,
              house_position:'中国长沙',
              connect_phone:'135234565441',
              renter_name:'张学友'
            },
            ],

            //对话显示
            dialogTableVisible:false,
            //dialog 数据
            house_title:'科学大道口',
            house_images:'',
            basic_interviews:'还不错',
            house_price:11,
            house_position:'sss',
            connect_phone:'15555555',
            renter_name:'古天乐',

            //添加图片框
            fileList:[{name:'',url:''}],
          }
      },
      //@brief:相关组件引入
       components:{
          VNavbar:Navbar,
       },
       //@brief:HTML加载前方法引入：
      created() {

      },
      //@brief:HTML加载后方法引入：
      mounted() {
          let that = this;
          let cur_headers = {'Authorization':"JWT " + localStorage.getItem('token')};
          this.$axios({
            url:'api/allhouses/',
            method:'get',
            headers:cur_headers,
          }).then(
            function (res) {
              console.log(res.data);
              let cur_count = res.data['count'];
              if (cur_count < 1)
              {
                return;
              }
              let i = 0;
              for (;i<cur_count; i++)
              {
                let str_house_images = res.data['results'][i]['house_images'];
                let str_house_title = res.data['results'][i]['house_title'];
                let str_basic_interviews = res.data['results'][i]['basic_interviews'];
                let str_house_price = res.data['results'][i]['house_price'];
                let str_house_position = res.data['results'][i]['house_position'];
                let str_connect_phone = res.data['results'][i]['connect_phone'];
                let str_renter_name = res.data['results'][i]['renter_name'];
                let push_data = {'house_images':str_house_images,
                                  'house_title':str_house_title,
                                  'basic_interviews':str_basic_interviews,
                                    'house_price':str_house_price,
                'house_position':str_house_position,'connect_phone':str_connect_phone,
                'renter_name':str_renter_name};
                that.tableData.unshift(push_data);
              }
              that.tableData.pop();
            }
          ).catch(
            function (res) {

            }
          );
      },
      //@brief：相关方法
      methods:{
        //编辑按钮
        handleEdit(index, row) {
          let that = this; //let作用域为方法内
          //
          this.house_title = this.tableData[index]['house_title'];
          this.house_images = this.tableData[index]['house_images'];
          this.basic_interviews = this.tableData[index]['basic_interviews'];
          this.house_price = this.tableData[index]['house_price'];
          this.house_position = this.tableData[index]['house_position'];          this.house_title = this.tableData[index]['house_title'];
          this.connect_phone = this.tableData[index]['connect_phone'];
          this.renter_name = this.tableData[index]['renter_name'];
          this.fileList.unshift({name:'1.png',url:this.house_images});
          this.fileList.pop();
          this.dialogTableVisible=true;
        },
        //删除按钮
        handleDelete(index, row) {
          console.log(index, row);
        },
        //@brief:批量删除按钮
        batchDelete(){

        },
        //@brief:修改更新方法
        putModify(){
          this.$refs.uploadhousephoto.submit();
        },
        //@brief:上传照片相关方法
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
          const isLt10M = file.size / 1024 / 1024 < 10; //大小小于10M
          if (!isIMAGE) {
            alert('只允许上传图片');
            return isIMAGE;
          }
          if (!isLt10M) {
            alert('上传房源大小需要小于5M');
            return isLt10M;
          }

          //进行上传的功能
          //添加token
          let params = new FormData();//创建form对象
          params.append('house_images',file);
          params.append('house_title',this.house_title); //房源名字
          params.append('basic_interviews',this.basic_interviews); //简单介绍
          params.append('house_price',this.house_price); //房源价格
          params.append('house_position',this.house_position); //房源位置
          params.append('connect_phone',this.connect_phone); //联系电话
          params.append('renter_name',this.renter_name); //房东
          let config = {
            headers:{'Content-Type':'multipart/form-data','Authorization':"JWT " + localStorage.getItem('token')}
          }; //添加请求头
          this.$http.put('api/allhouses/',params,config)
            .then(response=>{
              if(response.status == 200)
              {
                alert("上传成功！");
                console.log(response.data);
              }
              else if(response.status == 201){
                alert("添加成功！");
                console.log(response.data);
              }
            });
          return isIMAGE && isLt1M;
        },
        //上传成功
        onSuccessUpload(response,file,fileList){
          //上传成功处理事件
        },
      },
    }
</script>

<style scoped>

</style>
