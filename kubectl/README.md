# 设置kubectl客户端配置

```bash
kubectl config set-cluster cluster-name \
  --server=https://${ipaddress}:6443 --certificate-authority=ca.crt

kubectl config set-credentials cluster-name \
  --certificate-authority=ca.crt --client-key=admin.key --client-certificate=admin.crt

kubectl config set-context culster-name  --cluster=cluster-name --user=cluster-name

kubectl config use-context cluster-name
```
