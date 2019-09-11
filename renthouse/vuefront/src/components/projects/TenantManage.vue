<template>
    <!--租户管理界面-->
  <div>
    <h1>租户管理</h1>
    <el-row :gutter="30">
      <el-col :span="3">请选择租户名称：</el-col>
      <el-col :span="6">
        <el-select v-model="value" filterable placeholder="请选择租户名称：">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-col>
    </el-row>
    <!--租房时间-->
    <el-row :gutter="30">
      <el-col :span="3">租房时间：</el-col>
      <el-col :span="6">
        <el-date-picker
          v-model="rent_date_value"
          type="date"
          placeholder="选择日期">
        </el-date-picker>
      </el-col>
    </el-row>
    <!--租户地址-->
    <el-row :gutter="30">
      <el-col :span="3">租房地址：</el-col>
      <el-col :span="6">
        <el-input
          v-model="rent_address_value"
          placeholder="租房地址">
        </el-input>
      </el-col>
    </el-row>
    <!--房租价格-->
    <el-row :gutter="30">
      <el-col :span="3">房租价格：</el-col>
      <el-col :span="6">
        <el-input
          v-model="rent_price"
          placeholder="房租价格">
        </el-input>
      </el-col>
    </el-row>
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
    <!--提交按钮-->
    <el-row :gutter="30">
      <el-button type="primary">提交</el-button>
    </el-row>


  </div>

</template>

<script>
    export default {
        name: "TenantManage",
        data(){
           return{
               options: [{
                   value: '选项1',
                   label: '黄金糕'
               }, {
                   value: '选项2',
                   label: '双皮奶'
               }, {
                   value: '选项3',
                   label: '蚵仔煎'
               }, {
                   value: '选项4',
                   label: '龙须面'
               }, {
                   value: '选项5',
                   label: '北京烤鸭'
               }],
               value:'',
               rent_date_value:'',
               rent_address_value:'',
               rent_price:'',
               water_fee:'',
               electric_fee:'',
               is_net:true,
               net_fee:'',
               key_num:'',
               is_air:true,
               is_washer:true,

           }
        }
    }
</script>

<style scoped>

</style>
