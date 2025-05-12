from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os
import ast
def decrypt():
    k = ast.literal_eval(input("Enter key: "))
    txtfiles = [f for f in os.listdir('.') if f.endswith('.txt.encrypted')]
    for txtfile in txtfiles:
        enc = open(txtfile, "rb")
        with open(txtfile.replace(".encrypted", ""), "w") as orig:
            iv = enc.read(16)
            kencryption = AES.new(k, AES.MODE_CBC, iv)
            while True:
                data = enc.read(1024)
                if not data:
                    break
                orig.write(unpad(kencryption.decrypt(data), AES.block_size).decode())
        os.remove(txtfile)
if __name__ == "__main__":
    decrypt()
