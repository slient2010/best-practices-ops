# tools

[Capture website screenshots](https://github.com/sindresorhus/pageres)

```bash
pageres 'https://website/d?from=now-24h&to=now&kiosk=tv' '--header=Authorization: token' --crop --hide=.page-header 2200x1300 --filename=filename
```

## virtualbox cli

```bash
VBoxManage startvm debian10 --type headless
VBoxManage list runningvms
VBoxManage controlvm debian10 poweroff soft
```

