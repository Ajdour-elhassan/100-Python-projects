#Function With Output


def example_formate(name , profession) :
  
  if name == "" and profession == "" :
    return 'you did not match input value!'
  
  formated_name = profession.title()
  formated_age = profession.title()
  return f'my name is {formated_name} , my pefession is {formated_age}'
  
formated_string = example_formate('hassan' , 'software dev')

print(formated_string)

