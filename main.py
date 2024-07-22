import getpass 
from verificate_mainkey import first_verify
from free_acess import free

if __name__ == '__main__':
    print("Hello litle Cypherpunk")
    print(":-" *30)
    masterkey = getpass.getpass("Unlock \n -->")
    
    if first_verify(masterkey): 
        print("logged ✅")
        free()

    else:
        print("Wrong password 🖕")