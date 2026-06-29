# 05 真实世界协议

## 目的

看看互联网每天都在用的 TLS/HTTPS 到底是什么。

## 文件

- `inspect_tls.py`：检查目标网站的 TLS 证书和加密套件

## 运行

```bash
cd crypto-lab/05_realworld
python inspect_tls.py
```

## 你会看到

- TLS 版本（如 TLSv1.3）
- 加密套件名称
- 证书链信息
- 证书有效期

## 延伸学习

1. 用浏览器打开任意 HTTPS 网站，点击地址栏小锁，查看证书
2. 了解 TLS 1.3 握手过程
3. 了解什么是证书颁发机构（CA）和证书链
