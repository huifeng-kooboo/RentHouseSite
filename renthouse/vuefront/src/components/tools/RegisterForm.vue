<template>
<!--注册表单通用模板-->
  <div id="div_register_form">
    <!--通用登录表单模板-->
    <!-- v_model: 双向绑定，确实很酷-->
    <div id="div_title_register">
      <h2 class="h_title_register">用户注册</h2>
    </div>
    <div id="div_input_username">
      <el-input class="username" v-model="input_username" suffix-icon="el-icon-user" placeholder = "请输入用户名" ></el-input>
    </div>
    <div id="div_input_password">
      <!--show-password 表示展示密码-->
      <el-input class="password" v-model="input_password" placeholder="请输入密码" show-password></el-input>
    </div>

    <div id="div_input_phone_number">
      <!-- 手机号输入框 -->
      <el-input class="phone_number" v-model="input_phone_number" placeholder="请输入手机号"></el-input>
    </div>

    <div id="div_input_rent_address">
      <!-- 住址输入框 -->
      <el-input class="rent_address" v-model="input_rent_address" placeholder="请输入住址"></el-input>
    </div>

    <div id="div_input_idcard">
      <!-- 身份证号输入框 -->
      <el-input class="idcard" v-model="input_idcard" placeholder="请输入身份证号"></el-input>
    </div>

    <div id="div_button_register">
      <el-button type="primary" class="btn_register" icon="el-icon-user" style="">注册</el-button>
    </div>

  </div>

</template>

<script>
    export default {
        name: "RegisterForm",
        data(){
        return{
          input_username:'', //此处可以设置 直接绑定到输入框
          input_password:'',
          input_phone_number:'',
          input_rent_address:'',
          input_idcard:'',
        }
       }
    }
</script>

<style scoped>
  .username{
    width:300px;
    display: block;
    margin: 0 auto;
    position: relative;
    top:20px;
  }

  .password {
    width:300px;
    display: block;
    margin: 0 auto;
    position: relative;
    top:40px;
  }

  .phone_number{
    width:300px;
    display: block;
    margin: 0 auto;
    position: relative;
    top:60px;
  }

  .rent_address{
    width:300px;
    display: block;
    margin: 0 auto;
    position: relative;
    top:80px;
  }

  .idcard{
    width:300px;
    display: block;
    margin: 0 auto;
    position: relative;
    top:100px;
  }

  .btn_register{
    display: block;
    margin: 0 auto;
    position: relative;
    top:120px;
  }

  .h_title_register{
    text-align: center;
    position: relative;
    top:10px;
  }
</style>
