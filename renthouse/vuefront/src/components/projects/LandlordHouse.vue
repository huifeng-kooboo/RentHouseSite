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
          width="130">
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
          width="100">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.rent_fee }}</span>
          </template>
        </el-table-column>

        <!--电费-->
        <el-table-column
          label="电费(元/月)"
          width="100">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.electric_fee }}</span>
          </template>
        </el-table-column>

        <!--水费-->
        <el-table-column
          label="水费(元/月)"
          width="100">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.water_fee }}</span>
          </template>
        </el-table-column>

        <!--网费-->
        <el-table-column
          label="网费(元/月)"
          width="100">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.net_fee }}</span>
          </template>
        </el-table-column>

        <!--钥匙数量-->
        <el-table-column
          label="钥匙数量"
          width="100">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.key_num }}</span>
          </template>
        </el-table-column>

        <!--是否有空调-->
        <el-table-column
          label="是否有空调"
          width="100">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.air_num }}</span>
          </template>
        </el-table-column>

        <!--是否有洗衣机-->
        <el-table-column
          label="是否有洗衣机"
          width="100">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.washer_num }}</span>
          </template>
        </el-table-column>

        <!--编辑功能对应修改 删除功能向后端发起delete请求即可-->
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
          let cur_headers = {'Authorization':"JWT " + localStorage.getItem('token')};//
          let that = this;
          this.$axios({
              url:'api/allrenters/',
              method:'get',
              headers:cur_headers //添加token认证千万不能忘
          }).then(function (res) {
              //console.log(res.data);
              let cur_count = res.data['count'];
              if (cur_count < 1)
              {
                  this.$alert('当前您未添加租户房源！');
                  return;
              }
              let i = 0;
              for (;i< cur_count;i++)
              {
                  let json_data = {'renter_name':res.data['results'][i]['tenant'],'date':res.data['results'][i]['rental_time'],
                  'address':res.data['results'][i]['rental_address'],'rent_fee':res.data['results'][i]['rent_fee'],
                  'electric_fee':res.data['results'][i]['electric_fee'],'water_fee':res.data['results'][i]['water_fee'],
                  'net_fee':res.data['results'][i]['net_fee'],'key_num':res.data['results'][i]['key_num'],
                  'air_num':res.data['results'][i]['is_air'],'washer_num':res.data['results'][i]['is_washer']};
                  that.tableData.unshift(json_data);
              }
              that.tableData.pop();
          }).catch(function (res) {
              //处理异常 不擅长
          });
      },
      data() {
        return {
          tableData: [{
            renter_name:'小黄',
            date: '2016-05-02',
            address: '上海市普陀区金沙江路 1518 弄',
            rent_fee:1999,
            electric_fee:12,
              water_fee:14,
              net_fee:20,
              key_num:1,
              air_num :1,
              washer_num:1,
          }]
        }
      },
      methods: {
        handleEdit(index, row) {
            //处理编辑问题
          console.log(index, row);
        },
        handleDelete(index, row) {
            //处理删除问题
          console.log(index, row);
        }
      }
    }
</script>

<style scoped>

</style>
