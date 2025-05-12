from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import os
key = RSA.import_key(open('./Q3pk.pem').read())
files = [f for f in os.listdir('./Q3files') if not f.endswith('.sign')]
for file in files:
    with open('./Q3files/' + file, 'rb') as f:
        content = f.read()
    h = SHA256.new(content)
    with open('./Q3files/' + file + '.sign', 'rb') as f:
        try:
            signature = pkcs1_15.new(key).verify(h, f.read())
            print(file)
        except:
            pass