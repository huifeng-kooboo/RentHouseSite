<template>
    <div>
      <!--添加导航栏-->
      <VNavbar></VNavbar>
      <!--修改模板-->
      <el-table
        :data="tableData"
        style="width: 100%">

        <!--租户名-->
        <el-table-column
          label="租户名"
          width="100">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.renter_name }}</span>
          </template>
        </el-table-column>

        <el-table-column
          label="入租时间"
          width="130">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.date }}</span>
          </template>
        </el-table-column>

        <el-table-column
          label="入租地址"
          width="220">
          <template slot-scope="scope">
            <!--el-popover:类似于地址-->
            <el-popover trigger="hover" placement="top">
              <p>住址: {{ scope.row.address }}</p>
              <div slot="reference" class="name-wrapper">
                <el-tag size="medium">{{ scope.row.address }}</el-tag>
              </div>
            </el-popover>
          </template>
        </el-table-column>

        <!--入租租金-->
        <el-table-column
          label="本月租金(元/月)"
          width="130">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.rent_fee }}</span>
          </template>
        </el-table-column>

        <!--电费-->
        <el-table-column
          label="电费(元/月)"
          width="130">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.electric_fee }}</span>
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

    </div>
</template>

<script>
    import Navbar from "../tools/Navbar";

    export default {
        name: "LandlordHouse",
      components:{
          VNavbar:Navbar,
      },
      mounted() {
          //这边发送请求获取数据
      }
      ,
      data() {
        return {
          tableData: [{
            renter_name:'小黄',
            date: '2016-05-02',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄',
            rent_fee:1999,
            electric_fee:12
          }, {
            renter_name:'小黄',
            date: '2016-05-04',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1517 弄',
            rent_fee: 20000,
            electric_fee:12
          }, {
            renter_name:'小黄',
            date: '2016-05-01',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1519 弄',
            rent_fee: 200,
            electric_fee:12
          }]
        }
      },
      methods: {
        handleEdit(index, row) {
          console.log(index, row);
        },
        handleDelete(index, row) {
          console.log(index, row);
        }
      }
    }
</script>

<style scoped>

</style>
