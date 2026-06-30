"""
06_advanced/jwt_verify.py
JWT（JSON Web Token）结构与验证

一个 JWT 由三部分组成，用点号分隔：
header.payload.signature

本脚本演示如何：
1. 解析 JWT 结构
2. 用 HMAC-SHA256 验证签名
3. 检查过期时间

注意：不要用本脚本处理生产 JWT，请使用 PyJWT 库。
"""

import base64
import hashlib
import hmac
import json
import time


def base64url_decode(data: str) -> bytes:
    """Base64URL 解码"""
    padding = 4 - len(data) % 4
    if padding != 4:
        data += "=" * padding
    return base64.urlsafe_b64decode(data)


def verify_jwt(token: str, secret: bytes) -> dict:
    """验证 JWT 并返回 payload"""
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("Invalid JWT format")

    header_b64, payload_b64, signature_b64 = parts

    # 重新计算签名
    signing_input = f"{header_b64}.{payload_b64}".encode("utf-8")
    expected_sig = base64.urlsafe_b64encode(
        hmac.new(secret, signing_input, hashlib.sha256).digest()
    ).decode("utf-8").rstrip("=")

    if not hmac.compare_digest(signature_b64, expected_sig):
        raise ValueError("Invalid signature")

    payload = json.loads(base64url_decode(payload_b64))

    # 检查过期时间
    if "exp" in payload and payload["exp"] < time.time():
        raise ValueError("Token expired")

    return payload


if __name__ == "__main__":
    secret = b"your-256-bit-secret"

    # 构造一个示例 JWT（HS256）
    header = base64.urlsafe_b64encode(
        json.dumps({"alg": "HS256", "typ": "JWT"}).encode()
    ).decode().rstrip("=")

    payload = base64.urlsafe_b64encode(
        json.dumps({"sub": "1234567890", "name": "Alice", "exp": int(time.time()) + 3600}).encode()
    ).decode().rstrip("=")

    signing_input = f"{header}.{payload}".encode("utf-8")
    signature = base64.urlsafe_b64encode(
        hmac.new(secret, signing_input, hashlib.sha256).digest()
    ).decode().rstrip("=")

    token = f"{header}.{payload}.{signature}"
    print(f"JWT: {token}")

    decoded = verify_jwt(token, secret)
    print(f"验证通过，payload: {decoded}")
