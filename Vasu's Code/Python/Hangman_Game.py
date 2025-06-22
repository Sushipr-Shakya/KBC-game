import random

print("WELCOME TO THE HANGMAN GAME\n")

secret_words = ["APPLE" , "AVOCADO" , "BANANA" , "ORANGE" , "MANGO" , "PAPAYA" , "GRAPES" , "PEAR" , "LITCHI" , "APRICOT" , "BLACKBERRY" , "CHERRY" , "DRAGONFRUIT" , "FIG" , "GUAVA" , "WATERMELON" , "PINEAPPLE" , "POMEGRANATE" , "STRAWBERRY" , "KIWI"]

x = random.choice(secret_words)

user_name = input("Enter your name: ").upper()
print()

print("TARGET: Guess the random fruit name.\nEnter the alphabets one by one.\n\nTo make it easy and user interactive, endless guesses are enabled.\n")
print("BEWARE: It's not going to be easy unless you have a very nice knowledge of fruits :)\n")

exposed_alpha = ["_"] * len(x)

while "_" in exposed_alpha :
    alpha = input("Guess the alphabet: ").upper()
    if (alpha in x):
        for i in range(len(x)):
            if (x[i] == alpha) :
                exposed_alpha[i] = alpha   
    print(" ".join(exposed_alpha))     
    print()                   

print(F"\nBINGO. {user_name} YOU WON THE GAME.\n\nGAME ENDED\n\nTHANK YOU FOR PLAYING\n")