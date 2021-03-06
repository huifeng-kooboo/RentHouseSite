/*
* @desciption: 主要是定义相关路由信息
* users:用户包：包括登录、注册、用户信息、修改密码、等界面
* common:公共包： 一些基础界面
* */

import Vue from 'vue'
import Router from 'vue-router'
import Main from '../components/Main'
import ElementUI from 'element-ui'
import Login from "../components/users/Login"
import Register from "../components/users/Register"
import AddHouse from "../components/projects/AddHouse";
import ModifyPassword from "../components/users/ModifyPassword";
import TenantManage from "../components/projects/TenantManage";
import FeeList from "../components/projects/FeeList";
import MyInfo from "../components/users/MyInfo";
import HouseDetail from "../components/projects/HouseDetail";
import LandlordHouse from "../components/projects/LandlordHouse";
import NewPromotion from "../components/projects/NewPromotion";
import HouseManage from "../components/projects/HouseManage";
import AdPhotoManage from "../components/projects/AdPhotoManage";
//Vue.use(VueAxios,axios); //使用axios请求
Vue.use(ElementUI);
Vue.use(Router);

export default new Router({
  el: '#app',
  mode:'history', /*解决#问题*/
  /*定义相关路由*/
  routes: [
    {
      /*@description:主页：自动跳转至Main*/
      path: '/',
      redirect:'/main', //添加重定向方法
    },
    {
      /*@description:登录界面*/
      path: '/login',//测试
      name: 'Login',
      component:Login,
      meta: { auth:true }
    },
    {
      /*@description:注册界面*/
      path:'/register',
      name: 'Register',
      component:Register,
      meta: { auth:true }
    },
    {
      /*@description:主页功能*/
      path:'/main',
      name:'Main',
      component:Main,
      meta: { auth:true }
    },
    {
      /*@brief: 添加房源信息界面*/
      path:'/addhouse',
      name:'AddHouse',
      component:AddHouse,
      meta: { auth:true }
    },
    {
      /*@brief:修改密码*/
      path:'/modifypassword',
      name:'ModifyPassword',
      component:ModifyPassword,
      meta: { auth:true }
    },
    {
      /*@brief:租户管理*/
      path:'/tenant',
      name:'TenantManage',
      component:TenantManage,
      meta: { auth:true }
    },
    {
      /*@brief:费用清单: tenant:表示租户姓名*/
      /*此处处理逻辑为绑定用户登陆信息*/
      path:'/feelist',
      name:'FeeList',
      component:FeeList,
      meta: { auth:true }
    },
    {
      /*@brief:个人信息设置*/
      path:'/myinfo',
      name:'MyInfo',
      component:MyInfo,
      meta: { auth:true }
    },
    {
      /*@brief:房源详情页:通过动态路由配置*/
      /*原因：因为房屋数量太多，没法筛选*/
      path:'/housedetail/:housetitle',
      name:'HouseDetail',
      component:HouseDetail,
      meta: { auth:true }
    },
    {
      path:'/allrenters',
      name:'LandlordHouse',
      component:LandlordHouse,
      meta: { auth:true }
    },
    {
      path:'/newpromotion',
      name:'NewPromotion',
      component:NewPromotion,
      meta: { auth:true }
    },
    {
      path:'/housemanage',
      name:'HouseManage',
      component:HouseManage,
      meta: { auth:true }
    },
    {
      path:'/adphoto',
      name:'AdPhotoManage',
      component:AdPhotoManage,
      meta: { auth:true }
    }
  ]
})
