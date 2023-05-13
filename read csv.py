from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import csv
import base64

encrypted = []
with open('encrypted_msgs.csv', 'r') as file:
    csvreader = csv.reader(file)
    
    next(csvreader)

    for row in csvreader:
        encrypted.append(row)



'''for i in range(len(encrypted)):
    encrypted[i][1] = encrypted[i][1][:-1]'''

# Convert base64 to bytes
for i in range(len(encrypted)):
    encrypted[i][1] = base64.b64decode(encrypted[i][1])

print(encrypted)

for i in range(len(encrypted)):
    
    private_key = RSA.importKey(open('private_key.pem').read())
    cipher = PKCS1_OAEP.new(private_key)
    '''try:
        message = cipher.decrypt(encrypted[i][1])
        encrypted[i][1] = message
        print(i)
    except ValueError:
        pass'''
    message = cipher.decrypt(encrypted[i][1])
    encrypted[i][1] = message
    # decrypted = RSA.decrypt(encrypted[i][1], private_key)
    
    




