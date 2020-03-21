# Angular设置国内代理

直接下载下来跑命令 npm install -g @angular/cli 会报错

```text
“ETIMEDOUT: request to https://registry.npmjs.org/ini failed” 
```

## 代理设置

设置下registry就可以了，proxy不用修改，保持null就可以。报400 bad request也是代理问题

```bash
npm config set registry https://registry.npm.taobao.org
```

查看proxy：
```bash
npm config get proxy
npm config get https-proxy
```

修改为Null

```bash
npm config set proxy null
npm config set https-proxy null
```

## 参考资料

[https://blog.csdn.net/slience_blank/article/details/88855961](https://blog.csdn.net/slience_blank/article/details/88855961)
