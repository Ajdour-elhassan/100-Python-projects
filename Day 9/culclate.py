# calulator program!

#Add
def add(n1 , n2) :
  return n1 + n2

#Subtract
def subtract(n1 ,n2) :
  return n1 - n2

#Multipy
def multipy(n1 ,n2) :
  return n1 * n2

#Divide
def divid(n1 ,n2) :
  return n1 / n2

# operations 

operations  = {
   
  '+' : add ,
  '-' : subtract ,
  '*' : multipy ,
  '/' : divid
  
}



def calulator() :
  is_finished = True  
  num1 =  float(input("enter a first number :  "))
  for char in operations :
    print(char)
  while is_finished :
    opartions_symoble = input("choose which operation you wanna do! :  ")
      
    num2 =  float(input("enter a Second number :  "))
      
      #we store an opertion function total_function!
    total_function = operations[opartions_symoble]   #Opertion takes a key! 
      
       #The final Results!
    answer = total_function(num1, num2)          #opertion taks a Value!

    print(f'{num1} {opartions_symoble} {num2} = {answer}')
  
    should_continues = input(f'would you like to continues calucluting with {answer} ? type yes or exite type no! start agin type agin! :   ')
  
    if should_continues == 'yes' :
      num1 = answer
      print("let's continue!")
    elif should_continues == 'again' :
        calulator() #Reucursion
    else :
      is_finished = False
        
calulator()
 
#Add   num3
# opartions_symoble = input("choose which operation you wanna do! :  ")
# num3 =  int(input("enter a Third number :  "))
# total_function = operations[opartions_symoble] 
# second_results = total_function(first_results, num3) 
# print(f'{num3} {opartions_symoble} {first_results} = {second_results}')   