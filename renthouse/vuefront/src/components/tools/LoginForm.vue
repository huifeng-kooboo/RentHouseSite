<template>
    <div id="div_login_form">
      <!--通用登录表单模板-->
      <!-- v_model: 双向绑定，确实很酷-->
      <el-input class="username" v-model="input_username" placeholder = "请输入用户名"></el-input>
      <el-input class="password" v-model="input_password" placeholder="请输入密码" show-password></el-input>
      <el-button type="primary" class="btn_login" icon="el-icon-user">登录</el-button>
    </div>
</template>

<script>
    export default {
        name: "LoginForm",
      data(){
          return{
            input_username:'',
            input_password:'',
          }
      }
    }
</script>

<style scoped>

</style>
