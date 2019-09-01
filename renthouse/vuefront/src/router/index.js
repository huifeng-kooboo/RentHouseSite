/*
* @desciption: 主要是定义相关路由信息
* users:用户包：包括登录、注册、用户信息、修改密码、等界面
* common:公共包： 一些基础界面
* */

import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import ElementUI from 'element-ui'
import Login from "../components/users/Login"
import Register from "../components/users/Register"
//Vue.use(VueAxios,axios); //使用axios请求
Vue.use(ElementUI);
Vue.use(Router);

export default new Router({
  el: '#app',
  mode:'history', /*解决#问题*/
  /*定义相关路由*/
  routes: [
    {
      /*@description:主页*/
      path: '/',
      redirect:'/main', //添加重定向方法
    },
    {
      /*@description:登录界面*/
      path: '/login',
      name: 'Login',
      component:Login
    },
    {
      /*@description:注册界面*/
      path:'/register',
      name: 'Register',
      component:Register
    },
    {
      /*@description:主页功能*/
      path:'/main',
      name:'Main',
      component:Main
    }
  ]
})
