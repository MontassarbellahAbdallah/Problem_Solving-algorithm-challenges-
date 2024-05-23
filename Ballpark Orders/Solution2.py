ordr_price={"Nachos":6.00,"Pizza":6.00,"Cheeseburger":10.00,"Water":4.00,"Coke":5.00}

ordr=input().split(" ") 
prc=0.00

for j in ordr:
    if j in ordr_price:
        prc+= ordr_price[j]
    else:
        prc+= ordr_price["Coke"] 
total_prc=prc+prc*7/100 
print(total_prc )  
#Pizza Cheeseburger Water Popcorn