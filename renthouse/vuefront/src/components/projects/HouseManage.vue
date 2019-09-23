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
            }]
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
          //
      },
      //@brief：相关方法
      methods:{
        //编辑按钮
        handleEdit(index, row) {
          console.log(index, row);
        },
        //删除按钮
        handleDelete(index, row) {
          console.log(index, row);
        },
        //@brief:批量删除按钮
        batchDelete(){

        }
      },
    }
</script>

<style scoped>

</style>
