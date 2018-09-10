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
      if(globalData.is_systemUser)
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
    click_logout(){
      if(globalData.is_systemUser)
      {
        globalData.is_systemUser = false
        this.$message({
          type: 'info',
          message: '退出登录成功'
        }); 
        this.$router.push({
          name: 'user_page',
          path:'/user_page',
          query: {
          }
        })
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