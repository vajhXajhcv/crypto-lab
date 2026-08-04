import os
import sys
import pytest

# Make the 01_classical directory importable
sys.path.insert(0, os.path.abspath("01_classical"))
import caesar
import frequency_analysis


def test_caesar_roundtrip():
    message = "Hello, Caesar!"
    shift = 7
    encrypted = caesar.caesar_encrypt(message, shift)
    decrypted = caesar.caesar_decrypt(encrypted, shift)
    assert decrypted == message


def test_frequency_analysis_guess_shift_and_crack():
    # Construct a plaintext with a clear most-frequent letter 'e'
    plaintext = "e" * 50 + "a" * 10 + "b" * 5 + "c" * 3 + "\n"
    secret_shift = 11

    ciphertext = caesar.caesar_encrypt(plaintext, secret_shift)
    guessed = frequency_analysis.guess_shift(ciphertext)
    assert guessed == secret_shift

    cracked = frequency_analysis.crack_caesar(ciphertext)
    # Comparison case-insensitive because crack_caesar uses caesar_decrypt which preserves case
    assert cracked.lower() == plaintext.lower()


def test_frequency_analysis_empty_returns_zero():
    assert frequency_analysis.guess_shift("1234!@#$") == 0
