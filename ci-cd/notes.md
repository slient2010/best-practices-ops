# 一些笔记

- 命令行登陆

```bash
fly -t tutorial login -c http://172.19.1.18:8080 -u myuser -p mypass
```

- 触发任务

```bash
fly -t tutorial trigger-job  --job build-docker/publish  --watch
```

- 进入job容器

```bash
fly -t tutorial hijack  --job build-docker/publish
```

- 列出pipline

```bash
fly -t tutorial  pipelines
```

- 查看任务

```bash
fly -t tutorial watch -j build-docker/publish -b 30
```
