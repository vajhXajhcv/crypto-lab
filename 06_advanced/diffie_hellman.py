"""
06_advanced/diffie_hellman.py
Diffie-Hellman 密钥交换

两个通信方各自生成私钥，通过公开信道交换公钥，最后都能独立计算出相同的共享密钥。
中间窃听者即使拿到双方的公钥，也无法算出共享密钥（离散对数问题）。
"""

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes


def generate_parameters():
    """生成 DH 参数（p 和 g）。实际应用中这些参数通常是预定义的。"""
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters


def derive_shared_key(shared_secret: bytes) -> bytes:
    """用 HKDF 把共享密钥派生为固定长度的 AES 密钥"""
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"crypto-lab-dh",
    ).derive(shared_secret)


def demo_dh():
    parameters = generate_parameters()

    # Alice
    alice_private = parameters.generate_private_key()
    alice_public = alice_private.public_key()

    # Bob
    bob_private = parameters.generate_private_key()
    bob_public = bob_private.public_key()

    # 交换公钥后，双方各自计算共享密钥
    alice_shared = alice_private.exchange(bob_public)
    bob_shared = bob_private.exchange(alice_public)

    alice_key = derive_shared_key(alice_shared)
    bob_key = derive_shared_key(bob_shared)

    print(f"Alice 的共享密钥: {alice_key.hex()}")
    print(f"Bob 的共享密钥:   {bob_key.hex()}")
    print(f"密钥一致: {alice_key == bob_key}")


if __name__ == "__main__":
    demo_dh()
