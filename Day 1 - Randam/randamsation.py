import random
#print(random_number between (3-10)

choose_number = int(input("enter a number  : "))
rand_number = random.randint(3,10)
#print(rand_number)
if rand_number == choose_number :
    print("you wine")
else :
    print("you lose")

print(f"the winner number is {rand_number}")
print(f"th number you choose is {choose_number}")

#love_score = random.randint(0, 100)
#print(f"love score is {love_score}")