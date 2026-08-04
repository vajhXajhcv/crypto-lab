import os
import sys
import pytest
from cryptography.exceptions import InvalidTag

# Make the 02_symmetric directory importable (module names starting with digits are invalid)
sys.path.insert(0, os.path.abspath("02_symmetric"))
import aes_gcm


def test_aes_gcm_roundtrip():
    """Encrypt then decrypt returns the original plaintext."""
    key = aes_gcm.AESGCM.generate_key(bit_length=256)
    plaintext = "这是一个测试消息。"
    nonce, ciphertext = aes_gcm.aes_encrypt(plaintext, key)

    assert isinstance(nonce, bytes)
    assert isinstance(ciphertext, bytes)

    decrypted = aes_gcm.aes_decrypt(nonce, ciphertext, key)
    assert decrypted == plaintext


def test_aes_gcm_tamper_detection():
    """Modifying the ciphertext should raise InvalidTag on decrypt."""
    key = aes_gcm.AESGCM.generate_key(bit_length=256)
    nonce, ciphertext = aes_gcm.aes_encrypt("secret-data", key)

    tampered = bytearray(ciphertext)
    tampered[0] ^= 0xFF

    with pytest.raises(InvalidTag):
        aes_gcm.aes_decrypt(nonce, bytes(tampered), key)


def test_aes_gcm_wrong_key_length():
    """Providing a key with incorrect length should raise ValueError."""
    bad_key = b"short-key"
    with pytest.raises(ValueError):
        aes_gcm.aes_encrypt("data", bad_key)
