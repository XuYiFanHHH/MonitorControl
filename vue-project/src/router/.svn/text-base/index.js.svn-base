import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home/index.vue'
import page_1 from '@/components/page_1/index.vue'
import page_2 from '@/components/page_2/index.vue'
import page_3 from '@/components/page_3/index.vue'
import page_4 from '@/components/page_4/index.vue'
import header from '@/components/header/index.vue'

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
        path: '/page_1',
        name: 'page_1',
        component: page_1 // 页面一
      },{
        path: '/page_2',
        name: 'page_2',
        component: page_2 // 页面二
      },{
        path: '/page_3',
        name: 'page_3',
        component: page_3 // 页面三
      },{
        path: '/page_4',
        name: 'page_4',
        component: page_4 // 页面四
      }]
    }
  ]
})
