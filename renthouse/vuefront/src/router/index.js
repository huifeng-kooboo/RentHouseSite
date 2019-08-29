import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from "../components/Login";
import ElementUI from 'element-ui'


Vue.use(ElementUI);
Vue.use(Router);

export default new Router({
  mode:'history',
  /*定义相关路由*/
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/login',/*登录界面*/
      name: 'Login',
      component: Login
    }
  ]
})
