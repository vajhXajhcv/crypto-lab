# 练习：古典密码

## 练习 1：暴力破解凯撒密码

不用频率分析，直接尝试 shift = 1 到 25，找到有意义的英文句子。

```python
from caesar import caesar_decrypt

ciphertext = "Esp bftnv mczhy qzi ufxad zgpc esp wlkj ozr."
for shift in range(1, 26):
    print(shift, caesar_decrypt(ciphertext, shift))
```

## 练习 2：实现 ROT13

ROT13 是 shift=13 的凯撒密码。写一个 `rot13(text)` 函数，并验证它是对合运算（即 `rot13(rot13(x)) == x`）。

## 练习 3：处理非英文字符

当前 `caesar_encrypt` 会跳过非字母字符。修改它，让它也能处理数字（例如 `0-9` 循环移位）。

## 练习 4：频率分析的局限

找一段中文或很短的英文句子，观察 `guess_shift()` 为什么会失败。思考：如何让频率分析更可靠？
