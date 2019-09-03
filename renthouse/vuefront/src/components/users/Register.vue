<template>
  <div id="div_register">
    <!-- 引入注册导航栏，后面注册成功后替换常规导航栏-->
    <VNavbar link_title="租户注册" link_address="/register"></VNavbar>
    <VRegisterForm></VRegisterForm>
  </div>

</template>

<script>
  import LoginNavbar from '../tools/LoginNavbar'
  import RegisterForm from '../tools/RegisterForm'
  import $ from 'jquery'
    export default {
        name: "Register",
        components:{
        VNavbar:LoginNavbar,
        VRegisterForm:RegisterForm,
      },
      created() {
          //进行请求数据
      }
    }
    // var example1 = new Vue({
    //   el: '#example-1',
    //   data: {
    //     items: [
    //       { message: 'Foo' },
    //       { message: 'Bar' }
    //     ]
    //   }
    // })
</script>

<style scoped>

</style>
