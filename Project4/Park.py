import sys


print("What is the age of the first rider?")
rider1_age = int(input())
print()
print("What is the height of the first rider?")
rider1_height = int(input())
print()
if(rider1_height < 36):
    print("Sorry, you are not eligible to ride.")
    sys.exit()


loop = True
while(loop):
    print("Is there a second rider? (Y/N)")
    answer1 = input().upper()
    if(answer1 == "Y"):
        print("What is the age of the second rider?")
        rider2_age = int(input())
        if(rider2_age < 18 and rider1_age < 18):
            print("Sorry, you are not eligible to ride.")
            sys.exit()
        print()
        print("What is the height of the second rider?")
        rider2_height = int(input())
        if(rider2_height < 36):
            print("Sorry, the second rider is not eligible to ride.")
            print("Will the first rider ride alone?(Y/N)")
            answer2 = input().upper()
            if(answer2 == "Y"):
                print("Welcome! Please enjoy the ride.")
            else:
                print("Sorry, maybe next time.")
                sys.exit()         
        loop = False
    elif(answer1 == "N"):
        loop = False
    else:
        print("Please enter Y or N")
        loop = True
    if(loop == False):
        break
print()
print("You are both eligible! Welcome to the ride.! Please enjoy!")
sys.exit()


    