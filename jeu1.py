import random

# Introduction de l'aventure
print("========================================")
print("Bienvenue dans cette aventure textuelle !")
print("========================================\n")

# 1ère entrée utilisateur : choix du chemin à la bifurcation
chemin = input("Vous arrivez à une bifurcation dans la forêt. Choisissez votre chemin ('gauche' ou 'droite'): ").lower()

if chemin == "gauche":
    print("\nVous avez choisi le chemin de gauche, bordé par de vieux arbres majestueux.")
    
    # 2ème entrée utilisateur : décision à la rivière
    decision_riviere = input("Au détour du chemin, vous arrivez à une rivière scintillante. Voulez-vous 'traverser' en nageant ou 'suivre' la rive pour trouver un pont? ").lower()
    
    if decision_riviere == "traverser":
        print("\nVous prenez votre courage à deux mains et vous lancez dans la rivière.")
        # Utilisation de l'opérateur logique pour déterminer le succès de la traversée
        if random.randint(1, 10) > 3:
            print("Vous traversez la rivière avec succès malgré le courant.")
        else:
            print("Le courant est trop fort ! Vous perdez un peu de temps à regagner la rive en titubant.")
    
    elif decision_riviere == "suivre":
        print("\nVous suivez prudemment la rive et découvrez un vieux pont en pierre qui vous permet de traverser en toute sécurité.")
    
    else:
        print("\nAction non reconnue. Hésitant trop longtemps, vous perdez du temps précieux sur le chemin.")
        
elif chemin == "droite":
    print("\nVous avez choisi le chemin de droite, dans l'ombre dense des arbres.")
    
    # 2ème entrée utilisateur : rencontre avec un animal sauvage
    decision_animal = input("Soudain, un grognement retentit et un animal sauvage apparaît. Voulez-vous vous 'cacher' derrière un buisson ou 'combattre' l'animal? ").lower()
    
    if decision_animal == "cacher":
        print("\nVous vous faufilez derrière un buisson. L'animal, intrigué, passe sans vous remarquer.")
    
    elif decision_animal == "combattre":
        print("\nArmé de votre courage et de votre épée, vous engagez le combat contre l'animal.")
        # Détermination aléatoire de l'issue du combat
        if random.randint(1, 10) > 5:
            print("Votre habileté vous permet de vaincre l'animal, qui s'enfuit en grognant.")
        else:
            print("L'animal se révèle plus redoutable que prévu. Vous subissez quelques blessures, mais parvenez à le repousser.")
    
    else:
        print("\nAction non reconnue. L'animal, déconcerté, s'enfuit dans la forêt.")
        
else:
    print("\nChoix invalide. Perdu dans vos hésitations, vous continuez d'une manière imprévisible, mais l'aventure se poursuit.")

# 3ème étape : la grotte mystérieuse
print("\nAprès plusieurs heures de marche, vous découvrez enfin une grotte énigmatique, cachée sous la liane d'un grand arbre.")
decision_grotte = input("Voulez-vous 'entrer' dans la grotte ou 'contourner' l'endroit pour explorer les environs? ").lower()

# Variable pour déterminer si le joueur obtient le trésor
tresor = False

if decision_grotte == "entrer":
    print("\nVous décidez d'entrer dans la grotte. L'air est frais et l'obscurité vous enveloppe.")
    
    # Choix dans la grotte
    decision_in_grotte = input("À l'intérieur, vous trouvez deux passages: l'un mène vers une zone éclairée ('lumière'), l'autre plonge dans l'obscurité ('ombre'). Que choisissez-vous? ").lower()
    
    if decision_in_grotte == "lumière":
        print("\nVous suivez le passage illuminé et découvrez une salle secrète remplie de coffres et de bijoux scintillants.")
        tresor = True  # Trésor trouvé
    
    elif decision_in_grotte == "ombre":
        print("\nVous osez vous aventurer dans l'obscurité et tombez nez à nez avec un gardien mystique de la grotte.")
        gardien = input("Le gardien vous observe. Voulez-vous essayer de 'parler' pour négocier ou 'attaquer' pour forcer le passage? ").lower()
        
        if gardien == "parler":
            print("\nVotre sincérité et vos bonnes manières impressionnent le gardien.")
            # Utilisation de l'opérateur logique pour vérifier si le joueur a déjà choisi un chemin valide
            if chemin == "gauche" or chemin == "droite":
                print("Le gardien vous accorde l'accès au trésor en vous conseillant une relique ancestrale.")
                tresor = True
            else:
                print("Malheureusement, votre parcours hésitant ne convainc pas le gardien. Vous quittez la grotte bredouille.")
                tresor = False
        
        elif gardien == "attaquer":
            print("\nVous engagez un combat épique contre le gardien!")
            if random.randint(1, 10) > 6:
                print("Après un combat acharné, vous triomphez du gardien et découvrez le trésor caché derrière lui.")
                tresor = True
            else:
                print("Le gardien est trop puissant et vous blesse grièvement. Vous devez fuir la grotte, le trésor restant hors de portée.")
                tresor = False
        
        else:
            print("\nIndécision fatale... Le gardien, déçu, vous force à quitter la grotte sans rien.")
            tresor = False
    else:
        print("\nAction non reconnue dans la grotte. Vous vous perdez dans ses méandres et repartez, le cœur lourd.")
        tresor = False

elif decision_grotte == "contourner":
    print("\nVous choisissez de contourner la grotte. En explorant les environs, vous trouvez un vieux parchemin attaché à une branche.")
    print("Le parchemin décrit l'emplacement d'un trésor, mais comporte une énigme à résoudre.")
    
    # 4ème entrée utilisateur : résolution d'une énigme
    enigme = input("Enigme : 'Je suis léger comme une plume, mais même le plus fort des hommes ne peut me tenir plus de 5 minutes. Qui suis-je?' Tapez votre réponse: ").lower()
    
    # On utilise l'opérateur logique "or" pour tester plusieurs réponses possibles
    if enigme == "la respiration" or enigme == "respiration":
        print("\nBravo ! Vous avez résolu l'énigme. Le parchemin révèle l'emplacement d'un petit coffre enterré sous un vieux chêne.")
        # Petite chance d'obtenir le trésor après avoir suivi l'indice
        if random.randint(1, 10) > 4:
            print("En creusant sous le chêne, vous découvrez un coffre rempli de pièces d'or et de bijoux rares!")
            tresor = True
        else:
            print("Malheureusement, le coffre est vide. La légende du trésor reste un mystère pour vous.")
            tresor = False
    else:
        print("\nVotre réponse n'est pas correcte. Le parchemin se déchire et le secret du trésor reste à jamais perdu.")
        tresor = False

else:
    print("\nAction non reconnue. Hésitant trop longtemps, vous perdez votre chance d'explorer et l'aventure s'achève sans trésor.")
    tresor = False

# Conclusion de l'histoire avec plusieurs fins possibles
print("\n========================================")
if tresor:
    print("Félicitations !")
    print("Vous avez trouvé le trésor et terminé votre aventure avec succès.")
else:
    print("Votre aventure s'achève sans trésor")
print("========================================")
print("Merci d'avoir joué à cette aventure.")
