# Nesting a dictionary inside a list!
# We have here a list that handle Two dictionary
travel_log = [
  
   {'Country':  "france" ,
    "visitd_city": ['paris','dijon','lile'],
    'total_number': 2 
   },
   
   {'Country' : "Germany" , 
    'visited_city': ['Berlin' , 'Humborg' , 'Munich'],
    'total_number':0 
   }
]

def new_travel_log(visited_country, cities_visited, time_visited):
  new_country = {} #new_dictionary
  new_country['Country'] = visited_country  #Key : Value
  new_country['visited_city'] = time_visited 
  new_country['total_number'] = cities_visited
  travel_log.append(new_country) # here we add new dic to List that handls many dictionary
  
new_travel_log('Russia', ["Mosco" , "Saint Paitersburg"] , 2)
print(travel_log)

def add_item_travel(visted_town, visited_cities , visited_times) :
  new_town = {}
  new_town['Country'] = visted_town
  new_town['visited_city'] = visited_cities 
  new_town['total_number'] = visited_times 
  travel_log.append(new_town)

add_item_travel('Marocco' , ['fes' ,'Ifran','casa'] , 3)

print(travel_log)

  
  
  