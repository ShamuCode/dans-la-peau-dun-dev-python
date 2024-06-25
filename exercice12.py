import random

def game():
  nbmin = 1
  nbmax = int(input("Nombre max ? "))
  
  nombreCaché = random.randint(nbmin,nbmax)
  print("Min :",nbmin ,"- Max :", nbmax)
  print("")

  nbessai = 1
  essai = int(input("Essai ? "))

  while essai != nombreCaché:
    if nbessai >= 10:
       print("Tu as essayé trop de fois ! Perdu")
       return
    if essai < nombreCaché:
        print(essai, "est trop petit")
    else:
        print(essai, "est trop grand")
    nbessai = nbessai + 1
    print("")    
    essai = int(input("Essai ? "))

  print("Gagné :", nombreCaché)
  print("Nombre de coups :", nbessai)
  print("")
  
  
j = 0

while j != 1:
    game()  
