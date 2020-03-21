# 设置kubectl客户端配置

```bash
kubectl config set-cluster cluster-name \
  --server=https://${ipaddress}:6443 --certificate-authority=ca.crt

kubectl config set-credentials cluster-name \
  --certificate-authority=ca.crt --client-key=admin.key --client-certificate=admin.crt

kubectl config set-context culster-name  --cluster=cluster-name --user=cluster-name

kubectl config use-context cluster-name
```

`metallb`通过k8s原生的方式提供LB类型的Service支持，开箱即用

[https://metallb.universe.tf/](https://metallb.universe.tf/)
