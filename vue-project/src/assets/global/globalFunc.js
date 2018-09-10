export default {
    name: 'axiosModel',
    aixosModel: function(self, url, params, info) {
        console.log("axiosModel params",params);
        self.axios({
        method: 'post',
        url: url,
        params: params
        })
        .then((res) => {
        if(res.status === 200) {
            console.log(res);
            self.$message({
            type: 'success',
            message: `${info}成功!`
            });
        }
        else {
            self.$message({
            type: 'danger',
            message: `${info}失败!`
            });
        }
        })
        .catch(err => {
        console.log(err);
        });
    }
}