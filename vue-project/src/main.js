import Vue from 'vue'
import App from './App'
import router from './router'

// 引入babel-polyfill
import 'babel-polyfill'
// 引入es6-promise
import promise from 'es6-promise'
promise.polyfill()
// 引入jquery
import $ from 'jquery'
// 引入axios
import axios from 'axios'
import VueAxios from 'vue-axios'
import Qs from 'qs'

Vue.prototype.Qs=Qs
let axios_instance = axios.create({
  baseURL: process.env.API,
  transformRequest: [function (data) {
    data = Qs.stringify(data);
    return data;
  }],
  transformResponse:[function (data) {
  	// 兼容IE
    if (!!window.ActiveXObject || "ActiveXObject" in window || navigator.userAgent.indexOf('MSIE')>=0) {
      data = JSON.parse(data)
    };
    return data;
  }],
  responseType: 'json',
  headers: {
    'Content-Type':'application/x-www-form-urlencoded'
  },
  timeout: 10000
})
axios_instance.interceptors.request.use(function(res) {
	// 发送请求
  return res;
}, function(err) {
})
axios_instance.interceptors.response.use(function(res) {
	// 收到响应
  return res;
}, function(err) {
})
Vue.use(VueAxios, axios_instance)
// 引入ELement
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)
// 引入font-awesome
import 'font-awesome/css/font-awesome.css'
// 全局组件
import component from './assets/component/component.js'
// 全局变量
import globalData from './assets/global/globalData.js'
Vue.prototype.globalData = globalData
// 全局方法
import globalFC from './assets/global/globalFC.js'
Vue.prototype.globalFC = globalFC
// 全局过滤器
import globalFilter from './assets/global/globalFilter.js'
for(let item in globalFilter) {
  Vue.filter(item, globalFilter[item])
}

// 取消vue所有的日志与警告
Vue.config.silent = true
// 阻止vue在启动时生成生产提示
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
