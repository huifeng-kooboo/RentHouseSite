### Vue项目部署到CentOS服务器

* ```config/index.js```上修改以下部分：

  首先是```host:'localhost'```改为服务器ip

  ```assetsPublicPath:'/'```改为```assetsPublicPath:'./'```

* 运行```npm install```

* ```npm run build```

* 将dist下的static文件夹和Index.html单独复制出来存在github项目上（原因是方便复制和修改）

* 进入CENTOS服务器

* 先安装nginx 安装教程可参考```https://www.cnblogs.com/jackyzm/p/9600738.html``

* ```cd etc/nginx```

* ```vim nginx.conf```

* 修改如下数据

* ![1569380016715](C:\Users\coder\AppData\Roaming\Typora\typora-user-images\1569380016715.png)

其中 ```server_name```写的是服务器ip

```listen```写的是端口号

```root```写的是static文件夹和index.html 不建议放在root目录下 有可能出错。

然后保存修改文件

进入etc文件夹下，执行两条命令即可

```nginx -s reload``` 重新载入配置

```nginx -s reopen``` 重启服务

然后输入ip地址加端口号8080 ，如果显示，就说明没问题了。