<template>
  <el-row id="user_page" style="height: 100%">
    <el-row>
			<el-button type="primary" @click="changePwdDialogVisible = true">修改密码</el-button>
		</el-row>
     <el-form :model="form">
      <el-row>
        <el-col :span="2">
          <el-form-item label="左上点">
            <el-input v-model="bPoint0" placeholder=""></el-input>
            <el-input v-model="bPoint1" placeholder=""></el-input>
          </el-form-item>
      </el-col>   
        <el-col :span="2" :offset="1">
          <el-form-item label="右下点">       
            <el-input v-model="ePoint0" placeholder=""></el-input>
            <el-input v-model="ePoint1" placeholder=""></el-input>
          </el-form-item>
        <el-col :span="2">
          <el-button type="primary" @click="sendRect">提交</el-button>
        </el-col>
      </el-col>   
      </el-row>
    </el-form>
    <el-row id="user_page" style="height: 100%">
      <img alt src='http://127.0.0.1:8000/controller/send_image/'>
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

<script src="http://lib.sinaapp.com/js/jquery/1.9.1/jquery-1.9.1.min.js"></script>
<style src="./index.less" lang="less"></style>
<script src="./index.js"></script>