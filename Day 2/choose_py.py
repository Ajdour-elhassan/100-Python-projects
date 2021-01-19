import random

names_string = str(input('give everybody names with sepearted Comma? : '))

names = names_string.split(", ")

#we add an object to split_string
names.append("the weiter")

num_len = (len(names))

print(num_len)

random_choice = random.randint(0, num_len - 1)

person_who_pay = names[random_choice]

print(f" the person is going to pay the meal is : {person_who_pay}")