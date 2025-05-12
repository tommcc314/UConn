from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import time
length = 1024
content = b"This is the experiment script which tests how length of keys affect the time it takes to sign and verify"
h = SHA256.new(content)
for i in range(5):
    currtime = time.time()
    key = RSA.generate(length)
    sigsystem = pkcs1_15.new(key)
    signature = sigsystem.sign(h)
    sigsystem.verify(h, signature)
    print("Key of " + str(length) + " bits took " + str(time.time() - currtime) + " seconds.")
    length *= 2
    