#Creating a Kaun Banega Crorepati Game (KBC)

print("Welcome to KBC!\n")                       

ques1 = "Who was the first Mughal Emperor?"

ques2 = "Who is the author of the Sherlock Holmes franchise?"

ques3 = "Who is reverred (called respectfully) as Tathagata?"

ques4 = "Who acquired the title 'Piyadasi'?"

ques5 = "Which city in present was the capital of the Cholas?"

opt_ques1 = ["Humayun" , "Akbar The Great" , "Babur" , "Timur"]
opt_ques2 = ["Conan Doyle" , "J. K. Rowling" , "William Shakespeare" , "Rudyard Kipling"]
opt_ques3 = ["Muni Subrat" , "The Buddha" , "Adinath" , "Mahavira Swami"]
opt_ques4 = ["Ashoka The Great" , "Bimbisara" , "Pushyamitra" , "Sushruta"]
opt_ques5 = ["Thanjavur" , "Madurai" , "Chennai" , "Mysore"]

ques = [ques1 , ques2 , ques3 , ques4 , ques5]

print("Let's begin our game. 'Kaun Banega Crorepati!'")

for i in range(1):
    print(ques1)
    print(f"A. {opt_ques1[0]}\nB. {opt_ques1[1]}\nC. {opt_ques1[2]}\nD. {opt_ques1[3]}\n")
    x= int(input("Enter the correct option (1,2,3,4): "))
    if (x == 1):
        print("Wrong option! You lose.\n")
        break
    elif (x == 2):
        print("Wrong option! You lose.\n")
        break
    elif (x == 3):
        print("Correct option! You won ₹10,000.\n")
    elif (x == 4):
        print("Wrong option! You lose.\n") 
        break
    else:
        print("ERROR 101")
        break
    print(ques2)
    print(f"A. {opt_ques2[0]}\nB. {opt_ques2[1]}\nC. {opt_ques2[2]}\nD. {opt_ques2[3]}\n")
    x= int(input("Enter the correct option (1,2,3,4): "))
    if (x == 1):
        print("Correct option! You won ₹1,00,000.\n")
    elif (x == 2):
        print("Wrong option! You lose.\n")
        break
    elif (x == 3):
        print("Wrong option! You lose.\n")
        break
    elif (x == 4):
        print("Wrong option! You lose.\n") 
        break
    else:
        print("ERROR 101")
        break
    print(ques3)
    print(f"A. {opt_ques3[0]}\nB. {opt_ques3[1]}\nC. {opt_ques3[2]}\nD. {opt_ques3[3]}\n")
    x= int(input("Enter the correct option (1,2,3,4): "))
    if (x == 1):
        print("Wrong option! You lose.\n")
        break
    elif (x == 2):
        print("Correct option! You won ₹10,00,000.\n")
    elif (x == 3):
        print("Wrong option! You lose.\n")
        break
    elif (x == 4):
        print("Wrong option! You lose.\n") 
        break
    else:
        print("ERROR 101")
        break
    print(ques4)
    print(f"A. {opt_ques4[0]}\nB. {opt_ques4[1]}\nC. {opt_ques4[2]}\nD. {opt_ques4[3]}\n")
    x= int(input("Enter the correct option (1,2,3,4): "))
    if (x == 1):
        print("Correct option! You won ₹1 Crore.\n")
    elif (x == 2):
        print("Wrong option! You lose.\n")
        break
    elif (x == 3):
        print("Wrong option! You lose.\n")
        break
    elif (x == 4):
        print("Wrong option! You lose.\n") 
        break
    else:
        print("ERROR 101")   
        break
    print(ques5)
    print(f"A. {opt_ques5[0]}\nB. {opt_ques5[1]}\nC. {opt_ques5[2]}\nD. {opt_ques5[3]}\n")
    x= int(input("Enter the correct option (1,2,3,4): "))
    if (x == 1):
        print("Correct option! You won ₹7 Crore.\n")
        break
    elif (x == 2):
        print("Wrong option! You lose.\n")
        break
    elif (x == 3):
        print("")
    elif (x == 4):
        print("Wrong option! You lose.\n") 
        break
    else:
        print("ERROR 101")
        break
    
print("GAME ENDED")    