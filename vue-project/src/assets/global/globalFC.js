export default {
  // url截取参数
  urlSubstring: (name) => {
    return decodeURIComponent((new RegExp('[?|&]'+name+'='+'([^&;]+?)(&|#|;|$)').exec(location.href)||[,''])[1].replace(/\+/g,'%20'))||null;
  },
  // 文件下载
	downFile: (response) => {  
    let fileDownload = require('js-file-download');
    let fileName = response.headers['content-disposition'].match(/filename(\S*)xls/)[0];
    fileName = decodeURI(fileName.substring(fileName.indexOf('=')+2));     
    try {
      let a = document.createElement('a');
      let blob = new Blob([response.data], {type: 'text/plain'});
      let url = window.URL.createObjectURL(blob);
      a.href = url;
      a.download = fileName;
      document.body.appendChild(a);
      a.click();
      setTimeout(function() {
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
      },500);        
    }
    catch(err) {
      fileDownload(response.data,fileName);
    }
	},
  // 数字千位符
  scientificNotation: (num)=> {
    num = num.toString();
    let b = num.substring(num.indexOf('.'));
    let a = num.substring(0,num.indexOf('.'));
    if(Number(a)<0) {
      a = '-' + Math.floor(Number(a.substring(1))).toLocaleString();
    }
    else {
      a = Math.floor(num).toLocaleString();
    };
    if(a.indexOf('.')>0) {
      a = num.substring(0,num.indexOf('.'));
    }
    else if(a=='.000') {
      a = '0';
    };
    return a.toString()+b;
  }
}
