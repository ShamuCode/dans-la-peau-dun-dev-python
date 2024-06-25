prenom_nom = "Roberto Dupont"
with open("prenom_nom.txt", "w") as fichier:
    fichier.write(prenom_nom)

with open("prenom_nom.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)
