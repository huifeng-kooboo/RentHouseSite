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
           }
        }
    }
</script>

<style scoped>

</style>
