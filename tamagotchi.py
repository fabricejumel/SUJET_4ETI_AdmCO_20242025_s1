import random
import sys

# Dictionnaire des états du Tamagotchi
tamagotchi = {
    "bonheur": 50,  # Échelle de 0 à 100
    "energie": 50,   # Échelle de 0 à 100
    "capital_biologique": 100  # Capital biologique initial
}

# ASCII art pour chaque action
ascii_art_actions = {
    "nourrir": """
   ________
  /        \\
 |  ( ^_^)  |   <- Tamagotchi content après avoir mangé
 |   /|\\    |
  \\________/
    """,
    "jouer": """
   ________
  /        \\
 |  (o_o)  |   <- Tamagotchi heureux après avoir joué
 |   /|\\    |
  \\________/
    """,
    "ignorer": """
   ________
  /        \\
 |  (T_T)  |   <- Tamagotchi triste après avoir été ignoré
 |   /|\\    |
  \\________/
    """
}

# Fonction pour gérer l'impact des actions et le vieillissement
def action_choisie(action):
    global tamagotchi

    if action == "nourrir":
        tamagotchi["energie"] += 20
        tamagotchi["bonheur"] += 5
        vieillissement(1.5)  # Manger trop accélère le vieillissement
        print(f"\nVous avez nourri votre Tamagotchi !")
        print(ascii_art_actions["nourrir"])
    elif action == "jouer":
        tamagotchi["energie"] -= 30
        tamagotchi["bonheur"] += 20
        vieillissement(1.3)  # Jouer trop accélère le vieillissement
        print(f"\nVous avez joué avec votre Tamagotchi !")
        print(ascii_art_actions["jouer"])
    elif action == "ignorer":
        tamagotchi["energie"] -= 10
        tamagotchi["bonheur"] -= 20
        vieillissement(1.0)  # Ignorer a un effet neutre
        print(f"\nVous avez ignoré votre Tamagotchi...")
        print(ascii_art_actions["ignorer"])

# Fonction pour gérer le vieillissement du Tamagotchi et l'impact sur le capital biologique
def vieillissement(facteur):
    global tamagotchi

    # Diminution du capital biologique
    vieillissement_capital = random.uniform(0.5, 1.0) * facteur
    tamagotchi["capital_biologique"] -= vieillissement_capital

# Boucle du jeu avec un compteur d'actions
compteur_actions = 0  # Compteur des actions effectuées

while tamagotchi["energie"] > 0 and tamagotchi["bonheur"] > 0 and tamagotchi["capital_biologique"] > 0:
    # Affichage des choix d'actions
    print("\nChoisissez une action :")
    print("1. Nourrir")
    print("2. Jouer")
    print("3. Ignorer")

    # Forcer le rafraîchissement de l'affichage dans le terminal
    sys.stdout.flush()

    # Demander le choix à l'utilisateur
    choix = input("Entrez votre choix (1, 2, 3) : ")
    if choix == "":
        choix = "3"  # Par défaut, choisir 3 si entrée vide

    if choix == "1":
        action_choisie("nourrir")
    elif choix == "2":
        action_choisie("jouer")
    elif choix == "3":
        action_choisie("ignorer")
    else:
        print("Choix invalide. Essayez encore.")

    # Incrémenter le compteur d'actions
    compteur_actions += 1

    # Vérifier si le Tamagotchi est mort
    if tamagotchi["energie"] >= 150 or tamagotchi["bonheur"] >=150 or tamagotchi["energie"] <= 0 or tamagotchi["bonheur"] <= 0 or tamagotchi["capital_biologique"] <= 0:
        print("\nLe Tamagotchi est fatigué, malheureux, son capital biologique est épuisé. ou truc plus bizarre,  Le jeu est terminé.")
        break
 

    # Une pause avant la prochaine itération pour simuler le temps
    input("\nAppuyez sur Entrée pour continuer...\n")

# Fin du jeu : Tamagotchi meurt de vieillesse après un certain nombre d'actions
print(f"\nLe Tamagotchi est mort après {compteur_actions} actions. Le jeu est terminé.")

