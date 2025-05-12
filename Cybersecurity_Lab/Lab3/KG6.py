from Crypto.PublicKey import RSA
def keygenerate():

    key = RSA.generate(2048)
    privatekey = key.export_key('PEM').decode()
    # privatekey.replace("-----BEGIN RSA PRIVATE KEY-----\n", "")
    # privatekey.replace("-----END RSA PRIVATE KEY-----", "")
    publickey = key.public_key().export_key('PEM').decode()
    # publickey.replace("-----BEGIN PUBLIC KEY-----\n", "")
    # publickey.replace("-----END PUBLIC KEY-----", "")
    with open("d.key", "w") as file:
        file.write(privatekey)
    with open("e.key", "w") as file:
        file.write(publickey)
if __name__ == "__main__":
    keygenerate()