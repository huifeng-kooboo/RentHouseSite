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
      <el-button type="primary" class="btn_register" icon="el-icon-user" style="" v-on:click="postRegister()">注册</el-button>
    </div>

  </div>

</template>

<script>
    export default {
        name: "RegisterForm",
        data(){
        return{
          input_username:'ytouch78', //此处可以设置 直接绑定到输入框
          input_password:'1234567',
          input_phone_number:'13824464121',
          input_rent_address:'dkalkdla',
          input_idcard:'350181199608271875',
        }
       },
      methods:{
          postRegister(){
            const that = this;
            var post_data = {"username":this.input_username,"password":this.input_password,"is_admin":false,"phone_number":this.input_phone_number,"rent_address":this.input_rent_address,"idcard":this.input_idcard};/*需要post的数据*/
            if (this.input_username.length < 6)
            {
              alert("用户名输入过短,请重新输入");
            }
            else if (this.input_password.length < 6)
            {
              alert("密码过短，请重新输入");
            }
            else if (this.input_idcard.length< 16)
            {
              alert("身份证号码过短，请重新输入");
            }
            else if (this.input_rent_address.length<4)
            {
              alert("住址有误，请重新输入");
            }
            else if (this.input_phone_number.length<11)
            {
              alert("手机号过短，请重新输入");
            }
            else {
             // var post_data = {"username":this.input_username,"password":this.input_password};/*需要post的数据*/
              this.$axios(
                {
                  url:"api/register/", //请求的url 由于跨域
                  method:'post',
                  data:JSON.stringify(post_data),
                }
              ).then(
                function (return_data) {
                  //注册成功返回201:状态码201 创建成功的请求
                  if (return_data.status == 201){
                    //跳转url，并传递数据：跳转到主页面，自动完成登录
                    alert("租户注册成功！");
                    that.$router.push({name:'Main',params:return_data.data}); //返回首页
                  }
                }
              ).catch(
                function (res) {
                  //处理请求失败的情况
                  if (res.response.status == 400)
                  {
                    if (res.response.data.username)
                    {
                      alert(res.response.data.username);
                    }
                    else if (res.response.data.password)
                    {
                      alert(res.response.data.password);
                    }
                    else if (res.response.data.phone_number){
                      alert(res.response.data.phone_number);
                    }
                    else if(res.response.data.rent_address)
                    {
                      alert(res.response.data.rent_address);
                    }
                    else {
                      alert(res.response.data.idcard);
                    }
                  }
                  else if(res.response.status == 500)
                  {
                    alert("服务器出错，请联系QQ:942840260");
                  }
                  else {
                    alert("当前网络异常！");
                  }
                }
              )
            }
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
