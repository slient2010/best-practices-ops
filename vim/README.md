# Mac下vim环境

## vim配置

见`vimrc`

## 使用

- 将`vimrc`拷贝到用户家目录，并重命名为`.vimrc`

```bash
cp vimrc ~/.vimrc
```

- 然后手动下载如下文件：

```bash
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

- 之后在打开的vim中输入`:PluginInstall`来安装相应的插件，等待完成后就可以使用了。

其中youcompleteme模块，需要登陆官方，查看使用方法。
