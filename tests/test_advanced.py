import os
import sys
import pytest

# Make 06_advanced importable
sys.path.insert(0, os.path.abspath("06_advanced"))
import diffie_hellman
import ecdsa
from cryptography.fernet import Fernet
import jwt_verify


def test_diffie_hellman_shared_key_agreement():
    params = diffie_hellman.generate_parameters()
    a_priv = params.generate_private_key()
    b_priv = params.generate_private_key()

    a_pub = a_priv.public_key()
    b_pub = b_priv.public_key()

    a_shared = a_priv.exchange(b_pub)
    b_shared = b_priv.exchange(a_pub)

    a_key = diffie_hellman.derive_shared_key(a_shared)
    b_key = diffie_hellman.derive_shared_key(b_shared)

    assert a_key == b_key
    assert len(a_key) == 32


def test_ecdsa_sign_verify():
    priv, pub = ecdsa.generate_keypair()
    msg = "hello ecdsa"
    sig = ecdsa.ecdsa_sign(msg, priv)
    assert ecdsa.ecdsa_verify(msg, sig, pub)
    assert not ecdsa.ecdsa_verify(msg + "!", sig, pub)


def test_fernet_encrypt_decrypt_roundtrip():
    key = Fernet.generate_key()
    f = Fernet(key)
    msg = b"secret message"
    token = f.encrypt(msg)
    assert f.decrypt(token) == msg


def test_jwt_verify_valid_and_expired():
    secret = b"test-secret"

    # construct token
    import base64, json, time, hmac, hashlib

    header = base64.urlsafe_b64encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode()).decode().rstrip("=")
    payload = base64.urlsafe_b64encode(json.dumps({"sub": "1", "exp": int(time.time()) + 60}).encode()).decode().rstrip("=")
    signing_input = f"{header}.{payload}".encode()
    signature = base64.urlsafe_b64encode(hmac.new(secret, signing_input, hashlib.sha256).digest()).decode().rstrip("=")
    token = f"{header}.{payload}.{signature}"

    decoded = jwt_verify.verify_jwt(token, secret)
    assert decoded["sub"] == "1"

    # expired token
    payload_exp = base64.urlsafe_b64encode(json.dumps({"sub": "1", "exp": int(time.time()) - 10}).encode()).decode().rstrip("=")
    signing_input_exp = f"{header}.{payload_exp}".encode()
    signature_exp = base64.urlsafe_b64encode(hmac.new(secret, signing_input_exp, hashlib.sha256).digest()).decode().rstrip("=")
    token_exp = f"{header}.{payload_exp}.{signature_exp}"

    with pytest.raises(ValueError):
        jwt_verify.verify_jwt(token_exp, secret)
