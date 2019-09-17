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
          */
          sendLoginPost(){
            const that = this; //解决无法跳转的问题
            //设置规则 用户名和密码大小不能小于6
            let cur_token = localStorage.getItem('token');
            //先判断是否有token 有的话 先尝试用token进行登录
            if (cur_token == null)
            {
              alert("token为空");
            }
           // localStorage.removeItem('token');
            //js中对字符串求长度的方法
            if (this.input_username.length < 6)
            {
              alert("用户名输入过短,请重新输入");
            }
            else if (this.input_password.length < 6)
            {
              alert("密码过短，请重新输入");
            }
            else {
              var post_data = {"username":this.input_username,"password":this.input_password};/*需要post的数据*/
              this.$axios(
                {
                  url:'api/gettoken/',
                  method:'post',
                  data:JSON.stringify(post_data),
                }
              ).then(
                function (res) {
                  if (res.status == 200)
                  {
                    localStorage.setItem('token',res.data.token); //保存前端的token
                  }
                }
              );

              //验证token
              let token_data = {'token':localStorage.getItem('token')};
              this.$axios(
                {
                  url:'api/anatoken/',
                  method:'post',
                  data:JSON.stringify(token_data),
                }
              ).then(
                function (res) {
                  if (res.status == 200)
                  {
                    localStorage.setItem('token',res.data.token); //保存前端的token
                  }
                }
              );

              this.$axios(
                {
                  url:"api/login/", //请求的url 由于跨域
                  method:'post',
                  data:JSON.stringify(post_data),
                }
              ).then(
                function (return_data) {
                  /*当返回成功时，先判断状态码是否正确,信息解析*/
                  if (return_data.status == 200){
                    //跳转url，并传递数据
                    console.log(return_data.data.username);
                    that.$router.push({name:'Main',params:return_data.data});
                    // that.$router.push({name:'Main',params:return_data.data})---》处理跳转的一种方式
                    // that.$router.push({path:''}) //不传参清理方式
                  }
                }
              ).catch(
                function (res) {
                  //处理请求以长
                  if (res.response.status == 400)
                  {
                    alert(res.response.data); //弹出错误信息
                  }
                  else {
                    alert("当前网络异常！");
                  }
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
