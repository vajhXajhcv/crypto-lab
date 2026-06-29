"""
04_asymmetric/rsa_basic.py
RSA 基础：公钥加密、私钥解密、数字签名

核心思想：
- 公钥可以公开，用来加密或验证签名
- 私钥必须保密，用来解密或生成签名

注意：实际应用中 RSA 通常用于加密小数据（如对称密钥），大量数据用 AES。
"""

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding


def generate_keypair():
    """生成 2048 位 RSA 密钥对"""
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key


def rsa_encrypt(plaintext: str, public_key) -> bytes:
    """用公钥加密"""
    return public_key.encrypt(
        plaintext.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


def rsa_decrypt(ciphertext: bytes, private_key) -> str:
    """用私钥解密"""
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return plaintext.decode("utf-8")


def rsa_sign(message: str, private_key) -> bytes:
    """用私钥签名"""
    return private_key.sign(
        message.encode("utf-8"),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )


def rsa_verify(message: str, signature: bytes, public_key) -> bool:
    """用公钥验证签名"""
    try:
        public_key.verify(
            signature,
            message.encode("utf-8"),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return True
    except Exception:
        return False


if __name__ == "__main__":
    private_key, public_key = generate_keypair()

    # 加密通信
    msg = "这条消息只有持有私钥的人才能看到。"
    cipher = rsa_encrypt(msg, public_key)
    print(f"RSA 密文: {cipher.hex()[:64]}...")
    print(f"RSA 解密: {rsa_decrypt(cipher, private_key)}")

    # 数字签名
    contract = "我同意向 Bob 支付 100 元。"
    signature = rsa_sign(contract, private_key)
    print(f"\n签名: {signature.hex()[:64]}...")
    print(f"验证签名: {rsa_verify(contract, signature, public_key)}")

    # 篡改消息后验证失败
    fake_contract = "我同意向 Bob 支付 10000 元。"
    print(f"篡改后验证: {rsa_verify(fake_contract, signature, public_key)}")
