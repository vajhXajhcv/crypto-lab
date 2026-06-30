# 06 进阶主题

## 目的

在掌握基础之后，接触真实系统中常用的进阶技术。

## 文件

- `diffie_hellman.py`：Diffie-Hellman 密钥交换
- `ecdsa.py`：椭圆曲线数字签名
- `fernet.py`：cryptography 库的高级对称加密封装
- `jwt_verify.py`：JWT 结构与 HMAC 签名验证

## 运行

```bash
cd crypto-lab/06_advanced
python diffie_hellman.py
python ecdsa.py
python fernet.py
python jwt_verify.py
```

## 学习建议

- 理解 DH 为什么能让我们在公开信道上协商密钥
- 对比 ECDSA 与 RSA 的密钥长度和性能
- 了解 Fernet 适合什么场景，不适合什么场景
- JWT 的 payload 是 Base64 编码，不是加密，不要放敏感信息
