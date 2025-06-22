import random
import string

char_values = string.ascii_letters + string.punctuation + string.digits

print("WELCOME TO SUSHIPR'S PASSWORD GENERATOR\n\nCAUTION: Enter the password length greater than 10 for Secure Passwords.\n")

try:                                                            # Use of Error Handling
    pass_len = int(input("Enter a number: "))
except:
    print("The user input is incorrect. Please enter a valid number.\n")    
    
password = ""

try:                                                            # Use of Error Handling
    for i in range(pass_len):
        password += random.choice(char_values)
    print(f"The random password generated is: {password}\n")    # Use of f string
except:
    print("PASSWORD NOT GENERATED.\n")

print("THANK YOU\n")    