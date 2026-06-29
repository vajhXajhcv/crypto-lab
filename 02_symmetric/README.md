# 02 对称加密

## 目的

学会正确使用现代对称加密：AES-256-GCM。

## 文件

- `aes_gcm.py`：AES-256-GCM 加密、解密、篡改检测

## 运行

```bash
cd crypto-lab/02_symmetric
python aes_gcm.py
```

## 关键概念

- **AES**：目前最广泛使用的分组密码
- **GCM**：认证加密模式，同时保证机密性和完整性
- **Nonce**：每次加密必须唯一，可以公开
- **Key**：必须保密，32 字节（256 位）

## 安全红线

1. 不要自己实现 AES，用标准库
2. 不要用 ECB 模式
3. 不要重复使用 nonce
4. 不要用密码直接当密钥，要用 KDF（如 Argon2 / PBKDF2）派生
