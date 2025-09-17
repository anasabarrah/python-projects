taches = []

def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche pour l'instant.")
    else:
        print("Liste des tâches :")
        for i, tache in enumerate(taches, start=1):
            print(f"{i}. {tache}")

def ajouter_tache():
    tache = input("Entrez la nouvelle tâche : ")
    taches.append(tache)
    print(f"Tâche '{tache}' ajoutée !")

def supprimer_tache():
    afficher_taches()
    try:
        numero = int(input("Numéro de la tâche à supprimer : "))
        if 1 <= numero <= len(taches):
            supprimee = taches.pop(numero-1)
            print(f"Tâche '{supprimee}' supprimée !")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

while True:
    print("\n--- Gestionnaire de tâches ---")
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Supprimer une tâche")
    print("4. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        afficher_taches()
    elif choix == "2":
        ajouter_tache()
    elif choix == "3":
        supprimer_tache()
    elif choix == "4":
        print("Au revoir !")
        break
    else:
        print("Option invalide.")
