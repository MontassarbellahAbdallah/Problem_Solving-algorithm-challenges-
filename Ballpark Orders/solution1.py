taxe = 0.07
print("choisir au max 4 commande")
M = input()
x = M.split()
for i in range(len(x)):
  if x[i] == "Cheeseburger":
    Cheeseburger = 10.0
    x[i] = Cheeseburger
  elif x[i] == "Pizza":
    Pizza=6.0
    x[i] = Pizza
  elif x[i] == "Nachos":
    Nachos=6.0
    x[i] = Nachos
  elif x[i] == "Water":
    Water=4.0
    x[i] = Water
  elif x[i] == "Coke":
    Coke=5.0
    x[i] = Coke
  elif x[3] != "Water" or x[3] != "Cheeseburger" or x[3] != "Pizza" or x[3] != "Nachos" or x[3] != "Coke":
    x[3] = "Coke"
    Coke = 5.0
    x[3] = Coke
  else:
    print("erreur")

somme= float(x[0]+x[1]+x[2]+x[3])
print("la somme totale =",somme)
staxe=somme*taxe
somme_taxe=somme+staxe
print("la somme totale avec taxe =",somme_taxe)
#Pizza Cheeseburger Water Popcorn
