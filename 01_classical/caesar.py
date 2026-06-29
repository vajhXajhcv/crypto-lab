"""
01_classical/caesar.py
凯撒密码（Caesar Cipher）

原理：把字母表循环移动固定位数。
A + 3 → D, B + 3 → E, ..., Z + 3 → C

这是最早的替换密码之一，但非常不安全，因为密钥空间只有 25 种可能。
"""


def caesar_encrypt(text: str, shift: int) -> str:
    """加密：每个字母向后移动 shift 位"""
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            # 先归一化到 0-25，移位，再还原
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(cipher: str, shift: int) -> str:
    """解密：向前移动 shift 位"""
    return caesar_encrypt(cipher, -shift)


if __name__ == "__main__":
    message = "Hello, Caesar!"
    shift = 7

    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print(f"明文:    {message}")
    print(f"移位:    {shift}")
    print(f"密文:    {encrypted}")
    print(f"解密:    {decrypted}")

    # 练习：把 shift 改成 3，看看密文是什么？
    # 练习：尝试用 shift=26，结果会怎样？
