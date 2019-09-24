<template>
    <!--主页投放广告功能：可以增加图片或者删除图片功能-->
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

        <!--id-->
        <el-table-column
          label="id"
          width="100">
          <template slot-scope="scope">
            <el-tag type="primary">{{ scope.row.id }} </el-tag>
          </template>
        </el-table-column>

        <!--房屋图片-->
        <el-table-column
          label="广告图片"
          width="400">
          <template slot-scope="scope">
            <el-image
              style="width: 100px; height: 100px"
              :src="scope.row.image_url"
              :fit="fit"></el-image>
          </template>
        </el-table-column>

        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              size="mini"
              @click="handleAdd(scope.$index, scope.row)">增加</el-button>
            <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>

      <!--添加上传文件对话框-->
      <el-dialog title="添加广告图片" style="font-size: 12px;" :visible.sync="dialogTableVisible">

        <!--上传图片框-->
        <el-upload
          class="upload-demo"
          :file-list="fileList"
          action="/api/addphoto/"
          :auto-upload="false"
          accept="image/jpeg,image/gif,image/png"
          :before-upload="onBeforeUpload"
          ref = "uploadadphoto"
          :limit="1"
          list-type="picture">
          <el-button size="small" type="primary">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过10M,单次只能传1张</div>
        </el-upload>
        <el-divider></el-divider>
        <el-button type="primary" @click="uploadConfirm" >确认上传</el-button>
      </el-dialog>

    </div>
</template>

<script>
  import Navbar from '../tools/Navbar'
    export default {
        name: "AdPhotoManage",
      components:{
           VNavbar:Navbar,
      },
      data(){
        return{
          tableData: [{
            image_url:'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
            id:0,
          }],
          dialogTableVisible:false,//默认为隐藏状态
          fileList: [],
        }
      },
      mounted(){
       //
        let that = this;
        let cur_headers = {'Authorization':"JWT " + localStorage.getItem('token')};
        this.$axios(
          {
            url:'api/ads/',
            method:'get',
            headers:cur_headers,
          }
        ).then(
          //返回数据处理
          function (res) {
            let cur_count = res.data['count'];
            if (cur_count < 1)
            {
              that.tableData.pop();
              return;
            }
            let i = 0;
            for(;i<cur_count;i++)
            {
              that.tableData.unshift({'image_url':res.data['results'][i]['adphoto'],'id':res.data['results'][i]['id']});
            }
            that.tableData.pop();
          }
        ).catch();
      },
      methods:{
          //@brief:增加图片功能
        handleAdd(index, row) {
          //使用post方法
          this.dialogTableVisible = true;
        },
        //@brief:删除图片按钮
        handleDelete(index, row) {
          console.log(index, row);
          let delete_data = {'id':this.tableData[index]['id']};
          this.$axios(
            {
              url:'api/ads/',
              method:'delete',
              data:delete_data,
            }
          ).then(function (res) {
            window.location.reload(); //删除之后重新更新即可
          }).catch(function (res) {

          });
        },

        onBeforeUpload(file){
          let params = new FormData();//创建form对象
          params.append('image_url',file);
          console.log(file);
          let config = {
            headers:{'Content-Type':'multipart/form-data','Authorization':"JWT " + localStorage.getItem('token')}
          }; //添加请求头
          this.$axios(
            {
              url:'api/ads/',
              method:'put',
              data:params,
              headers:{'Content-Type':'multipart/form-data','Authorization':"JWT " + localStorage.getItem('token')},
            }
          ).then(
            function (res) {
              alert('添加成功');
              window.location.reload();
            }
          ).catch(
            function (res) {
              alert('添加失败');
            }
          );
        },
        uploadConfirm(){
          //上传
          this.$refs.uploadadphoto.submit();
        }
      },
    }
</script>

<style scoped>

</style>
