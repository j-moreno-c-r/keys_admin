import getpass 
from random_password import generate_password
from resgister_keys import register_newkey
from register_mainkey import register_main
def free():
    choice = ' '
    while choice != 'e':
        choice = input("(a)to see the possble keys \n(b) to register a new key \n(c)to generate a strong random key \n(d)to update the master key \n(e)To exit\n --->")
        
        
        if choice == 'b':
            entrace_username = input("type your username or name of the service🙍: ")
            print(":-"*30)
            entrace_key = getpass.getpass("type the key 🔑: ")
            register_newkey(entrace_username, entrace_key)
        if choice == 'c':
            print(":-"*30)
            print("Lets made a fucking strong pasword!!!")
            input_size_words= int(input("How long do you want the size of the sub-words ? "))
            print(":-"*30)
            input_number_words = int(input("How many sub-words do you want in your password? "))
            print(":-"*30)
            input_spacer_text = input("Enter the spacer text!(One caracter)")
            print(":-"*30)

            try:
                print(generate_password(input_number_words, input_size_words, input_spacer_text))
            except ValueError as e:
                print(f"Error: {e}")
            print(":-"*30)
        if choice == 'd':
                key = input("Enter your new mainkey : ")
                try:
                    register_main(key)
                    print("successfully changed your mainkey 🗝️ ✅")
                except:
                    print("something went wrong 🚨 💔")

    