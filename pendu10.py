import random

def choisirNiveau():
    mots = {
        "1": ["selene", "orbite", "cosmos","etoile","astres", "comete"],
        "2": ["Astronaute","telescope","galaxique","asteroides","exploration","telemetrie"],
        "3": ["Astrophysicien","teledetection","cosmogonie","telescopique","cosmonaute","telemedecine"]
    }
    red = "\033[31m"
    yellow="\033[93m"
    blue = "\033[94m"
    reset = "\033[0m"
    green = "\033[92m"
    niveau = input("""Choisissez votre niveau :
    "\033[93m1 = Niveau facile    : 5 à 6 lettres 
    "\033[92m2 = Niveau moyen     : 7 à 10 lettres  
    "\033[31m3 = Niveau difficile : 12 à 26 lettres"\033[0m
    Quel niveau ?""")
 
    if niveau == "1" or niveau == "2" or niveau == "3":
        mot_mystere = random.choice(mots[niveau])
        return mot_mystere
    else:
        print("Sélection invalide! Veuillez entrer 1, 2 ou 3!")
        return choisirNiveau()
   
def cadre():
    red = "\033[31m"
    blue = "\033[94m"
    reset = "\033[0m"
    green = "\033[92m"
 
    print(blue+"+---------------------------------+"+reset)
    print(red+"| BIENVENUE DANS LE JEU DU PENDU! |"+reset)
    print(blue+"+---------------------------------+"+reset)
    print("")
 
def bonhomme_pendu(tentatives):
    max_tentatives = 7
    etapes = ["""
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    
        |
        |
        |
        |
    ------------
 """, """
        ------
        |    |
        |    O
        |    
        |    
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |  
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
      """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   //
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |   \|
        |    |
        |   //
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |   \|/
        |    |
        |   //
        |
    ------------
    """]
    return etapes[max_tentatives - tentatives]

def continuer():
    rejouer = input("Voulez-vous rejouer ? (o/n) : ")
    if rejouer.lower() == 'n':
        print("Merci pour votre participation :-)")
        return False
    elif rejouer.lower() == "o":
        return True
    else:
        print("Lettre invalide! Veuillez entrer o ou n!")
        return continuer()

continuer_partie = True
while continuer_partie:
    cadre()
    mot_mystere= choisirNiveau()
   
    if mot_mystere:
        tentatives = 7
        affichage = "_" * len(mot_mystere)
        lettres_trouvees = ""
        lettres_erronees = set()
      
        while tentatives > 0:
            print("\nMot à deviner :", affichage)
            print("Tentatives restantes :", tentatives)
            print("Lettres incorrectes :", ", ".join(lettres_erronees))
            print("")
            proposition = input("Votre proposition : ")[0:1].lower()
          
            if len(proposition)!= 1 or not proposition.isalpha():
                print("Veuillez entrer une seule lettre valide.")
                #proposition = input("Votre proposition : ")[0:1].lower()
            elif proposition in lettres_erronees:
                print(f"Vous avez déjà proposé la lettre '{proposition}'.")
            elif proposition in mot_mystere:
                lettres_trouvees += proposition
                print("-> Bien vu!")
            else:
                lettres_erronees.add(proposition)
                tentatives -=  1
                print("-> Raté\n")
                print(bonhomme_pendu(tentatives))
             
            affichage = ""
            for lettre in mot_mystere:
                if lettre in lettres_trouvees:
                    affichage += lettre
                else:
                    affichage += "_"
   
            if "_" not in affichage:
                print(f"Gagné ! Le mot à trouver était {mot_mystere}")
                break
            elif tentatives == 0:
                print(f"C'est perdu ! Le mot était : {mot_mystere}")
   
    continuer_partie=continuer()
            