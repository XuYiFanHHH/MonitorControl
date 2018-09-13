import globalData from "../../assets/global/globalData";

export default {
  name: 'warning_history',
  components: {
  },
  
  data () {
    return {
      currentPage: 1,
      pages: 0,
      tableData: null,
    }
  },
  created() {
    this.refresh();
    globalData.basePageInfo.getIntoUserPage = true
  },
  methods: {
    handleCurrentChange(val) {
      this.currentPage = val
      this.axios({
        method: 'post',
        url: '/controller/get_onepage_warnings',
        data: {
         page: val,
        }
      })
      .then((res) => {
        this.tableData = res.data["list"]
      })
      .catch(err => {
        console.log(err);
      });
    },

    deleteData(index, row) {
      this.axios({
        method: 'post',
        url: '/controller/delete_warning',
        data: {
         id: row.id,
        }
      })
      .then((res) => {
        this.$message({
          message: '该警告已删除',
          type: 'success'
        });
        this.refresh()
      })
      .catch(err => {
        console.log(err);
      });
    },

    refresh() {    
      let location = window.document.cookie.indexOf('username') 
      if(location != -1) 
      {
        console.log("refresh warning page");
        this.axios({
          method: 'post',
          url: '/controller/get_onepage_warnings',
          data: {
           page: '1'
          }
        })
        .then((res) => {
          this.pages = res.data["pages"]
          this.tableData = res.data["list"]
        })
        .catch(err => {
          console.log(err);
        });
      }
      else{
        this.$message({
          type: 'warning',
          message: '您还未登录，不能浏览'
        }); 
        this.$router.push({
          name: 'login',
          path:'/login',
          query: {
          }
        })
      }
    }
  }
}