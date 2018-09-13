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
    // 登录函数
    userLogin(){
      this.axios({
        method: 'post',
        url: '/controller/login',
        data: {
          username: this.account.username,
          password: this.account.password,
        }
      })
      .then((res) => {
        if(res.data['error_num'] === 0)
        {
          this.$message({
            type: 'success',
            message: '登录成功'
          });
          globalData.basePageInfo.getIntoUserPage = true
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
            type: 'info',
            message: res.data['msg']
          });
        }
      })
      .catch(err => {
        console.log(err);
      });
    }
  }
}