# 练习：真实世界协议

## 练习 1：检查多个网站

扩展 `inspect_tls.py`，批量检查以下网站并汇总报告：

- wumingmp.me
- github.com
- google.com
- baidu.com

比较它们的 TLS 版本、证书颁发商、过期时间。

## 练习 2：模拟中间人检测

如果访问一个使用自签名证书的网站，`ssl.create_default_context()` 会报错。捕获这个异常并解释为什么浏览器会拦截这类网站。

## 练习 3：HTTP 严格传输安全（HSTS）

用 `requests` 或 `urllib` 发送 HTTP 请求，检查响应头中是否有 `Strict-Transport-Security`。它有什么作用？

## 练习 4：握手时间测量

用 Python 的 `time` 模块测量完成一次 TLS 握手需要多少毫秒。对比 TLS 1.2 和 TLS 1.3 的网站（如果找得到）。
