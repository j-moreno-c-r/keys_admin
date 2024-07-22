import gnupg

# Initialize the gnupg object
gpg = gnupg.GPG()

def encrypt_message(message, fingerprint_file):
    # Import the public key
    with open(fingerprint_file) as f:
        key_fingerprint = f.read()
    # Encrypt the message
    encrypted_data = gpg.encrypt(message,key_fingerprint)
    return encrypted_data

def decrypt_message(encrypted_data, private_key_file):
    # Import the private key
    with open(private_key_file) as f:
        private_key = f.read()
    gpg.import_keys(private_key)

    # Decrypt the message
    decrypted_data = gpg.decrypt(str(encrypted_data))
    return decrypted_data


