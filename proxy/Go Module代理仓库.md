# Go Module代理仓库服务

## 简介

go module公共代理仓库，代理并缓存go模块。你可以利用该代理来避免DNS污染导致的模块拉取缓慢或失败的问题，加速你的构建

地址[https://mirrors.aliyun.com/goproxy/](https://mirrors.aliyun.com/goproxy/)

## 使用帮助

- 使用阿里云代理

1.使用go1.11以上版本并开启go module机制

2.导出GOPROXY环境变量

```bash
export GOPROXY=https://mirrors.aliyun.com/goproxy/
```

- 使用官方代理

To start using it, all you have is to set the environment variable:

```bash
GOPROXY=https://proxy.golang.org
```

Other public proxies are:

```bash
GOPROXY=https://goproxy.io
GOPROXY=https://goproxy.cn # proxy.golang.org is blocked in China, this proxy is not
```

more configurations, see below.

## 参考资料

[https://studygolang.com/articles/24119](https://studygolang.com/articles/24119)

[https://arslan.io/2019/08/02/why-you-should-use-a-go-module-proxy/](https://arslan.io/2019/08/02/why-you-should-use-a-go-module-proxy/)
