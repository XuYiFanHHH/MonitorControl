<template>
  <el-row :gutter="20" id="header">
    <el-col class="left_header" :span="20">
      <img alt src="../../../res/ncclogo.png" 
        width="36" 
        height="36" 
        class="ncc_logo">
    </el-col>
    <el-col class="right_header" :span="4">
      <el-row>
        <el-button type="primary" @click="clicklogin">登录</el-button>
        <el-button type="success" @click="click_logout">注销</el-button>
      </el-row>
    </el-col>
  </el-row>
</template>
<style src="./index.less" lang="less"></style>
<script src="./index.js"></script>