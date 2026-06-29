"""
05_realworld/inspect_tls.py
查看真实 HTTPS 连接的 TLS 证书信息

运行前确保能联网。这个脚本会连接到指定域名，显示：
- 协议版本
- 证书颁发者
- 证书有效期
- 主题备用名（SAN）
"""

import ssl
import socket


def inspect_tls(hostname: str, port: int = 443):
    context = ssl.create_default_context()

    with socket.create_connection((hostname, port), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            cipher = ssock.cipher()
            version = ssock.version()

            print(f"主机:     {hostname}:{port}")
            print(f"TLS 版本: {version}")
            print(f"加密套件: {cipher[0]}")
            print(f"证书主题: {cert.get('subject')}")
            print(f"颁发者:   {cert.get('issuer')}")

            not_before = cert.get("notBefore")
            not_after = cert.get("notAfter")
            print(f"生效时间: {not_before}")
            print(f"过期时间: {not_after}")

            san = cert.get("subjectAltName", [])
            print(f"SAN:      {[name for _, name in san][:5]}...")


if __name__ == "__main__":
    inspect_tls("wumingmp.me")

    # 练习：换成其他网站试试，比如 github.com, google.com
    # inspect_tls("github.com")
