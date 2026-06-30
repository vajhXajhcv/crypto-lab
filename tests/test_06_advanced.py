import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "06_advanced"))

from diffie_hellman import generate_parameters, derive_shared_key
from ecdsa import generate_keypair, ecdsa_sign, ecdsa_verify
from fernet import Fernet
from jwt_verify import verify_jwt
import json
import base64
import hashlib
import hmac
import time


def test_diffie_hellman_shared_secret():
    parameters = generate_parameters()
    alice_private = parameters.generate_private_key()
    bob_private = parameters.generate_private_key()

    alice_shared = alice_private.exchange(bob_private.public_key())
    bob_shared = bob_private.exchange(alice_private.public_key())

    alice_key = derive_shared_key(alice_shared)
    bob_key = derive_shared_key(bob_shared)

    assert alice_key == bob_key
    assert len(alice_key) == 32


def test_ecdsa_sign_verify():
    private_key, public_key = generate_keypair()
    message = "test message"
    signature = ecdsa_sign(message, private_key)
    assert ecdsa_verify(message, signature, public_key) is True
    assert ecdsa_verify("tampered", signature, public_key) is False


def test_fernet_roundtrip():
    key = Fernet.generate_key()
    f = Fernet(key)
    message = "hello fernet"
    token = f.encrypt(message.encode())
    assert f.decrypt(token).decode() == message


def test_jwt_verify():
    secret = b"test-secret"
    header = base64.urlsafe_b64encode(
        json.dumps({"alg": "HS256", "typ": "JWT"}).encode()
    ).decode().rstrip("=")
    payload = base64.urlsafe_b64encode(
        json.dumps({"sub": "1", "exp": int(time.time()) + 3600}).encode()
    ).decode().rstrip("=")
    signing_input = f"{header}.{payload}".encode("utf-8")
    signature = base64.urlsafe_b64encode(
        hmac.new(secret, signing_input, hashlib.sha256).digest()
    ).decode().rstrip("=")
    token = f"{header}.{payload}.{signature}"

    decoded = verify_jwt(token, secret)
    assert decoded["sub"] == "1"
