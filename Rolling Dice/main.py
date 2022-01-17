import random

print("Welcome to Rolling Dice Game!")

user_answer = input("Want to roll a dice ? (y / n):  ").lower()

while(user_answer == "y"):
    num = random.randint(1, 6)
    if (num == 1):
        print("----------")
        print("          ")
        print("    0     ")
        print("          ")
        print("----------")
        
    elif (num == 2):
        print("----------")
        print("          ")
        print("    0 0   ")
        print("          ")
        print("----------")
        
    elif (num == 3):
        print("----------")
        print("          ")
        print("  0 0 0   ")
        print("          ")
        print("----------")
        
    elif (num == 4):
        print("----------")
        print("          ")
        print("   0 0 0  ")
        print("     0    ")
        print("----------")
        
    elif (num == 5):
        print("----------")
        print("          ")
        print("   0 0 0  ")
        print("    0 0   ")
        print("----------")
        
    else:
        print("----------")
        print("          ")
        print("   0 0 0  ")
        print("   0 0 0  ")
        print("----------")
    
    user_answer = input("Want to roll a dice ? (y / n):  ").lower()
    
    if( user_answer == 'n'):
        exit()