import random

class Joueur:
    def __init__(self, nom, niveau):
        self.nom = nom
        self.niveau = niveau
        self.attaque = 2
        self.resistance = 1
        self.points_de_vie = 10

class Robot:
    def __init__(self, nom):
        self.nom = nom
        self.niveau = random.randint(1, 10)
        self.attaque = random.randint(0, 5)
        self.resistance = random.randint(0, 5)
        self.points_de_vie = random.randint(5, 20)

def combat(joueur, robot):
    while joueur.points_de_vie > 0 and robot.points_de_vie > 0:
        joueur_attaque = joueur.attaque - robot.resistance
        if joueur_attaque <= 0:
            print(f"{joueur.nom} attaque {robot.nom}, mais ne lui inflige aucun dégât.")
        else:
            robot.points_de_vie -= joueur_attaque
            print(f"{joueur.nom} attaque {robot.nom} et lui inflige {joueur_attaque} points de dégât.")
            if robot.points_de_vie <= 0:
                print(f"Bravo {joueur.nom}, vous avez vaincu {robot.nom} !")
                break

        robot_attaque = robot.attaque - joueur.resistance
        if robot_attaque <= 0:
            print(f"{robot.nom} attaque {joueur.nom}, mais ne lui inflige aucun dégât.")
        else:
            joueur.points_de_vie -= robot_attaque
            print(f"{robot.nom} attaque {joueur.nom} et lui inflige {robot_attaque} points de dégât.")
            if joueur.points_de_vie <= 0:
                print(f"{robot.nom} a vaincu {joueur.nom}.")
                break

# Exemple d'utilisation
joueur1 = Joueur("PLAYER", 1)
robot1 = Robot("ROBOT")
combat(joueur1, robot1)
