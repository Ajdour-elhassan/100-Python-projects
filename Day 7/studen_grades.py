students_scores = {
  'bob' : 78 ,
  'Anna' : 90 ,
  'Max' : 87 ,
  'Jhon' : 68 ,
}

#print(students_scores['bob'])
students_grades = {}

for key in students_scores :
  score = students_scores[key]
  if score > 90 :
    students_grades[key] = "Outstanding"
  elif score > 80 :
    students_grades[key] = "Excceds Expectations"
  elif score > 70 :
    students_grades[key] = "Acceptanle!"
  else :
    students_grades[key] = "Failed"
    
print(students_grades)
      