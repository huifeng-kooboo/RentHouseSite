<template>
    <!--添加房屋信息 展示给访客-->
  <div id="div_add_house">
    <!--主要为添加房源功能：针对于管理者，为项目特有，故放在projects模块-->
    <!--先放置常用导航栏模块-->
    <VNavbar></VNavbar>
    <h2>添加房源</h2>
    <ul>
    <!--列表渲染测试-->
    <li v-for="item in items">
      {{item.message}}
    </li>
    </ul>
  </div>
</template>

<script>
  import Navbar from '../tools/Navbar'
    export default {
        name: "AddHouse",
      data(){
          return{
            items:[
              {message:'foo'},
              {message:'fff'}
            ]
          }
      },
       components:{
         VNavbar:Navbar,
      },
      created() {
      },
      mounted() {
      },
      destroyed() {
      },
      methods:{
          //存放各种方法类
      }
    }
</script>

<style scoped>

</style>
