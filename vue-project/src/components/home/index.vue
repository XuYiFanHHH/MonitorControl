<template>
   <el-container id="home">
    <el-header>
      <headers>
      </headers>
    </el-header>  
    <el-container>
        <el-aside>
          <asideBar ref="asideBar"></asideBar>
        </el-aside>
        <el-main>
          <router-view id="routerInner"></router-view>
        </el-main>
      </el-container>
    </el-container>
</template>
<style src="./index.less" lang="less"></style>
<script src="./index.js"></script>