import sys
import hashlib
import hmac
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "03_hash"))

from hash_hmac import demo_hash, demo_hmac, demo_password_hash


def test_sha256_consistency():
    data = b"hello world"
    assert hashlib.sha256(data).hexdigest() == "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"


def test_sha256_avalanche_effect():
    d1 = hashlib.sha256(b"hello world").hexdigest()
    d2 = hashlib.sha256(b"Hello world").hexdigest()
    assert d1 != d2


def test_hmac_verification():
    key = b"my-secret-key"
    message = b"transfer $100 to Alice"
    mac = hmac.new(key, message, hashlib.sha256).hexdigest()
    expected = hmac.new(key, message, hashlib.sha256).hexdigest()
    assert hmac.compare_digest(mac, expected)


def test_hmac_detects_tampered_message():
    key = b"my-secret-key"
    message = b"transfer $100 to Alice"
    mac = hmac.new(key, message, hashlib.sha256).hexdigest()

    fake_message = b"transfer $10000 to Alice"
    expected = hmac.new(key, fake_message, hashlib.sha256).hexdigest()
    assert not hmac.compare_digest(mac, expected)
