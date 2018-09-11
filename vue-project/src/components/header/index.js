import globalData from "../../assets/global/globalData";

export default {
  name: 'header',
  data () {
    return {
      date: null
    }
  },
  created() {
  },
  methods: {
    clicklogin(){
      let location = window.document.cookie.indexOf('username')
      if(location != -1)
      {
        this.$message({
          type: 'info',
          message: '您已登录'
        }); 
      }
      else
      {
        this.$router.push({
          name: 'login',
          path:'/login',
          query: {
          }
        })
      }
    },
    clicklogout(){
      let location = window.document.cookie.indexOf('username')
      if(location != -1)
      {
        this.axios({
          method: 'post',
          url: '/controller/logout',
          data: {
          }
        })
        .then((res) => {
          this.$message({
            type: 'success',
            message: '退出登录成功'
          });
          this.$router.push({
            name: 'login',
            path:'/login',
            query: {
            }
          })
        })
        .catch(err => {
          console.log(err);
        });
      }
      else
      {
        this.$message({
          type: 'warning',
          message: '您还未登录'
        }); 
      }
    }
  }
}