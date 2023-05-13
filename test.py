from Crypto.PublicKey import RSA

# Read the contents of the PEM-encoded private key file
with open('test_private_key.pem', 'r') as f:
    private_key_data = f.read()

# Create a private key object from the key data
private_key = RSA.import_key(private_key_data)

'''
# Extract the modulus and private exponent from the private key
n = private_key.n
d = private_key.d

# Compute the public exponent (usually 65537)
e = 65537

# Create a new public key object
public_key = RSA.construct((n, e))

# Print the public key
print(public_key.export_key())'''

# Extract the public key from the private key
public_key = private_key.publickey()

# Export the public key to a PEM-encoded string
public_key_pem = public_key.export_key()

# Write the public key to a file named 'public_key.pem'
with open('new_public_key.pem', 'wb') as f:
    f.write(public_key_pem)