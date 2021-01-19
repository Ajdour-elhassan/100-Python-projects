#Dectionries
Quiz_dictionary = {
    'Q1': 'where do you live',
    'Q2': 'where do you work',
    'Q3': 'where do you sleep',
}

#print(Quiz_dictionary['Q1'])
#Adding items to dectionary
Quiz_dictionary['Q4'] = "What's the your favourite color ?"
#print(Quiz_dictionary['Q4'])

#Create an empty dic 
empty_dictionary = {}
empty_dictionary['S2'] = " S2 is validated"
#print(empty_dictionary['S2'])

#Wipe a dictionary
#Quiz_dictionary = {}
#print(Quiz_dictionary)

# Edit a dictionary 
Quiz_dictionary['Q1'] = "What's your favourite team ?"

#print(Quiz_dictionary['Q1'])

# Loop through dictionary 

for key in Quiz_dictionary :
  #print(key)
  print(Quiz_dictionary[key])





