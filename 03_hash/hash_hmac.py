"""
03_hash/hash_hmac.py
哈希、HMAC 与密码存储

- 哈希（Hash）：单向函数，任意长度输入 → 固定长度输出，无法反推
- HMAC：哈希消息认证码，需要密钥，用于验证消息完整性和来源
- 密码存储：不能直接存哈希，要加盐 + 慢哈希（如 Argon2 / bcrypt）
"""

import hashlib
import hmac
import os
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id


def demo_hash():
    """演示 SHA-256"""
    data = b"hello world"
    digest = hashlib.sha256(data).hexdigest()
    print(f"SHA-256('hello world') = {digest}")

    # 改一个字母，哈希完全不同（雪崩效应）
    data2 = b"Hello world"
    print(f"SHA-256('Hello world') = {hashlib.sha256(data2).hexdigest()}")


def demo_hmac():
    """演示 HMAC：需要共享密钥"""
    key = b"my-secret-key"
    message = b"transfer $100 to Alice"

    mac = hmac.new(key, message, hashlib.sha256).hexdigest()
    print(f"HMAC-SHA256 = {mac[:32]}...")

    # 验证时重新计算一次，对比是否相同
    expected = hmac.new(key, message, hashlib.sha256).hexdigest()
    print(f"验证通过: {hmac.compare_digest(mac, expected)}")


def demo_password_hash():
    """演示 Argon2id 密码哈希（推荐算法）"""
    password = b"correct horse battery staple"
    salt = os.urandom(16)

    # Argon2id 参数：迭代次数、内存、并行度
    kdf = Argon2id(
        salt=salt,
        length=32,
        iterations=3,
        lanes=4,
        memory_cost=64 * 1024,  # 64 MB
    )
    key = kdf.derive(password)
    print(f"Argon2id 派生密钥: {key.hex()[:32]}...")
    print("注意：这是 KDF 派生，不是直接存储密码哈希。生产环境用 passlib / bcrypt 更方便。")


if __name__ == "__main__":
    print("=== SHA-256 ===")
    demo_hash()

    print("\n=== HMAC ===")
    demo_hmac()

    print("\n=== Argon2id 派生 ===")
    demo_password_hash()

    # 关键结论：
    # 1. SHA-256 很快，适合校验文件完整性，不适合直接存密码
    # 2. HMAC 需要密钥，能防止第三方伪造
    # 3. 密码存储要用专门算法：Argon2id / bcrypt / scrypt
