#import math

#test_height = int(input('height is : '))
#test_width = int(input('width is : '))
#coverage = 5

#def calculate(height, width, cover):
    #area = width * height
    #num_of_cans = math.ceil(area / cover)
    #print(f'you need {num_of_cans}')

#calculate(height=test_height, width=test_width, cover=coverage)

n = int(input("enter a number :  "))

def prime_checker(number) :
    pass
prime_checker(number=n)

def prime_checker(number) :
    is_prime = True
    for i in range(2, number) :
        if number % i == 0 :
            is_prime = False
    if is_prime  :
        print("it's a prime number")
    else :
        print('is not a prime number')

prime_checker(number=n)

