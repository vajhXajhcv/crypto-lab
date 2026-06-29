import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "01_classical"))

from caesar import caesar_encrypt, caesar_decrypt
from frequency_analysis import guess_shift, crack_caesar


def test_caesar_roundtrip():
    text = "Hello, Caesar Cipher!"
    for shift in [0, 3, 7, 11, 25]:
        encrypted = caesar_encrypt(text, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        assert decrypted == text


def test_caesar_shift_26_is_identity():
    text = "ABCxyz"
    assert caesar_encrypt(text, 26) == text


def test_frequency_analysis_guesses_shift():
    # 使用一段足够长、字母频率接近英语的文本，确保 E 是最高频字母
    plaintext = (
        "The enormous elephant eagerly entered the elegant entrance "
        "every evening, expecting excellent entertainment. "
        "Everywhere everyone expressed endless enthusiasm."
    )
    shift = 11
    ciphertext = caesar_encrypt(plaintext, shift)
    guessed = guess_shift(ciphertext)
    assert guessed == shift


def test_crack_caesar_recovers_plaintext():
    plaintext = (
        "The enormous elephant eagerly entered the elegant entrance "
        "every evening, expecting excellent entertainment. "
        "Everywhere everyone expressed endless enthusiasm."
    )
    shift = 11
    ciphertext = caesar_encrypt(plaintext, shift)
    cracked = crack_caesar(ciphertext)
    assert cracked == plaintext
