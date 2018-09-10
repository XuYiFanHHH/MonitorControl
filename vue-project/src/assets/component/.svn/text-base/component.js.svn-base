import Vue from 'vue'
import '!vue-style-loader!css-loader!less-loader!./component.less'
// 加载页面
Vue.component( 'loadPage-template', {  
  template: '',  
});

// 分页
Vue.component( 'pagination-template', {
  template: `<div id="pagination" v-if="pagination.pageTotal>1">
                <el-pagination background layout="pager" :page-size="pagination.pageSize" :page-count="pagination.pageTotal" :currentPage="pagination.pageNum" @current-change="pageReturn"></el-pagination>
                <div class="pageInput">
                  <el-input v-model.number="pageNUMGO" pattern="^[0-9]*[1-9][0-9]*$"></el-input>
                  <el-button type="primary" @click="changePage(pageNUMGO)">go</el-button>
                </div>
            </div>`,
  data() {
    return {
      pageNUMGO: ''
    }
  },
  props: ['pagination'],
  methods: {
  	pageReturn(num) {
  		this.$emit('paginationNum',num);
  	},
  	changePage(num) {
  		if(typeof(num)=='number') {
        if(this.pagination.pageTotal>=num) {
          this.$emit('paginationNum',num);
        }
        else {
          this.$emit('paginationNum',this.pagination.pageTotal);
        }
  		};
      this.pageNUMGO = '';
  	}
  }
});