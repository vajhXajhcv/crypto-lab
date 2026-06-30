"""
06_advanced/fernet.py
Fernet：Python cryptography 提供的高级对称加密封装

Fernet 自动处理：
- AES-128-CBC 加密
- HMAC-SHA256 认证
- Base64 编码
- 时间戳和过期检查

适合"我不想自己处理 nonce、IV、MAC"的场景。
"""

from cryptography.fernet import Fernet


def demo_fernet():
    key = Fernet.generate_key()
    print(f"Fernet 密钥: {key.decode()}")

    f = Fernet(key)
    message = "Fernet 让对称加密变得简单"

    token = f.encrypt(message.encode("utf-8"))
    print(f"密文 token: {token.decode()}")

    decrypted = f.decrypt(token).decode("utf-8")
    print(f"解密结果: {decrypted}")


if __name__ == "__main__":
    demo_fernet()
