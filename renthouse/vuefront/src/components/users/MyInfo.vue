<template>
    <!--个人信息设置通用模板-->
  <div id="div_myinfo">
    <VNavbar></VNavbar>
    <!--头像 ：可更改-->
    <el-row :gutter="70">
      <el-col :span="3">
        个人头像：
      </el-col>
      <el-col :span="6">
        <!--circleUrl:测试头像url-->
        <el-avatar :size="70" :src="circleUrl"></el-avatar>
      </el-col>
    </el-row>

    <!--用户名：不可更改-->
    <el-row :gutter="70">
      <el-col :span="3">
        用户名：
      </el-col>
      <el-col :span="6">
        <!--circleUrl:测试头像url-->
        ytouch<!--测试用-->
      </el-col>
    </el-row>
    <!--用户住址：可更改-->
    <el-row :gutter="70">
      <el-col :span="3">
        用户住址：
      </el-col>
      <el-col :span="6">
        <el-input placeholder="个人地址" v-model="input_address"></el-input>
      </el-col>
    </el-row>
    <!--用户住址：可更改-->
    <el-row :gutter="70">
      <el-col :span="3">
        手机号：
      </el-col>
      <el-col :span="6">
        <el-input placeholder="个人手机号" v-model="input_phone"></el-input>
      </el-col>
    </el-row>
    <!--用户住址：可更改-->
    <el-row :gutter="70">
      <el-col :span="3">
        身份证：
      </el-col>
      <el-col :span="6">
        <el-input placeholder="身份证号" v-model="input_idcard"></el-input>
      </el-col>
    </el-row>
    <el-button type="primary">确认信息</el-button>

  </div>
</template>

<script>
  import Navbar from '../tools/Navbar'
    export default {
        name: "MyInfo",
        components: {
          VNavbar: Navbar,
        },
      data(){
          return{
            circleUrl:'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
            input_address :'广东省',
            input_phone:'1322222',
            input_idcard:'3501811111111',
          }
      }
    }
</script>

<style scoped>

</style>
