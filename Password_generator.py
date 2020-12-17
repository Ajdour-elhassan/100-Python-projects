# Password Generator Programmer!
import random
alphabet = ['a' , 'b' , 'c' , 'd', 'e' , 'f']
number = ['1', '2' , '3' , '4', '5', '6', '7', '8', '9', '10', '11']
symbole = ['%' , '&' , '@' , 'é' , '°' , '}' , '+']
name = str(input("Enter your name : "))
print(f"welcome {name} to Password generator")
nr_alphabet = int(input(f"How much of alphabet ? \n"))
nr_number = int(input(f"How much of number ? \n"))
nr_symbole  = int(input(f"How much of symbole ? \n"))

list_password = []

for char in range(1, nr_alphabet + 1) :
    list_password += random.choice(alphabet)

for char in range(1, nr_number + 1 ) :
    list_password += random.choice(number)

for char in range(1, nr_symbole + 1) :
    list_password += random.choice(symbole)

print(list_password)
random.shuffle(list_password)
print(list_password)

password = ""
for char in list_password :
    password += char
print(f"final password is ;  {password}")






