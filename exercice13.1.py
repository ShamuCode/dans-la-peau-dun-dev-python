import random
from termcolor import colored,cprint

game_end = False

player = {"name": input("Quel est ton nom ? "), "level": 1, "attack": 2, "defense": 1, "pv": 10}
robot = {"name": "Bot", "level": 1, "attack": random.randint(0, 5), "defense": random.randint(0, 5), "pv": random.randint(5, 20)}
print(robot["defense"])
print(robot["pv"])

print("\033[1;31mPLAYER ONE\033[0m")
for cle, valeur in player.items():
    print(f"{cle}: {valeur}")

print("")

print("\033[1;32mPLAYER TWO\033[0m")
for cle, valeur in robot.items():
    print(f"{cle}: {valeur}")

def round():
    #robo
    print("")

print("")
print("")

def attack_robot(damage):
    print("\033[1;31m" + player["name"], "attaque", robot["name"], "avec", damage, "dégats." + "\033[0m")
    print("Joueur 2 ; Défense :", robot["defense"], "Vie :", robot["pv"])
    while damage != 0:
        if robot["defense"] <= 0:
            if robot["pv"] <= 0:
                for i in range(3):
                    print("")
                print("Partie terminée, défaite du", robot["name"])
                exit(1)
                game_end = True
                return 0
            robot["pv"] = robot["pv"] - 1
        if robot["defense"] > 0:
            robot["defense"] = robot["defense"] - 1
        
        damage = damage - 1
    print("Joueur 2 ; Défense :", robot["defense"], "Vie :", robot["pv"])
    print("")

def attack_player(damage):
    print("\033[32m" + robot["name"] + " attaque " + player["name"] + " avec " + str(damage) + " dégats." + "\033[0m")
    print("Joueur 1 ; Défense :", player["defense"], "Vie :", player["pv"])
    while damage != 0:
        """print(damage)
        print(player["defense"])
        print(player["pv"])"""
       
        if player["defense"] <= 0:
            if player["pv"] <= 0:
                for i in range(3):
                    print("")
                print("Partie terminée, défaite de", player["name"])
                exit(1)
                game_end = True
                return
            player["pv"] = player["pv"] - 1
        if player["defense"] > 0:
            player["defense"] = player["defense"] - 1
        damage -= 1
    print("Joueur 1 ; Défense :", player["defense"], "Vie :", player["pv"])
    print("")

while game_end != True :
    attack_robot(player["attack"])
    attack_player(robot["attack"])

    """while player["pv"] != 0:
        while robot["pv"] != 0:
            
    while player["pv"] != 0:
        while robot["pv"] != 0:"""
            
