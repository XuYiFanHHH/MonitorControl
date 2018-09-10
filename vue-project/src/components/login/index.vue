<template>
	<div class = "login">
    <el-form ref = "AccountForm" :model = "accont" class = "login-container" label-width="40px">
		<!--tab标签-->
		<div class="tabsUser">
		<el-tabs v-model = "activeName" @tab-click = "handleClick" style = "height: 30px;font-size: 25px">
			<el-tab-pane label = "用户登录" name = "user">
				<el-form-item  label = "账号">
					<el-input v-model = "account.username"  auto-complete = "off" placeholder = "请输入您的账号" class = "form-control" >
					</el-input>
				</el-form-item> 
				<el-form-item label = "密码" class = "form-inline">
					<el-input v-model = "account.password" auto-complete = "off" placeholder = "请输入密码" class = "form-control" >
				</el-input>
				</el-form-item>
				<el-form-item style = "width:100%;">
					<el-button type = "primary" style = "width:100%;" @click="userLogin">
						登录
					</el-button>
				</el-form-item>
			</el-tab-pane>
		</el-tabs>
		</div>
    </el-form>
    </div>
</template>
<style src="./index.less" lang="less"></style>
<script src="./index.js"></script>
