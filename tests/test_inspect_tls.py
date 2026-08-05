import os
import sys
import pytest

# Ensure 05_realworld is importable
sys.path.insert(0, os.path.abspath("05_realworld"))
import inspect_tls


def test_inspect_tls_localhost_fails_fast(monkeypatch):
    # Provide a hostname that will likely fail to connect quickly (invalid domain)
    with pytest.raises(Exception):
        inspect_tls.inspect_tls("nonexistent.invalid.example", port=443)


def test_inspect_tls_github(monkeypatch):
    # Do a real network call to github.com — this is flaky in CI without network access.
    # Instead of performing the network call in CI, we mark it as skipped if no network.
    import socket

    try:
        # Quick network reachability check
        socket.gethostbyname("github.com")
    except Exception:
        pytest.skip("Network unavailable in test environment")

    # If we reach here, call the function to ensure it runs without raising
    inspect_tls.inspect_tls("github.com")
