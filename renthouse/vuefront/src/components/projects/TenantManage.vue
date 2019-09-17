<template>
    <!--租户管理界面-->
  <div>
    <VNavbar></VNavbar>
    <el-row :gutter="30">
      <el-col :span="3">请选择租户名称：</el-col>
      <el-col :span="6">
        <el-select v-model="tenant" filterable placeholder="请选择租户名称：">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-col>
    </el-row>
    <!--租房时间-->
    <el-row :gutter="30">
      <el-col :span="3">租房时间：</el-col>
      <el-col :span="6">
        <el-date-picker
          v-model="rental_time"
          format="yyyy-MM-dd"
          value-format="yyyy-MM-dd"
          type="date"
          placeholder="选择日期">
        </el-date-picker>
      </el-col>
    </el-row>
    <!--租户地址-->
    <el-row :gutter="30">
      <el-col :span="3">租房地址：</el-col>
      <el-col :span="6">
        <el-input
          v-model="rental_address"
          placeholder="租房地址">
        </el-input>
      </el-col>
    </el-row>
    <!--房租价格-->
    <el-row :gutter="30">
      <el-col :span="3">房租价格：</el-col>
      <el-col :span="6">
        <el-input
          v-model="rent_fee"
          placeholder="房租价格">
        </el-input>
      </el-col>
    </el-row>
    <!--水费-->
    <el-row :gutter="30">
      <el-col :span="3">水费：</el-col>
      <el-col :span="6">
        <el-input
          v-model="water_fee"
          placeholder="水费">
        </el-input>
      </el-col>
    </el-row>
    <!--电费-->
    <el-row :gutter="30">
      <el-col :span="3">电费：</el-col>
      <el-col :span="6">
        <el-input
          v-model="electric_fee"
          placeholder="电费">
        </el-input>
      </el-col>
    </el-row>
    <!--是否有网费-->
    <el-row :gutter="30">
      <el-col :span="3">是否有网费：</el-col>
      <el-col :span="6">
        <el-switch
          v-model="is_net"
          active-color="#13ce66"
          inactive-color="#ff4949">
        </el-switch>
      </el-col>
    </el-row>
    <!--网费-->
    <el-row :gutter="30">
      <el-col :span="3">网费：</el-col>
      <el-col :span="6">
        <el-input
          v-model="net_fee"
          placeholder="网费">
        </el-input>
      </el-col>
    </el-row>
    <!--钥匙数量-->
    <el-row :gutter="30">
      <el-col :span="3">钥匙数量：</el-col>
      <el-col :span="6">
        <el-input
          v-model="key_num"
          placeholder="钥匙数量">
        </el-input>
      </el-col>
    </el-row>
    <!--是否有空调-->
    <el-row :gutter="30">
      <el-col :span="3">是否有空调：</el-col>
      <el-col :span="6">
        <el-switch
          v-model="is_air"
          active-color="#13ce66"
          inactive-color="#ff4949">
        </el-switch>
      </el-col>
    </el-row>
    <!--是否有洗衣机-->
    <el-row :gutter="30">
      <el-col :span="3">是否有洗衣机：</el-col>
      <el-col :span="6">
        <el-switch
          v-model="is_washer"
          active-color="#13ce66"
          inactive-color="#ff4949">
        </el-switch>
      </el-col>
    </el-row>
    <!--提交按钮-->
    <el-row :gutter="30">
      <el-button type="primary" @click="addpost">提交</el-button>
    </el-row>


  </div>

</template>

<script>
  import Navbar from '../tools/Navbar'
    export default {
        name: "TenantManage",
      components:{
          VNavbar:Navbar,
      },
        created(){},
        //
        //渲染数据
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
              url:'api/anatoken/',
              method: 'post',
              data:JSON.stringify(json_token),
            }
          ).then(
            function (res) {
              let permission = res.data['permission'];
              console.log(permission);
              if(permission == "admin")
              {
              }
              else if(permission == "visitor")
              {
                alert("您还没有登录，没有访问权限");
                window.location.href='/main';//调回主页
                return;
              }
              else{
                alert("您没有该访问权限");
                window.location.href='/main';//调回主页
              }
            }
          );

          this.$axios.get('api/briefuser/').then(function (response) {
                if (response.status == 200)
                {
                    console.log("数据为：");
                    let data_count =response.data['count'];
                    if (data_count < 1)
                    {
                        return false;
                    }
                    let i = 0;
                    for (;i< data_count; i++)
                    {
                        //console.log(response.data['results'][i]);
                        let add_vals = {'value':response.data['results'][i]['username'],'label':response.data['results'][i]['username']};
                        that.options.push(add_vals);
                    }
                    that.options.shift();//剔除第一个范例数据
                }
            }).catch();
        },
        //数据部分
        data(){
           return{
               options: [{
                   value: '',
                   label: ''
               }],
               tenant:'',
               rental_time:'',
               rental_address:'',
               rent_fee:'',
               water_fee:'',
               electric_fee:'',
               is_net:true,
               net_fee:'',
               key_num:'',
               is_air:true,
               is_washer:true,

           }
        },
      methods:{
          /*@brief：发送请求测试*/
        addpost(){
          //发送post请求去增加数据
            //请求url：'/api/addland'
            console.log(this.rental_time);
            let json_data = {'tenant':this.tenant,'rental_time':this.rental_time,
            'rental_address':this.rental_address,'rent_fee':this.rent_fee,
            'water_fee':this.water_fee,'electric_fee':this.electric_fee,
            'is_net':this.is_net,'net_fee':this.net_fee,
            'key_num':this.key_num,'is_air':this.is_air,
            'is_washer':this.is_washer};
            let cur_headers = {'Authorization':"JWT " + localStorage.getItem('token')};//添加请求头认证内容
            this.$axios(
                {
                    url:'api/addland/',
                    method:'post',
                    data:JSON.stringify(json_data),
                    headers:cur_headers,
                }
            ).then(
                function (response) {
                    //201表示创建
                    if (response.status == 201){
                        alert("租户设置成功！");
                    }
                    else
                    {
                        alert(response.data);
                    }
                }
            ).catch(function (response) {
                //弹出错误原因
                alert(response.data);
            });
        },
      },
    }
</script>

<style scoped>

</style>
