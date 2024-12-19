import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def secure_function():
    user_input = input("Enter a command: ")
    print("Executing:", user_input)  # Safe handling without shell execution

def strong_crypto():
    key = os.urandom(32)  # 256-bit key for AES
    iv = os.urandom(16)   # 128-bit IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv))

secure_function()
strong_crypto()
