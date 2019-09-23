<template>
  <!--费用清单List-->
    <div>
      <!--添加常规导航栏-->
      <VNavbar></VNavbar>
      <el-table
        :data="tableData"
        border
        style="width: 100%">
        <el-table-column
          prop="price_type"
          label="类型"
          width="180">
        </el-table-column>
        <el-table-column
          prop="price"
          label="价格(元)"
          width="180">
        </el-table-column>
      </el-table>

      <el-button type="primary" @click="payMoney">立即支付</el-button>
    </div>
</template>

<script>
  import Navbar from '../tools/Navbar'
    export default {
        name: "FeeList",
      components:{
          VNavbar:Navbar,
      },
      mounted(){
          //访问获取用户名信息：
        let cur_headers = {'Authorization':"JWT " + localStorage.getItem('token')};//
        let that = this;
        //先判断是否已经登录 已登录则跳转到主页 并提示用户
        let token_data = localStorage.getItem('token');
        //先判断是否有token 有的话 先尝试用token进行登录
        if (token_data == null)
        {
          //为空，则说明未登录 允许登录
          alert("该用户未登录，请先登录后再进行操作！");
          window.location.href = '/login';
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
            let str_username = res.data['username']; //获取用户名
            let fee_data = {'tenant':str_username};
            that.$axios(
              {
                url:'api/feelist/',
                method:'get',
                params:fee_data,
                headers:cur_headers
              }
            ).then(
              function (res) {
                let cur_Count = res.data['count'];
                if (cur_Count < 1)
                {
                  alert("当前缴费清单未出，请联系房东！");
                  window.location.href = '/main';//返回主页
                  return;
                }
                that.rent_fee = res.data['results'][0]['rent_fee'];
                let rent_fee_table = {'price_type':'月租','price':that.rent_fee};
                that.water_fee = res.data['results'][0]['water_fee'];
                let water_fee_table = {'price_type':'水费','price':that.water_fee};
                that.electric_fee = res.data['results'][0]['electric_fee'];
                let electric_fee_table = {'price_type':'电费','price':that.electric_fee};
                that.net_fee = res.data['results'][0]['net_fee'];
                let net_fee_table = {'price_type':'网费','price':that.net_fee};
                that.tableData.unshift(rent_fee_table);
                that.tableData.unshift(water_fee_table);
                that.tableData.unshift(electric_fee_table);
                that.tableData.unshift(net_fee_table);
                let all_fees = that.rent_fee + that.electric_fee + that.water_fee + that.net_fee; //总费用
                that.tableData.pop();
                that.tableData.push({'price_type':'总计','price':all_fees});
                console.log(res.data['results'][0]['rent_fee']);
                console.log(res.data['count']);
              }
            ).catch(function (res) {

            });
          }
        );
      },
      data(){
        return{
          //tableData:费用清单列表
          tableData: [{
            price_type:'合计',
            price:'0',
          }],
          rent_fee:0, //月租
          water_fee: 0, //水费
          electric_fee:0,//电费
          net_fee:0,//网费
        }
      },
      methods:{

          //付款
        payMoney(){
          alert("付款功能暂未开通 敬请期待");
        }
      }
    }
</script>

<style scoped>

</style>
