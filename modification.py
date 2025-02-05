"""
Ajout de la fonction prendre_decision(question, options), qui permet de s'assurer que l'utilisateur entre une réponse valide.

Ajout de la fonction lancer_defi(proba_reussite, succes_msg, echec_msg), qui simule un défi avec une probabilité de réussite donnée.

Ajout de la fonction principale aventure(), qui gère le déroulement du jeu.

Amélioration de la gestion des entrées utilisateur

Dans le code original, les entrées utilisateur étaient obtenues directement via input(), sans validation.

Le code présent utilise prendre_decision() pour forcer l'utilisateur à entrer une réponse valide et éviter les erreurs.

Dans le code original, la probabilité de succès pour certaines actions était définie par random.randint(1, 10) > valeur.

Le code présent remplace cela par lancer_defi(proba_reussite, succes_msg, echec_msg), rendant le code plus modulaire et lisible.

Suppression des réponses par défaut non reconnues, remplacées par une boucle demandant à l’utilisateur de choisir une option valide.

Réduction du risque d’erreur utilisateur en limitant les choix à des réponses précises et contrôlées.

Le code original répétait plusieurs blocs de code pour gérer des décisions similaires.

Grâce aux nouvelles fonctions, le code présent réduit ces répétitions en factorisant la logique commune.

L'aventure est toujours la même, mais sa gestion est plus claire.

Ajout de if __name__ == "__main__": aventure() pour permettre l’exécution du script comme un programme autonome.

La variable tresor est toujours utilisée pour déterminer la réussite de l’aventure.

La gestion des conditions menant à la découverte du trésor a été rationalisée via lancer_defi().
"""