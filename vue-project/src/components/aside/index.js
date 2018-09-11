import globalData from "../../assets/global/globalData";

export default {
  name: 'navBar',
  data () {
    return {
      activeItem: 0
    }
  },
  created() {
    console.log('create')
    let location = window.document.cookie.indexOf('username')
    if(location == -1)
    {
      this.$router.push({
        name: 'login',
        path:'/login',
        query: {
          partnum: this.activeItem
        }
      })
    }
    else
    {
      this.$router.push({
        name: 'user_page',
        path:'/user_page',
        query: {
          partnum: this.activeItem
        }
      })
    }
  },
  watch: {
    $route() {
      if(this.$route.query.partnum != undefined) {
        this.activeItem = Number(this.$route.query.partnum);
      }
    }
  }
}