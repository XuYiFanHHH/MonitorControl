<template>
  <el-row id="sysuser_page" style="height: 100%">
	  <el-col :span="24">
			<el-row>
				<el-button type="primary" @click="refresh">获取最新历史数据</el-button>
			</el-row>
			<br>
   	  <el-table
	      :data="tableData"
	      style="width: 100%">
	      <el-table-column
	        type="index"
	        label="序号"
	        width="80">
	      </el-table-column>
	      <el-table-column
	        prop="warningtype"
	        label="警告类型"
					width="250">
	      </el-table-column>
				<el-table-column
	        prop="warningcontent"
	        label="警告内容"
					width="250">
	      </el-table-column>
				<el-table-column
	        prop="warningtime"
	        label="警告时间"
					width="250">
	      </el-table-column>
				<el-table-column
		      label="删除"
					width="80">
					<template slot-scope="scope">
					<el-button
						round
						size="mini"
						type="primary"
						@click="deleteData(scope.$index, scope.row)">
						删除
					</el-button>
					</template>
		    </el-table-column>
	    </el-table>
			<br>
				<el-row>
					<el-pagination
						@current-change="handleCurrentChange"
						:current-page.sync="currentPage"
						layout="prev, pager, next, jumper"
						background="true"
						:page-count="pages">
					</el-pagination>
				</el-row>
				<br>
	  </el-col>
	</el-row>
</template>
<style src="./index.less" lang="less"></style>
<script src="./index.js"></script>