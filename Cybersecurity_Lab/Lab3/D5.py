from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import MD5
BLOCKSIZE = 64
count = 0
h = MD5.new()
def MyChecksum(hexlist):
    summ=0
    carry=0
    for i in range(0,len(hexlist),2):
        summ+=(hexlist[i]<< 8)  + hexlist[i+1]
        carry=summ>>16
        summ=(summ & 0xffff)  + carry
    while( summ != (summ & 0xffff)):
        carry=summ>>16
        summ=summ & 0xffffffff  + carry
    summ^=0xffff 
    return summ
with open('./Q5files/R5.py' , 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        count = count + 1
        h.update(buf)
        buf = afile.read(BLOCKSIZE)
hf = h.digest()

with open('./Q5files/Encrypted5', 'rb') as file:
    iv = file.read(16)
    padvalue = file.read()
    cipher = AES.new(hf, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(padvalue), AES.block_size).decode()
print(plaintext)