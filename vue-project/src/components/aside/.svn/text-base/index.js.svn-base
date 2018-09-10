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
        name: 'page_1',
        path:'/page_1',
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