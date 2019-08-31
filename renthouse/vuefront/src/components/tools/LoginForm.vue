<template>
    <div id="div_login_form">
      <!--通用登录表单模板-->
      <!-- v_model: 双向绑定，确实很酷-->
      <div id="div_title_login">
        <h2 class="h_title_login">用户登录</h2>
      </div>
      <div id="div_input_username">
        <el-input id="username" class="username" v-model="input_username" suffix-icon="el-icon-user" placeholder = "请输入用户名" ></el-input>
      </div>
      <div id="div_input_password">
        <el-input  id="password" class="password" v-model="input_password" placeholder="请输入密码" show-password></el-input>
      </div>
      <div id="div_button_login">
        <el-button @click="sendLoginPost" type="primary" class="btn_login" icon="el-icon-user" style="" >登录</el-button>
      </div>
    </div>
</template>

<script>
     import Vue from 'vue'
    import axios from "axios"
    import $ from 'jquery'
   //  axios.defaults.withCredentials = true;//允许跨域

    export default {
        name: "LoginForm",
      data(){
          return{
            input_username:'', //此处可以设置 直接绑定到输入框
            input_password:'',
          }
      },
      methods:{
          /*
          * @brief: 发送登录请求到服务器
          * */
          sendLoginPost(){
            //设置规则 用户名和密码大小不能小于6
            //js中对字符串修改的规则如下
            if (this.input_username.length < 6)
            {
              alert("用户名输入过短,请重新输入");
            }
            else if (this.input_password.length < 6)
            {
              alert("密码过短，请重新输入");
            }
            else {
              alert("发起请求");
              var post_data = {"username":this.input_username,"password":this.input_password};
              this.$axios(
                {
                  url:"api/login/", //请求的url 由于跨域
                  method:'post',
                  data:JSON.stringify(post_data),
                }
              ).then(
                function (return_data) {
                  alert("返回成功");
                }
              )
            }
          }
      }
      // Vue 绑定按钮事件
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

.btn_login{
  display: block;
  margin: 0 auto;
  position: relative;
  top:60px;
}

.h_title_login{
  text-align: center;
  position: relative;
  top:10px;
}
</style>
