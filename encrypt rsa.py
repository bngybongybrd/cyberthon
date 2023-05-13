from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

message = b'You can attack now!'
key = RSA.importKey(open('pub1.pem').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)
print(ciphertext)

key = RSA.importKey(open('private_key.pem').read())
cipher = PKCS1_OAEP.new(key)
message = cipher.decrypt(ciphertext)