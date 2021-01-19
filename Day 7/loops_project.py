students_height = input("enter a list of number : ").split()
for n in range(0, len(students_height)) :
    students_height[n] = int(students_height[n])
print(students_height)
#print(sum(students_height))

total_height = 0
for height in students_height :
    total_height += height
    print(total_height)
#write your code
#total_height = sum(students_height)
#number_of_students = len(students_height)
#overage_result = round(number_of_students / number_of_students)
#print(overage_result)