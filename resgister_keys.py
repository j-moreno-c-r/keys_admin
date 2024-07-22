from encrypt_decrypt import encrypt_message


pubkey = "keys/public_key.asc"

def register_newkey(user, key):
    encrypted_key =  encrypt_message(str(key), pubkey)
    geral_dict = {}
    geral_dict[f"{user}"] = encrypted_key
    try:
        with open(".txts/encrypted_keys.txt", "a") as keys_file:
            keys_file.write(str(geral_dict))
            result = print("sucess ✅")
    except Exception as error:
        result =  print(f"error {error} 🤬")
    return result