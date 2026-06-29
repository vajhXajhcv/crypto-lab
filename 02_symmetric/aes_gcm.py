"""
02_symmetric/aes_gcm.py
AES-256-GCM：现代对称加密的推荐用法

GCM 模式同时提供：
- 机密性（Confidentiality）：加密数据，外人看不懂
- 完整性/认证（Integrity/Authenticity）：防止篡改，并验证密钥是否正确

关键概念：
- key: 32 字节（256 位），必须保密
- nonce: 12 字节（96 位），每次加密必须不同，不需要保密
- tag: 认证标签，通常附加在密文末尾
"""

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def aes_encrypt(plaintext: str, key: bytes) -> tuple[bytes, bytes]:
    """AES-256-GCM 加密，返回 (nonce, ciphertext_with_tag)"""
    if len(key) != 32:
        raise ValueError("AES-256 需要 32 字节密钥")

    nonce = os.urandom(12)  # 每次加密都生成新的随机 nonce
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, plaintext.encode("utf-8"), None)
    return nonce, ciphertext


def aes_decrypt(nonce: bytes, ciphertext: bytes, key: bytes) -> str:
    """AES-256-GCM 解密。如果密文被篡改或密钥错误，会抛出 InvalidTag"""
    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext.decode("utf-8")


if __name__ == "__main__":
    # 1. 生成一个安全的随机密钥
    key = AESGCM.generate_key(bit_length=256)
    print(f"密钥（hex）: {key.hex()}")

    # 2. 加密
    message = "这是只有你我才能看到的秘密消息。"
    nonce, ciphertext = aes_encrypt(message, key)
    print(f"Nonce（hex）: {nonce.hex()}")
    print(f"密文（hex）:  {ciphertext.hex()[:80]}...")

    # 3. 解密
    decrypted = aes_decrypt(nonce, ciphertext, key)
    print(f"解密结果:    {decrypted}")

    # 4. 演示完整性保护：篡改一个字节
    tampered = bytearray(ciphertext)
    tampered[0] ^= 0xFF
    try:
        aes_decrypt(nonce, bytes(tampered), key)
    except Exception as e:
        print(f"\n篡改检测: 发现异常！{type(e).__name__}")

    # 重要规则：
    # 1. 永远不要重复使用同一个 (key, nonce) 对
    # 2. nonce 可以和密文一起明文传输
    # 3. 密钥必须通过安全渠道分发
