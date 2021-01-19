# Blind Auction Pogram 
from reprlib import clear

bids = {}
bidding_finished = False

def find_hightest_price(biding_record) :
    highest_price = 0 
    winner = ""
    for char in biding_record :
      if biding_record[char] > highest_price :
        highest_price = biding_record[char] 
        winner = char
    print(f'thse winner is {winner} with a bid of a {highest_price} $')

#find_hightest_price(bids)

while not bidding_finished :
  name = input('enter your name?  ')
  price = int(input('enter a Bid ? $'))
  bids[name] = price  # Key : value => to 
  should_continues = input("Are there any bid ? ")
  if should_continues == 'no' :
    bidding_finished = False
    find_hightest_price(bids)
  elif should_continues =='yes' :
    clear()
    #print('no')



    
  
  
  