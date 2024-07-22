from sha_256 import encrypter

def register_main(key):
    digest_key = encrypter(key)
    with open('.txts/main-key.txt', 'w') as f:
        f.write(str(digest_key))
        return True
    
    