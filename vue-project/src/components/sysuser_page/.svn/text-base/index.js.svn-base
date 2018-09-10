export default {
  name: 'page_1',
  data () {
    return {
      tableData: [{
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1517 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1519 弄'
      }, {
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1516 弄'
      }]
    }
  },
  created() {
    this.axios({
      method: 'post',
      url: '/NNC/rest/systemUser/system_user_page',
      data: {
       page: '1'
      }
    })
    .then((res) => {
      this.msg = res.data.data.list;
      console.log(this.msg);
    })
    .catch(err => {
      // console.log(err);
    })
  }
}