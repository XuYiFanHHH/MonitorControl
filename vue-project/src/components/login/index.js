import globalData from "../../assets/global/globalData";
export default {
  name: 'login',
  components: {
  },
  
  data () {
    return {
        activeName: "systemUser",
        logining : false,
        account : {
            username:'',
            password:'',
        },
    }
  },
  created() {
  },
  methods: {
    sysUserLogin(){
      if(this.account.username == "admin" && this.account.password == "pass")
      {
        globalData.is_systemUser = true  
        this.$router.push({
          name: 'sysuser_page',
          path:'/sysuser_page',
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