import os
import hashlib
with open('./Q2hash.txt', 'r') as file:
    target = file.read()
files = [f for f in os.listdir('./Q2files')]
for file in files:
    with open('./Q2files/' + file, 'rb') as f:
        contents = f.read()
    # print(hashlib.sha256(contents).hexdigest())
    if hashlib.sha256(contents).hexdigest() == target:
        print(file)
