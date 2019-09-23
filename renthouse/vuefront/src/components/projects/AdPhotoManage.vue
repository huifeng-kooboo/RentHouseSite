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
          }]
        }
      },
      mounted(){
       //
        let that = this;
        this.$axios(
          {
            url:'api/ads/',
            method:'get',
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
              that.tableData.unshift({'image_url':res.data['results'][i]['adphoto']});
            }
            that.tableData.pop();
          }
        ).catch();
      },
      methods:{
          //增加图片功能
        handleAdd(index, row) {
          console.log(index, row);
        },
        //删除图片按钮
        handleDelete(index, row) {
          console.log(index, row);
        },
      },
    }
</script>

<style scoped>

</style>
