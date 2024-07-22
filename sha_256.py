import hashlib
def encrypter(prhase):
          result = hashlib.sha256(prhase.encode()).hexdigest()
          print(result)
          return result
