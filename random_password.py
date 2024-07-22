import random 
import string 

def generate_password(number_of_words,size_of_words,text_spacer):
    password = ""
    word = ""
    word_size = " " * size_of_words
    keyboard = string.ascii_lowercase + string.ascii_uppercase +  string.digits + string.punctuation
    digits_password  = number_of_words * size_of_words
    total_digits = digits_password + number_of_words
    while len(password) != total_digits:
        if len(word) < size_of_words:
                for i in word_size:
                    i = random.choice(keyboard)
                word +=  i 
        elif len(word) == size_of_words:
            password += word + text_spacer
            word = ""
           
    return password


