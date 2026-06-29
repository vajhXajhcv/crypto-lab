# 练习：哈希与认证

## 练习 1：文件校验

写一个 `file_hash(path)` 函数，计算任意文件的 SHA-256 值。用它验证下载的文件是否完整。

## 练习 2：实现简单 MAC

不用 HMAC，直接用 `hashlib.sha256(key + message)` 计算 MAC。这个做法有什么问题？

提示：长度扩展攻击、密钥前缀冲突。

## 练习 3：密码注册/登录模拟

实现两个函数：

```python
def register(username, password) -> (salt, hash):
    ...

def login(username, password, salt, stored_hash) -> bool:
    ...
```

使用 Argon2id 或 bcrypt。不要用 SHA-256。

## 练习 4：彩虹表攻击

生成一个常见密码列表（如 `password`, `123456`, `qwerty`），预计算它们的 SHA-256 值。给定一个哈希值，能否快速反查？这就是彩虹表的基本思想，也是为什么要加盐。
