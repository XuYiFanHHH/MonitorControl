export default {
  //  时间戳转换
  timeFilter: (time,type) => {
    if(!time) {
      return '—';
    };
    time = new Date(time);
    let Y = time.getFullYear() + '-',
    M = (time.getMonth()+1 < 10 ? '0'+(time.getMonth()+1) : time.getMonth()+1) + '-',
    D = time.getDate()< 10 ? '0'+time.getDate() : time.getDate(),
    H = ' ' + (time.getHours()< 10 ? '0'+time.getHours() : time.getHours()),
    MM = ':' + (time.getMinutes()< 10 ? '0'+time.getMinutes() : time.getMinutes()),
    y = time.getFullYear(),
    m = (time.getMonth()+1 < 10 ? '0'+(time.getMonth()+1) : time.getMonth()+1);
    if(type=='yyyy-mm-dd') {
      time = Y+M+D;
    }
    else if(type=='yyyy-mm-dd/hh:mm') {
      time = Y+M+D+H+MM;
    }else if(type=='yyyy.mm.dd/hh:mm') {
      time = y+'年'+m+'月'+D+'日'+H+MM;
    };
    return time;
  },
}
