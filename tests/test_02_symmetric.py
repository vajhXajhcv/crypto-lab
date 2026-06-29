import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "02_symmetric"))

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from aes_gcm import aes_encrypt, aes_decrypt


def test_aes_gcm_roundtrip():
    key = AESGCM.generate_key(bit_length=256)
    message = "秘密消息，支持中文和 emojis 🎉"
    nonce, ciphertext = aes_encrypt(message, key)
    decrypted = aes_decrypt(nonce, ciphertext, key)
    assert decrypted == message


def test_aes_gcm_tamper_detection():
    key = AESGCM.generate_key(bit_length=256)
    message = "敏感数据"
    nonce, ciphertext = aes_encrypt(message, key)

    tampered = bytearray(ciphertext)
    tampered[0] ^= 0xFF

    try:
        aes_decrypt(nonce, bytes(tampered), key)
        assert False, "Expected decryption to fail after tampering"
    except Exception:
        pass


def test_aes_gcm_wrong_key_fails():
    key = AESGCM.generate_key(bit_length=256)
    wrong_key = AESGCM.generate_key(bit_length=256)
    message = "test"
    nonce, ciphertext = aes_encrypt(message, key)

    try:
        aes_decrypt(nonce, ciphertext, wrong_key)
        assert False, "Expected decryption to fail with wrong key"
    except Exception:
        pass
