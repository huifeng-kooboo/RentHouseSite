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
      mounted(){
          let that = this;
        //先判断是否已经登录 已登录则跳转到主页 并提示用户
        let token_data = localStorage.getItem('token');
        //先判断是否有token 有的话 先尝试用token进行登录
        if (token_data == null)
        {
          //为空，则说明未登录 允许登录
          return;
        }
        //不为空时，判断是否过期
        //token存在 请求获取用户信息及权限
        let json_token = {'token':token_data};
        this.$axios(
          {
            //url:'api/anatoken/', //修改到生产模式
            url:'http://49.234.6.143:8000/api/anatoken/',
            method: 'post',
            data:JSON.stringify(json_token),
          }
        ).then(
          function (res) {
            let permission = res.data['permission'];
            console.log(permission);
            if(permission == "admin")
            {
              alert("您已登录,如需重新登录，请在个人中心--》注销后再次登录即可");
              window.location.href='/main';//调回主页
            }
            else if(permission == "visitor")
            {
              return;
            }
            else{
              alert("您已登录,如需重新登录，请在个人中心--》注销后再次登录即可");
              window.location.href='/main';//调回主页
            }
          }
        );
      },
      methods:{
          /*
          * @brief: 发送登录请求到服务器
          */
          sendLoginPost(){
            const that = this; //解决无法跳转的问题
            //设置规则 用户名和密码大小不能小于6
            //先判断是否有token 有的话 先尝试用token进行登录
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
                  url:'http://49.234.6.143:8080/api/gettoken/',
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

              this.$axios(
                {
                  url:"http://49.234.6.143:8080/api/login/", //请求的url 由于跨域
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
