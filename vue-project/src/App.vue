<template>
  <div id="app">
    <router-view/>
    <!-- 加载等待 -->
    <i id="pageLoading" class="el-icon-loading"></i>
  </div>
</template>
<style src="./main.less" lang="less"></style>
<script>
export default {
  name: 'App'
}
</script>
