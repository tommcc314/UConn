from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
with open('./Q4files/.key.txt', 'rb') as file:
    key = file.read()
with open('./Q4files/Encrypted4', 'rb') as file:
    iv = file.read(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(file.read()), AES.block_size).decode()
print(plaintext)