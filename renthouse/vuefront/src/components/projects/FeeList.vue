<template>
  <!--费用清单List-->
    <div>
      <!--添加常规导航栏-->
      <VNavbar></VNavbar>
      <el-table
        :data="tableData"
        border
        style="width: 100%">
        <el-table-column
          prop="price_type"
          label="类型"
          width="180">
        </el-table-column>
        <el-table-column
          prop="price"
          label="价格"
          width="180">
        </el-table-column>
      </el-table>

      <el-button type="primary">立即支付</el-button>
    </div>
</template>

<script>
  import Navbar from '../tools/Navbar'
    export default {
        name: "FeeList",
      components:{
          VNavbar:Navbar,
      },
      data(){
        return{
          //tableData:费用清单列表
          tableData: [{
            price_type: '月租',
            price: '800元',
          }, {
            price_type: '电费',
            price: '80元',
          }, {
            price_type: '物业费',
            price: '90元',
          }, {
            price_type: '水费',
            price: '90元',
          }, {
            price_type: '网费',
            price: '90元',
          },{
            price_type:'合计',
            price:'10011元',
          }],

        }
      },
    }
</script>

<style scoped>

</style>
