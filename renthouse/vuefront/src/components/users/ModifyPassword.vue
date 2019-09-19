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
          <el-input v-model="input_newpsd" type="password" placeholder="请输入新密码"></el-input>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="3">
          请确认新密码：
        </el-col>
        <el-col :span="6">
          <el-input v-model="input_repsd" type="password" placeholder="请确认新密码"></el-input>
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
          if (this.input_newpsd != this.input_repsd)
          {
            this.$alert('密码错误，请重新输入!');
            return;
          }
          //绑定相关数据
          let verify_data = {'phone_number':this.input_phone,'password':this.input_newpsd,'verify_code':this.input_verify};
          this.$axios(
            {
              url:'api/modifypassword/',
              method:'post',
              data:JSON.stringify(verify_data),
            }
          ).then(function (res) {
            console.log(res.data);
          }).catch(
            function (res) {
              //异常处理
            }
          );
        },
      }
    }
</script>

<style scoped>

</style>
