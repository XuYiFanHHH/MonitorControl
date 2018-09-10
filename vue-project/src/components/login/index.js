import globalData from "../../assets/global/globalData";
export default {
  name: 'login',
  components: {
  },
  
  data () {
    return {
        activeName: "user",
        account : {
            username:'',
            password:'',
        },
    }
  },
  created() {
  },
  methods: {
    userLogin(){
      if(this.account.username == "admin" && this.account.password == "pass")
      {
        globalData.user_logined = true  
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
          message: '账号密码错误'
        });
      }
    }
  }
}