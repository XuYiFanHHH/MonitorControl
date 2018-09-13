// import editDialog from "../Dialog/index.vue"

export default {
  name: 'user_page',
  components: {
  },
  
  data () {
    return {
      changePwdDialogVisible: false,
      websock: null,
      state: null,
      account:{
        username: null,
        password: null,
        newPassWord: null,
      },
    }
  },
  created() {
    this.long_polling()
    // this.axios({
    //   method: 'post',
    //   url: '/controller/websocket',
    //   responseType: 'stream',
    //   data: {
        
    //   }
    // })
    // .then((res) => {
    //   console.log(res.data)
    // })
    // .catch(err => {
    //   console.log(err);
    // });
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
    // this.initWebpack()
  },
  methods: {
    // initWebpack() {
    //   const wsurl = "ws://localhost:8000/controller/websocket"
    //   this.websock = new WebSocket(wsurl)
    //   this.websock.onopen = this.websocketOpen
    //   this.websock.onmessage = this.websocketMessage
    //   this.websock.onclose = this.websocketClose
    //   this.websock.onerror = this.websocketError
    // },

    // websocketOpen() {
    //   console.log("Websocket连接成功")
    // },

    // websocketMessage(res) {
    //   console.log(res)
    //   this.state = JSON.parse(res.data)
    // },

    // websocketClose() {
    //   console.log("Websocket关闭")
    // },

    // websocketError() {
    //   console.log("Websocket连接失败")
    // },

    long_polling() {
      console.log("hahaha")
      var getting = {

        url:'http://127.0.0.1:8000/controller/long_polling',

        dataType:'json',

        success:function(res) {

         console.log(res);

         $.ajax(getting); //关键在这里，回调函数内再次请求Ajax

        },        
        //当请求时间过长（默认为60秒），就再次调用ajax长轮询
        error:function(res){
        // $.ajax(getting);
        }
      }
      $.ajax(getting)
    },

    sendRect() {
      this.axios({
        method: 'post',
        url: '/controller/setRect/',
        data: {
          bPoint0: this.bPoint0,
          bPoint1: this.bPoint1,
          ePoint0: this.ePoint0,
          ePoint1: this.ePoint1,
        }
      })
      .then((res) => {
        console.log(this.bPoint0)
      })
      .catch(err => {
        console.log(err);
      });
    },

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