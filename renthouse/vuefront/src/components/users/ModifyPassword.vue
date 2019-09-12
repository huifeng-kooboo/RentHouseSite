<template>
  <!--主要用于忘记密码和修改密码 用一个模板： 原因：
  不能找回密码。
  -->
    <div id="div_modify">
      <VNavbar></VNavbar>
      <el-row :gutter="30">
        <el-col :span="3">
          请输入手机号：
        </el-col>
        <el-col :span="6">
          <el-input v-model="input_phone" placeholder="手机号"></el-input>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="3">
          请输入手机验证码：
        </el-col>
        <el-col :span="6">
          <el-input v-model="input_verify" placeholder="手机验证码"></el-input>
        </el-col>
        <el-col :span="6">
          <el-button @click="postVerify" type="primary">发送验证码</el-button>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="3">
          请输入新密码：
        </el-col>
        <el-col :span="6">
          <el-input v-model="input_newpsd" placeholder="请输入新密码"></el-input>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="3">
          请确认新密码：
        </el-col>
        <el-col :span="6">
          <el-input v-model="input_repsd" placeholder="请确认新密码"></el-input>
        </el-col>
      </el-row>
      <el-row>
        <el-button type="primary" @click="postModify">提交</el-button>
      </el-row>
    </div>
</template>

<script>
  import Navbar from '../tools/Navbar'
    export default {
        name: "ModifyPassword",
      components:{
          VNavbar:Navbar,
      },
      data(){
          return{
            input_phone:'',
            input_verify:'',
            input_newpsd:'',
            input_repsd:'',
          }
      },
      methods:{
          //@brief：手机发送验证码
        postVerify(){
          alert("发送验证码");
        },
        //@brief:提交新密码
        postModify(){
          alert("提交新密码");
        },
      }
    }
</script>

<style scoped>

</style>
