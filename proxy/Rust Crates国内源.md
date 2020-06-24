#Rust Crates 国内源地址代理

## 修改方式

在`$HOME/.cargo/config`中添加如下内容：

```text
[source.crates-io]
replace-with = 'ustc'

[source.ustc]
registry = "git://mirrors.ustc.edu.cn/crates.io-index"
```

如果所处的环境中不允许使用 git 协议，可以把上述地址改为：

```text
registry = "https://mirrors.ustc.edu.cn/crates.io-index"
```

## 参考地址

[https://mirrors.ustc.edu.cn/help/crates.io-index.html](https://mirrors.ustc.edu.cn/help/crates.io-index.html)
