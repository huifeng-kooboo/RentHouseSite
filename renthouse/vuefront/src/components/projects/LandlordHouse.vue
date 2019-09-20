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

      <!--编辑数据对话框 ：租户名不允许修改，其余信息可修改-->
      <el-dialog title="租户信息修改" :visible.sync="dialogTableVisible">
        <!--修改自TenantManage.vue中的表单-->
        <el-row :gutter="30">
          <el-col :span="3">租户名：</el-col>
          <el-col :span="6">
            <el-input
              :disabled="true"
              v-model="tenant"
              placeholder="租户名">
            </el-input>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <!--租房时间-->
        <el-row :gutter="30">
          <el-col :span="3">租房时间：</el-col>
          <el-col :span="6">
            <el-date-picker
              v-model="rental_time"
              format="yyyy-MM-dd"
              value-format="yyyy-MM-dd"
              type="date"
              placeholder="选择日期">
            </el-date-picker>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <!--租户地址-->
        <el-row :gutter="30">
          <el-col :span="3">租房地址：</el-col>
          <el-col :span="6">
            <el-input
              v-model="rental_address"
              placeholder="租房地址">
            </el-input>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <!--房租价格-->
        <el-row :gutter="30">
          <el-col :span="3">房租价格：</el-col>
          <el-col :span="6">
            <el-input
              v-model="rent_fee"
              placeholder="房租价格">
            </el-input>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <!--水费-->
        <el-row :gutter="30">
          <el-col :span="3">水费：</el-col>
          <el-col :span="6">
            <el-input
              v-model="water_fee"
              placeholder="水费">
            </el-input>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <!--电费-->
        <el-row :gutter="30">
          <el-col :span="3">电费：</el-col>
          <el-col :span="6">
            <el-input
              v-model="electric_fee"
              placeholder="电费">
            </el-input>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <!--是否有网费-->
        <el-row :gutter="30">
          <el-col :span="3">是否有网费：</el-col>
          <el-col :span="6">
            <el-switch
              v-model="is_net"
              active-color="#13ce66"
              inactive-color="#ff4949">
            </el-switch>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <!--网费-->
        <el-row :gutter="30">
          <el-col :span="3">网费：</el-col>
          <el-col :span="6">
            <el-input
              v-model="net_fee"
              placeholder="网费">
            </el-input>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <!--钥匙数量-->
        <el-row :gutter="30">
          <el-col :span="3">钥匙数量：</el-col>
          <el-col :span="6">
            <el-input
              v-model="key_num"
              placeholder="钥匙数量">
            </el-input>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <!--是否有空调-->
        <el-row :gutter="30">
          <el-col :span="3">是否有空调：</el-col>
          <el-col :span="6">
            <el-switch
              v-model="is_air"
              active-color="#13ce66"
              inactive-color="#ff4949">
            </el-switch>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <!--是否有洗衣机-->
        <el-row :gutter="30">
          <el-col :span="3">是否有洗衣机：</el-col>
          <el-col :span="6">
            <el-switch
              v-model="is_washer"
              active-color="#13ce66"
              inactive-color="#ff4949">
            </el-switch>
          </el-col>
        </el-row>
        <el-divider></el-divider>
        <!--提交按钮-->
        <el-row :gutter="30">
          <el-button type="primary" @click="addpost">确认修改</el-button>
        </el-row>

      </el-dialog>

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
          //判断是否有权限访问


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
            window.location.href = "/main"; //没权限便不允许访问
          });
      },
      data() {
        return {
          //显示表单数据
          tableData: [{
            renter_name:'小黄',
            date: '2016-05-02',
            address: '上海市普陀区金沙江路 1518 弄',
            rent_fee:1999,
            electric_fee:12,
              water_fee:14,
              net_fee:20,
              key_num:1,
              air_num :true,
              washer_num:true,
          }],
          //编辑框数据
          dialogTableVisible:false,
          //编辑修改数据
          tenant:'12',
          rental_time:'2019-08-30', //时间格式'yyyy-mm-dd'
          rental_address:'香港',
          rent_fee:11,
          water_fee:122,
          electric_fee:21,
          is_net:true,
          net_fee:22,
          key_num:1,
          is_air:true,
          is_washer:true,

        }
      },
      methods: {
        handleEdit(index, row) {
            //处理编辑问题
          let cur_rentername =  this.tableData[index]['renter_name'];
          this.tenant = cur_rentername;
          this.rent_fee = this.tableData[index]['rent_fee'];
          this.water_fee = this.tableData[index]['water_fee'];
          this.net_fee = this.tableData[index]['net_fee'];
          this.electric_fee = this.tableData[index]['electric_fee'];
          this.key_num = this.tableData[index]['key_num'];
          this.rental_time = this.tableData[index]['date'];
          this.rental_address = this.tableData[index]['address'];
          this.is_air = this.tableData[index]['air_num'];
          this.is_washer = this.tableData[index]['washer_num'];
          this.is_net = true; //默认网费

          this.dialogTableVisible = true; //显示界面
          console.log(index, row);
        },
        handleDelete(index, row) {
            //处理删除问题
          let that = this;
          let json_data = {'tenant':that.tableData[index]['renter_name']};
          let cur_headers = {'Authorization':"JWT " + localStorage.getItem('token')};
          this.$axios(
            {
              url:'api/gettenantinfo/',
              method:'delete',
              data:json_data,
              headers:cur_headers,
            }
          ).then(
            function (res) {
              console.log(res.data);
            }
          ).catch(
            function (res) {
              //异常处理
            }
          );
          console.log(index, row);
          location.reload();//刷新页面
        },
        //addpost:提交修改方法
        addpost(){
          let that = this;
          let json_data = {'tenant':this.tenant,'rental_time':this.rental_time,
            'rental_address':this.rental_address,'rent_fee':this.rent_fee,
            'water_fee':this.water_fee,'electric_fee':this.electric_fee,
            'is_net':this.is_net,'net_fee':this.net_fee,
            'key_num':this.key_num,'is_air':this.is_air,
            'is_washer':this.is_washer};
          let cur_headers = {'Authorization':"JWT " + localStorage.getItem('token')};
          
          this.$axios(
            {
              url:'api/gettenantinfo/',
              method:'put',
              data:json_data,
              headers:cur_headers,
            }
          ).then(
            function (res) {
              console.log(res.data);
            }
          ).catch(
            function (res) {
              //异常处理
            }
          );
          
          alert("修改成功");
          this.dialogTableVisible = false;
          location.reload();//刷新页面
        }
      }
    }
</script>

<style scoped>

</style>
