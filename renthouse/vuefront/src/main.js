// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import VueResource from 'vue-resource'
//import /index.html
/*导入element-ui库*/
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
/*导入jquery库*/
import $ from 'jquery'
Vue.use(router);
//注册ElementUI
Vue.use(ElementUI);
Vue.use($);

//设置axios的请求
Vue.prototype.$http = axios;
Vue.prototype.$axios = axios;
axios.defaults.headers.post['Content-Type'] = 'application/json'; /*解决跨域问题*/
Vue.config.productionTip = false;
Vue.use(VueResource);

/* eslint-disable no-new */
var app = new Vue({
  el: '#app', //对应的是index.html的id
  router,
  components: { App },
  template: '<App/>'
});
