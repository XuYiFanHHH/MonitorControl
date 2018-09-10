<template>
	<el-menu id="asideBar" :default-active="activeItem">
    <el-menu-item v-for="(data,index) in globalData.basePageInfo.asideList" :key="index" :index="index">
    	<router-link :to="{ path: data.link, query: { partnum: index } }">{{ data.item }}</router-link>
    </el-menu-item>
  </el-menu>
</template>
<style src="./index.less" lang="less"></style>
<script src="./index.js"></script>