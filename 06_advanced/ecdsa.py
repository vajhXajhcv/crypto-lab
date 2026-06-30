"""
06_advanced/ecdsa.py
椭圆曲线数字签名算法（ECDSA）

相比 RSA，ECDSA 可以用更短的密钥达到相同的安全强度。
"""

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes


def generate_keypair():
    private_key = ec.generate_private_key(ec.SECP256R1())
    return private_key, private_key.public_key()


def ecdsa_sign(message: str, private_key) -> bytes:
    return private_key.sign(message.encode("utf-8"), ec.ECDSA(hashes.SHA256()))


def ecdsa_verify(message: str, signature: bytes, public_key) -> bool:
    try:
        public_key.verify(signature, message.encode("utf-8"), ec.ECDSA(hashes.SHA256()))
        return True
    except Exception:
        return False


if __name__ == "__main__":
    private_key, public_key = generate_keypair()

    msg = "用 ECDSA 签名的消息"
    signature = ecdsa_sign(msg, private_key)

    print(f"签名: {signature.hex()[:64]}...")
    print(f"验证通过: {ecdsa_verify(msg, signature, public_key)}")
    print(f"篡改后验证: {ecdsa_verify('被篡改的消息', signature, public_key)}")
