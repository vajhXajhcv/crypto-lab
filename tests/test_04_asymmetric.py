import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "04_asymmetric"))

from rsa_basic import generate_keypair, rsa_encrypt, rsa_decrypt, rsa_sign, rsa_verify


def test_rsa_encrypt_decrypt():
    private_key, public_key = generate_keypair()
    message = "只有私钥能解开这条消息"
    ciphertext = rsa_encrypt(message, public_key)
    decrypted = rsa_decrypt(ciphertext, private_key)
    assert decrypted == message


def test_rsa_sign_verify():
    private_key, public_key = generate_keypair()
    contract = "我同意向 Bob 支付 100 元。"
    signature = rsa_sign(contract, private_key)
    assert rsa_verify(contract, signature, public_key) is True


def test_rsa_detects_tampered_contract():
    private_key, public_key = generate_keypair()
    contract = "我同意向 Bob 支付 100 元。"
    signature = rsa_sign(contract, private_key)
    fake_contract = "我同意向 Bob 支付 10000 元。"
    assert rsa_verify(fake_contract, signature, public_key) is False
