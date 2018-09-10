# vue-cli构建项目（vue-project简洁版）

> 1. 应用技术：webpack、yarn、vue-cli、jQuery、axios、less、font-awesome

> 2. 兼容性：![](https://sfault-image.b0.upaiyun.com/135/366/1353660446-586b059433d7c)

> 3. node下载地址：[https://nodejs.org/en/download/](https://nodejs.org/en/download/)

> 4. 修改npm默认配置路径：[https://blog.csdn.net/wkkyo/article/details/52799488](https://blog.csdn.net/wkkyo/article/details/52799488)

> 5. npm换源：[https://www.jianshu.com/p/0deb70e6f395](https://www.jianshu.com/p/0deb70e6f395)

> 6. 安装yarn、vue-cli：[https://www.jianshu.com/p/9308e6abbe44](https://www.jianshu.com/p/9308e6abbe44) 

> 7. vue-cli构建项目：[https://www.jianshu.com/p/2769efeaa10a](https://www.jianshu.com/p/2769efeaa10a)

## 1、建立项目

### 下载依赖
yarn install

### 启动服务
yarn start

## 2、打包项目

### 打包
yarn run build

### 打包项目并查看分析报告
yarn run build --report

## 3、项目目录
### 具体页面在src/components中
1. 初始页面：HelloWorld

##### 需添加依赖
1. 引入jQuery

		文档地址：https://www.npmjs.com/package/jquery
		（1）yarn add jquery
		（2）/build/webpack.base.conf.js中添加：
			var webpack = require("webpack")
			module.exports中添加：
			plugins: [
				new webpack.optimize.CommonsChunkPlugin('common.js'),
				new webpack.ProvidePlugin({
					jQuery: "jquery",
					$: "jquery"
				})
			]
		引入：/src/main.js中：
		import $ from 'jquery'	
 
2. 引入font-awesome

		文档地址：http://www.fontawesome.com.cn/
		yarn add font-awesome
		引入：/src/main.js中：
		import 'font-awesome/css/font-awesome.css'

3. 添加Less

		文档地址：http://lesscss.cn/
		yarn add less less-loader
		/build/webpack.base.conf.js的rules中添加：
		{
			test: /\.less$/,
			loader: "style-loader!css-loader!less-loader",
		},
		使用：<style src="路径" lang="less"></style>

4. 引入axios

		文档地址：https://www.kancloud.cn/yunye/axios/234845
		yarn add axios
		yarn add vue-axios
		引入：/src/main.js中：
		import axios from 'axios'
		import VueAxios from 'vue-axios'
		import Qs from 'qs'
		Vue.prototype.Qs=Qs
		...
		Vue.use(VueAxios, axios_instance)

5. 引入babel-polyfill

		文档地址：https://www.babeljs.cn/docs/usage/polyfill/
		yarn add babel-polyfill
		a. /build/webpack.base.conf.js的module.exports中entry改为：
		entry: ["babel-polyfill", "./src/main.js"],
		b. /src/main.js中引入：
		import 'babel-polyfill'

6. 引入es6-promise

		文档地址：https://www.npmjs.com/package/es6-promise
		yarn add es6-promise
		引入：/src/main.js中：
		import promise from 'es6-promise'
		promise.polyfill()

###### 注：引入babel-polyfill、es6-promise目的是解决axios、promise在ie下的兼容性

##### VUE-CLI配置
1. 防止打包后tomcat、nginx、node、apache等服务器中刷新出现404

		/src/router/index.js中：
		export default new Router({
			mode: 'history', （注掉此句，改为：// mode: 'history'）
		})

2. 打包后项目文件夹名

		/src/router/index.js中：
		export default new Router({
			base: '/vue-project', （在new Router中添加此句）
		})

3. 解决打包后原assest、static文件夹中各种文件、图片等路径错误问题
		
		/build/webpack.prod.conf.js中：
		output: {
    		publicPath: './', （在output中添加此句）
		}

		/build/utils.js中：
	    return ExtractTextPlugin.extract({
	        use: loaders,
	        fallback: 'vue-style-loader',
	        publicPath: '../../' （在ExtractTextPlugin.extract中添加此句）
	    })

4. 解决font-awesome打包后引入失败问题：
		
		/build/webpack.base.conf.js中：
		{
			test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
			loader: 'url-loader',
			options: {
		  		limit: 10000, （改为：limit: 90000）
		 		name: utils.assetsPath('fonts/[name].[hash:7].[ext]')
			}
		}

5. 前端跨域问题：
		
		/config/index.js中：
		proxyTable: {（在proxyTable中添加如下代码）
	      '/crossDomain': {
		        target: 'http://127.0.0.1',
		        secure: true,  
		        changeOrigin: true, 
		        pathRewrite: {
		          '^/crossDomain': '' 
		        }
	    	}
		}

6. nginx反向代理：

		a、找到nginx文件夹中conf文件夹下的nginx.conf；
		b、找到如下代码：
			location / {
			   root  html;
			   index  index.html index.htm;
			}
		c、在其后加上如下代码（crossDomain为代理的名称，proxy_pass为需要调用的接口）
		    location /crossDomain {
		      rewrite  ^.+crossDomain/?(.*)$ /$1 break;
		      include  uwsgi_params;
		      proxy_pass  'http://127.0.0.1',
			}

7. 开发、部署接口配置

		a.开发：
			/config/prod.env.js中：
			module.exports = merge(prodEnv, {
			  ...
			  API: '"[开发的接口地址]"'(添加此句)
			}
	
		b.部署：
			/config/prod.env.js中：
			module.exports = {
			  ...
			  API: '"[部署的接口地址]"'(添加此句)
			}
		
		c.调用方法：
			process.env.API(直接调用即可)
		
##### webpack打包优化
1. 加入happypack

		文档地址：https://www.npmjs.com/package/happypack
		yarn add happypack
		a. /build/webpack.prod.conf.js的module.exports之前添加：
			const HappyPack = require('happypack')
			const os = require('os')
			const happyThreadPool = HappyPack.ThreadPool({ size: os.cpus().length })
		b. /build/webpack.prod.conf.js的module.exports中module/rules中修改js为如下方式：
	      {
	        test: /\.js$/,
	        loader: 'happypack/loader?id=happyBabel',
	        exclude: /node_modules/
	      }
		c. module.exports中添加：
			plugins: [
			    new HappyPack({
			      id: 'happyBabel',
			      loaders: [{
			        loader: 'babel-loader?cacheDirectory=true',
			      }],
			      threadPool: happyThreadPool,
			      verbose: true,
			    })
			]

2. 	加入webpack-parallel-uglify-plugin

		文档地址：https://www.npmjs.com/package/webpack-parallel-uglify-plugin
		yarn add webpack-parallel-uglify-plugin
		a. /build/webpack.prod.conf.js的module.exports之前添加：
			const ParallelUglifyPlugin = require('webpack-parallel-uglify-plugin')
		b. module.exports中添加：
			plugins: [
			    new ParallelUglifyPlugin({
			      cacheDir: '.cache/',
			      uglifyJS:{
			        output: {
			          comments: false
			        },
			        compress: {
			          warnings: false
			        }
			      }
			    })
			]

```