import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home/index.vue'
import login from '@/components/login/index.vue'
import user_page from '@/components/user_page/index.vue'
import warning_history from '@/components/warning_history/index.vue'

Vue.use(Router)

export default new Router({
  // mode: 'history',
	base: '/vue-project',
  routes: [
    {
      path: '*',
      component: home
    },
    {
      path: '/',
      name: 'home',
      component: resolve => require(['@/components/home/index.vue'],resolve),
      children: [{
        path: '/login',
        name: 'login',
        component: login // 登录页面
      },{
        path: '/warning_history',
        name: 'warning_history',
        component: warning_history // 历史警告
      },{
        path: '/user_page',
        name: 'user_page',
        component: user_page // 普通用户页面
      }]
    }
  ]
})
