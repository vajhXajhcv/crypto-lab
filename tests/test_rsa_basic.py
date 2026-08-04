import os
import sys
import pytest

# Make 04_asymmetric directory importable
sys.path.insert(0, os.path.abspath("04_asymmetric"))
import rsa_basic


def test_rsa_encrypt_decrypt_roundtrip():
    priv, pub = rsa_basic.generate_keypair()
    message = "Hello RSA"
    ciphertext = rsa_basic.rsa_encrypt(message, pub)
    assert isinstance(ciphertext, bytes)

    plaintext = rsa_basic.rsa_decrypt(ciphertext, priv)
    assert plaintext == message


def test_rsa_sign_and_verify():
    priv, pub = rsa_basic.generate_keypair()
    message = "Important message"
    sig = rsa_basic.rsa_sign(message, priv)
    assert isinstance(sig, bytes)
    assert rsa_basic.rsa_verify(message, sig, pub) is True

    # tamper with message
    assert rsa_basic.rsa_verify(message + "!", sig, pub) is False
