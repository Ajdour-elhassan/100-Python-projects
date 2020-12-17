items = [90,90,90,92]

total_score = 0
for score in items :
    total_score = total_score + score
print(f"total score is : {total_score}")
total = (items[1]) / (len(items))
print(total)
print(len(items))
print(sum(items))

#Heightest value :
heightest_score = 0
for score in items :
    if score > heightest_score :
        heightest_score = score
print(f'heightest score is {heightest_score}')
