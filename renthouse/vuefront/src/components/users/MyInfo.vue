<template>
    <!--个人信息设置通用模板-->
  <div id="div_myinfo">
    <VNavbar></VNavbar>

    <!--头像 ：可更改:后期功能做完再完善头像-->
    <el-row :gutter="70">
      <el-col :span="3">
        个人头像：
      </el-col>
      <el-col :span="6">
        <!--circleUrl:测试头像url-->
        <el-avatar :size="70" :src="circleUrl"></el-avatar>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <!--用户名：不可更改-->
    <el-row :gutter="70">
      <el-col :span="3">
        用户名：
      </el-col>
      <el-col :span="6">
        <!--circleUrl:测试头像url-->
        <el-tag>{{ input_username }}</el-tag>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <!--用户住址：可更改-->
    <el-row :gutter="70">
      <el-col :span="3">
        用户住址：
      </el-col>
      <el-col :span="6">
        <el-input placeholder="个人地址" v-model="input_address"></el-input>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <!--用户手机号：可更改-->
    <el-row :gutter="70">
      <el-col :span="3">
        手机号：
      </el-col>
      <el-col :span="6">
        <el-input placeholder="个人手机号" v-model="input_phone"></el-input>
      </el-col>
    </el-row>
    <el-divider></el-divider>
    <!-- 身份证：不可更改-->
    <el-row :gutter="70">
      <el-col :span="3">
        身份证：
      </el-col>
      <el-col :span="6">
        <el-input placeholder="身份证号" v-model="input_idcard" :disabled="true"></el-input>
      </el-col>
      <el-tag type="danger">tip:身份证号不可更改</el-tag>
    </el-row>
    <el-button type="primary" @click="confirmInfo">确认信息</el-button>

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
            input_username:'',
          }
      },
      //方法:
      methods:{
          //更新视图数据 用put方法 难！
        confirmInfo(){
          let  that = this;
            let curHeaders = {'Authorization':"JWT " + localStorage.getItem('token')};//
            let json_put_data = {'username':this.input_username,'rent_address':this.input_address,'phone_number':this.input_phone,
                'idcard':this.input_idcard};
            let address_data = {'rent_address':this.input_address};
            this.$axios(
                {
                    url:'api/myinfo/',
                    method:'put',
                    data:json_put_data,
                    headers:curHeaders,
                }
            ).then(function (res) {
                console.log(res.data);
               that.$alert('修改成功！');
            }).catch(function (res) {
                //此处为异常处理
            //更新视图信息 使用put方法
            });
        }

      },
      //前期准备
      mounted() {
        //步骤：
        //* 1.先判断TOKEN
        //* 2. 获取用户名 'api/anatoken'
        //* 3. 发送get请求到 'api/myinfo' 获取全部信息
        let that = this;
        let cur_token = localStorage.getItem('token');
        if (cur_token == null)
        {
          alert("请先登录!");
          window.location.href = '/login';
          return;
        }
        let token_data = {'token':cur_token};
         this.$axios(
          {
            url:'api/anatoken/',
            method: 'post',
            data:JSON.stringify(token_data),
          }
        ).then(
          function (res) {
            let str_username = res.data['username'];
            let get_data = {'username':str_username};
            let token_datas = {'Authorization':"JWT " + localStorage.getItem('token')};//
            that.$axios(
              {
                url:'api/myinfo/',
                method:'get',
                params:get_data,
                headers:token_datas
              }).then(
                function (res) {
                  console.log(res.data);
                  that.input_idcard = res.data['results'][0]['idcard'];
                  that.input_address = res.data['results'][0]['rent_address'];
                  that.input_phone = res.data['results'][0]['phone_number'];
                  that.input_username = res.data['results'][0]['username'];
                }
            )
          }
        ).catch(
          function (res) {
          }
        );
      }
    }
</script>

<style scoped>

</style>
