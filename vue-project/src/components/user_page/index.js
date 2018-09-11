// import editDialog from "../Dialog/index.vue"

export default {
  name: 'user_page',
  components: {
  },
  
  data () {
    return {
      changePwdDialogVisible: false,
      account:{
        username: null,
        password: null,
        newPassWord: null,
      },
    }
  },
  created() {
    let location = window.document.cookie.indexOf('username')
    if(location == -1)
    {
      this.$message({
        type: 'warning',
        message: '您还未登录'
      });
      this.$router.push({
        name: 'login',
        path:'/login',
        query: {
        }
      })
    }
  },
  methods: {
    changePwd(){
      this.axios({
        method: 'post',
        url: '/controller/changePwd',
        data: {
          username: this.account.username,
          password: this.account.password,
          newPassWord: this.account.newPassWord
        }
      })
      .then((res) => {
        console.log(res.data['msg'])
        if(res.data['error_num'] === 0)
        {
          this.$message({
            type: 'success',
            message: '密码修改成功'
          });
          this.changePwdDialogVisible = false
        }
        else if(res.data['error_num'] === 100)
        {
          this.$message({
            type: 'warning',
            message: '您还未登录,请重新登录'
          });
          this.$router.push({
            name: 'login',
            path:'/login',
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