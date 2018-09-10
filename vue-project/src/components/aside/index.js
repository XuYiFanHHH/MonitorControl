import globalData from "../../assets/global/globalData";

export default {
  name: 'navBar',
  data () {
    return {
      activeItem: 0
    }
  },
  created() {
    if(this.$route.query.partnum == undefined) {
      this.$router.push({
        name: 'user_page',
        path:'/user_page',
        query: {
          partnum: this.activeItem
        }
      })
      globalData.user_logined = false
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