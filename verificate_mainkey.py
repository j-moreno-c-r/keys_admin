from sha_256 import encrypter
def first_verify(entrace):
    main_key= open(r".txts/main-key.txt").read()
    hash_entrace = encrypter(entrace)
    if hash_entrace == main_key:
        return True
    else: 
        return False