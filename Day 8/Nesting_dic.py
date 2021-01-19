
# Nesting Dectionary in a Dectionary!

travel_city = {'France': {"visitd_city": ['paris','dijon','lile'], 
                       'total_number':2 },
            'Germany' : {'visited_city': ['Berlin' , 'Humborg' , 'Munich'], 
                         'total_number':0}
}

print(travel_city['France'])

# Nesting a dictionary inside a list!

travel_log = [
  
   {'Country':  "france" ,
    "visitd_city": ['paris','dijon','lile'],
    'total_number': 2 },
   
   {'Country' : "Germany" , 
    'visited_city': ['Berlin' , 'Humborg' , 'Munich'],
    'total_number':0}
]
