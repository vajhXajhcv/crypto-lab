# 练习：非对称加密

## 练习 1：保存和加载密钥

把 RSA 私钥保存为 PEM 文件，公钥保存为另一个 PEM 文件。然后重新加载它们，验证加密/解密仍然正常。

提示：使用 `private_key.private_bytes()` 和 `public_key.public_bytes()`。

## 练习 2：混合加密

RSA 不适合加密大量数据。实现：

1. 生成随机 AES 密钥
2. 用 RSA 公钥加密 AES 密钥
3. 用 AES-GCM 加密消息
4. 发送 `encrypted_aes_key + nonce + ciphertext`
5. 接收方用 RSA 私钥解密 AES 密钥，再解密消息

## 练习 3：证书链验证

用 `cryptography.x509` 读取一个 `.crt` 文件，解析：

- 证书主题
- 颁发者
- 有效期
- 公钥算法

## 练习 4：ECC 入门

用 `cryptography.hazmat.primitives.asymmetric.ec` 生成一个 ECDSA 密钥对，实现签名和验证。对比 RSA 和 ECDSA 的密钥长度与性能。
