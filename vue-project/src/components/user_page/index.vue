<template>
  <el-row id="user_page" style="height: 100%">
    <el-row>
			<el-button type="primary" @click="changePwdDialogVisible = true">修改密码</el-button>
		</el-row>
    <el-dialog
				title="修改密码"
				:visible.sync="changePwdDialogVisible"
				width="30%"
				center>
      <el-form ref = "AccountForm" :model = "accont" class = "login-container" label-width="80px">

        <el-form-item  label = "账号">
          <el-input v-model = "account.username"  auto-complete = "off" placeholder = "请输入您的账号">
          </el-input>
        </el-form-item> 
        <el-form-item label = "原始密码">
          <el-input v-model = "account.password" auto-complete = "off" placeholder = "请输入旧密码">
          </el-input>
        </el-form-item>
        <el-form-item label = "新密码">
          <el-input v-model = "account.newPassWord" auto-complete = "off" placeholder = "请输入新密码">
          </el-input>
        </el-form-item>
        <el-form-item style = "width:100%;">
          <el-button type = "primary" style = "width:100%;" @click="changePwd">
            修改密码
          </el-button>
        </el-form-item>

      </el-form>
		</el-dialog>
	</el-row>
</template>
<style src="./index.less" lang="less"></style>
<script src="./index.js"></script>