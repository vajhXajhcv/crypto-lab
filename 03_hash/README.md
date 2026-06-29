# 03 哈希与认证

## 目的

理解哈希函数、HMAC 和密码存储的区别。

## 文件

- `hash_hmac.py`：SHA-256、HMAC-SHA256、Argon2id 演示

## 运行

```bash
cd crypto-lab/03_hash
python hash_hmac.py
```

## 关键区别

| 场景 | 正确做法 | 错误做法 |
|------|---------|---------|
| 文件完整性校验 | SHA-256 / SHA-3 | MD5 / SHA-1 |
| API 请求认证 | HMAC-SHA256 | 普通 SHA-256 |
| 密码存储 | Argon2id / bcrypt / scrypt | SHA-256 / MD5 |

## 思考题

1. 为什么 HMAC 需要密钥，而 SHA-256 不需要？
2. 为什么密码存储不能用快速哈希？
