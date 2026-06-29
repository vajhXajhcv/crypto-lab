"""
01_classical/frequency_analysis.py
频率分析破解凯撒密码

英语中最常见的字母是 E、T、A、O、I、N。
如果密文是简单的替换/移位密码，我们可以通过统计密文字母频率来反推移位量。
"""

from collections import Counter
from caesar import caesar_encrypt


def guess_shift(cipher: str) -> int:
    """通过频率分析猜测凯撒密码的移位量"""
    # 只统计字母
    letters = [ch for ch in cipher.upper() if ch.isalpha()]
    if not letters:
        return 0

    # 找到密文中出现最多的字母
    most_common = Counter(letters).most_common(1)[0][0]

    # 假设它对应英语中最常见的字母 E
    shift = (ord(most_common) - ord("E")) % 26
    return shift


def crack_caesar(cipher: str) -> str:
    """自动破解并返回最可能的明文"""
    shift = guess_shift(cipher)
    from caesar import caesar_decrypt

    return caesar_decrypt(cipher, shift)


if __name__ == "__main__":
    plaintext = (
        "The quick brown fox jumps over the lazy dog. "
        "Cryptography is the practice of secure communication."
    )
    secret_shift = 11
    ciphertext = caesar_encrypt(plaintext, secret_shift)

    print(f"明文:     {plaintext}")
    print(f"密文:     {ciphertext}")
    print(f"真实移位: {secret_shift}")

    guessed_shift = guess_shift(ciphertext)
    cracked = crack_caesar(ciphertext)

    print(f"猜测移位: {guessed_shift}")
    print(f"破解结果: {cracked}")

    # 思考：为什么短句可能破解失败？
    # 提示：样本量不够时，统计规律不成立。
