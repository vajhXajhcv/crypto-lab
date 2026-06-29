# 练习：对称加密

## 练习 1：用密码派生密钥

当前示例直接生成随机密钥。修改 `aes_encrypt` / `aes_decrypt`，让它们接受一个**用户密码字符串**，并用 PBKDF2 或 Argon2id 派生出 32 字节密钥。

提示：同一个密码 + 同一个 salt 会得到同一个密钥。

## 练习 2：关联数据（Associated Data）

AES-GCM 支持 authenticated associated data（AAD）。尝试给 `aes_gcm.py` 增加一个 `associated_data` 参数，并验证：

- 解密时使用相同的 AAD 才能成功
- 修改 AAD 会导致解密失败

## 练习 3：文件加密工具

写一个 `encrypt_file(input_path, output_path, password)` 和 `decrypt_file(input_path, output_path, password)` 函数。

输出文件格式建议：`salt(16B) + nonce(12B) + ciphertext`。

## 练习 4：对比 ECB 和 GCM

用 `cryptography.hazmat.primitives.ciphers.Cipher` 实现一次 ECB 模式加密同一张图片或重复文本，观察为什么 ECB 不安全（会出现明显模式）。
