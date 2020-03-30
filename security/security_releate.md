# https sites

通过curl访问https网站总结

## 具体步骤

```bash
openssl pkcs12 -in private.pfx -out file.key.pem -nocerts -nodes
openssl pkcs12 -in private.pfx -out file.crt.pem -clcerts -nokeys  # 生成的为空文件，无用
openssl pkcs12 -in private.pfx -out client.pem -clcerts -nokeys
curl --insecure --key file.key.pem --cacert private.pem --cert client.pem  https://thewebsite/
```

注意: private.p12 是由private.pfx导入系统后，导出来的

## 需学习的

```text
pfx、p12、tls
```

## 参考资料

[http://www.rajatswarup.com/blog/2007/03/10/using-certificates-with-curl/](http://www.rajatswarup.com/blog/2007/03/10/using-certificates-with-curl/)
