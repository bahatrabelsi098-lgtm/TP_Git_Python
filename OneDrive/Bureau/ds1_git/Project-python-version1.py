import csv
from datetime import date

MAX_PRETS = 3
DUREE_PRET = 14
SEUIL_STOCK_FAIBLE = 1

# 1. DONNEES DE DEMONSTRATION

livres = [
    {"id": 1, "titre": "Python", "auteur": "Ahmed",
     "categorie": "Informatique", "annee": 2024, "total": 3},

    {"id": 2, "titre": "Java", "auteur": "Ali",
     "categorie": "Informatique", "annee": 2023, "total": 2},

    {"id": 3, "titre": "Math", "auteur": "Sami",
     "categorie": "Science", "annee": 2022, "total": 2}
]

adherents = [
    {"id": 1, "nom": "Farouk", "prenom": "Farouk",
     "contact": "farouk@gmail.com", "actif": True},

    {"id": 2, "nom": "Baha", "prenom": "Baha",
     "contact": "baha@gmail.com", "actif": True}
]

prets = []

# Copies des donnees originales
livres_demo = [x.copy() for x in livres]
adherents_demo = [x.copy() for x in adherents]
prets_demo = [x.copy() for x in prets]


# A. CATALOGUE

# Ajouter un livre
def ajouter_livre():

    id_livre = int(input("ID du livre : "))

    for livre in livres:
        if livre["id"] == id_livre:
            print("ID deja utilise !")
            return

    titre = input("Titre : ")
    auteur = input("Auteur : ")
    categorie = input("Categorie : ")
    annee = int(input("Annee : "))
    total = int(input("Nombre d'exemplaires : "))

    if total < 0:
        print("Quantite invalide")
        return

    nouveau_livre = {
        "id": id_livre,
        "titre": titre,
        "auteur": auteur,
        "categorie": categorie,
        "annee": annee,
        "total": total
    }

    livres.append(nouveau_livre)
    print("Livre ajoute avec succes")


# Afficher les livres
def afficher_livres():

    for livre in livres:
        print(livre)

# B. DISPONIBILITE

def disponibles(id_livre):

    total = 0
    empruntes = 0

    for livre in livres:
        if livre["id"] == id_livre:
            total = livre["total"]

    for pret in prets:
        if pret["id_livre"] == id_livre:
            if pret["date_retour"] == "":
                empruntes += 1

    return total - empruntes


# C. EMPRUNTS ET RETOURS

# Emprunter un livre
def emprunter():

    id_livre = int(input("ID du livre : "))
    id_adherent = int(input("ID adherent : "))

    livre_trouve = False
    adherent_trouve = False

    for livre in livres:
        if livre["id"] == id_livre:
            livre_trouve = True

    for adherent in adherents:
        if adherent["id"] == id_adherent:
            adherent_trouve = True

            if adherent["actif"] == False:
                print("Adherent desactive")
                return

    if livre_trouve == False:
        print("Livre introuvable")
        return

    if adherent_trouve == False:
        print("Adherent introuvable")
        return

    if disponibles(id_livre) <= 0:
        print("Stock epuise")
        return

    compteur = 0

    for pret in prets:
        if pret["id_adherent"] == id_adherent:
            if pret["date_retour"] == "":
                compteur += 1

    if compteur >= MAX_PRETS:
        print("Limite de 3 prets atteinte")
        return

    id_pret = 1

    for pret in prets:
        if pret["id_pret"] >= id_pret:
            id_pret = pret["id_pret"] + 1

    nouveau_pret = {
        "id_pret": id_pret,
        "id_livre": id_livre,
        "id_adherent": id_adherent,
        "date_emprunt": str(date.today()),
        "date_retour": ""
    }

    prets.append(nouveau_pret)

    print("Emprunt enregistre avec succes")
    print("ID du pret :", id_pret)


# Retourner un livre
def retourner():

    id_pret = int(input("ID du pret : "))

    for pret in prets:

        if pret["id_pret"] == id_pret:

            if pret["date_retour"] != "":
                print("Livre deja retourne")
                return

            pret["date_retour"] = str(date.today())

            print("Retour effectue avec succes")
            return

    print("Pret introuvable")


# D. RECHERCHE

def rechercher():

    valeur = input("Recherche : ").lower()

    trouve = False

    for livre in livres:

        if (valeur in livre["titre"].lower()
            or valeur in livre["auteur"].lower()
            or valeur == livre["categorie"].lower()
            or valeur == str(livre["id"])):

            print(livre)
            trouve = True

    if trouve == False:
        print("Aucun resultat trouve")


# E. TRI

def trier():

    print("1. Par titre")
    print("2. Par auteur")
    print("3. Par nombre d'emprunts")

    choix = input("Votre choix : ")

    liste = livres.copy()

    if choix not in ["1", "2", "3"]:
        print("Choix invalide")
        return

    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):

            compteur1 = 0
            compteur2 = 0

            for pret in prets:
                if pret["id_livre"] == liste[i]["id"]:
                    compteur1 += 1

                if pret["id_livre"] == liste[j]["id"]:
                    compteur2 += 1

            echange = False

            if choix == "1":
                if liste[i]["titre"].lower() > liste[j]["titre"].lower():
                    echange = True

            elif choix == "2":
                if liste[i]["auteur"].lower() > liste[j]["auteur"].lower():
                    echange = True

            elif choix == "3":
                if compteur1 < compteur2:
                    echange = True

            if echange:
                temp = liste[i]
                liste[i] = liste[j]
                liste[j] = temp

    for livre in liste:
        print(livre)



# F. RETARDS

def detecter_retards():

    retards = []

    for pret in prets:

        if pret["date_retour"] == "":

            date_emprunt = date.fromisoformat(
                pret["date_emprunt"]
            )

            duree = (date.today() - date_emprunt).days

            if duree > DUREE_PRET:
                retards.append(pret)

    return retards


# G. STATISTIQUES

def statistiques():

    total_livres = len(livres)
    total_exemplaires = 0
    total_disponibles = 0

    actifs = 0
    termines = 0

    for livre in livres:

        total_exemplaires += livre["total"]

        total_disponibles += disponibles(livre["id"])

    for pret in prets:

        if pret["date_retour"] == "":
            actifs += 1
        else:
            termines += 1

    retards = detecter_retards()

    print("\n===== STATISTIQUES =====")

    print("Nombre de livres :", total_livres)
    print("Total exemplaires :", total_exemplaires)
    print("Exemplaires disponibles :", total_disponibles)
    print("Prets actifs :", actifs)
    print("Prets termines :", termines)
    print("Retards :", len(retards))

    # Repartition par categorie

    categories = {}

    for livre in livres:

        categorie = livre["categorie"]

        if categorie in categories:
            categories[categorie] += 1
        else:
            categories[categorie] = 1

    print("\nRepartition par categorie :")

    for categorie in categories:
        print(categorie, ":", categories[categorie])

    # Alertes

    print("\nAlertes :")

    for livre in livres:

        stock = disponibles(livre["id"])

        if livre["total"] > 0 and stock == 0:
            print(livre["titre"], ": Tout emprunte")

        elif stock <= SEUIL_STOCK_FAIBLE:
            print(livre["titre"], ": Stock faible")

    # Top 5 des livres

    print("\nTop 5 des livres :")

    liste = livres.copy()

    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):

            compteur1 = 0
            compteur2 = 0

            for pret in prets:

                if pret["id_livre"] == liste[i]["id"]:
                    compteur1 += 1

                if pret["id_livre"] == liste[j]["id"]:
                    compteur2 += 1

            if compteur1 < compteur2:
                temp = liste[i]
                liste[i] = liste[j]
                liste[j] = temp

    for livre in liste[:5]:
        print(livre["titre"])



# H. RECOMMANDATION

def recommander():

    categorie = input("Categorie : ").lower()

    resultat = []

    for livre in livres:

        if livre["categorie"].lower() == categorie:

            if disponibles(livre["id"]) > 0:

                compteur = 0

                for pret in prets:
                    if pret["id_livre"] == livre["id"]:
                        compteur += 1

                resultat.append([livre, compteur])

    # Trier par popularite puis par titre

    for i in range(len(resultat)):
        for j in range(i + 1, len(resultat)):

            livre1 = resultat[i][0]
            livre2 = resultat[j][0]

            compteur1 = resultat[i][1]
            compteur2 = resultat[j][1]

            if compteur1 < compteur2:

                temp = resultat[i]
                resultat[i] = resultat[j]
                resultat[j] = temp

            elif compteur1 == compteur2:

                if livre1["titre"].lower() > livre2["titre"].lower():

                    temp = resultat[i]
                    resultat[i] = resultat[j]
                    resultat[j] = temp

    if len(resultat) == 0:
        print("Aucun livre disponible")
        return

    print("\n===== RECOMMANDATIONS =====")

    for element in resultat[:3]:
        print(element[0]["titre"])

# I. SAUVEGARDE CSV

def sauvegarder():

    with open("books.csv", "w", newline="", encoding="utf-8") as f:

        champs = ["id", "titre", "auteur", "categorie", "annee", "total"]

        writer = csv.DictWriter(f, fieldnames=champs)
        writer.writeheader()
        writer.writerows(livres)

    with open("members.csv", "w", newline="", encoding="utf-8") as f:

        champs = ["id", "nom", "prenom", "contact", "actif"]

        writer = csv.DictWriter(f, fieldnames=champs)
        writer.writeheader()
        writer.writerows(adherents)

    with open("loans.csv", "w", newline="", encoding="utf-8") as f:

        champs = [
            "id_pret", "id_livre", "id_adherent",
            "date_emprunt", "date_retour"
        ]

        writer = csv.DictWriter(f, fieldnames=champs)
        writer.writeheader()
        writer.writerows(prets)

    print("Sauvegarde effectuee")

# J. VERIFICATION DES DONNEES CSV

def verifier_donnees(nouveaux_livres, nouveaux_adherents, nouveaux_prets):

    ids_livres = []
    ids_adherents = []
    ids_prets = []

    # Verifier les livres

    for livre in nouveaux_livres:

        if livre["id"] in ids_livres:
            return False

        ids_livres.append(livre["id"])

        if livre["total"] < 0:
            return False

    # Verifier les adherents

    for adherent in nouveaux_adherents:

        if adherent["id"] in ids_adherents:
            return False

        ids_adherents.append(adherent["id"])

    # Verifier les prets

    for pret in nouveaux_prets:

        if pret["id_pret"] in ids_prets:
            return False

        ids_prets.append(pret["id_pret"])

        if pret["id_livre"] not in ids_livres:
            return False

        if pret["id_adherent"] not in ids_adherents:
            return False

        try:
            date_emprunt = date.fromisoformat(pret["date_emprunt"])

            if pret["date_retour"] != "":
                date_retour = date.fromisoformat(pret["date_retour"])

                if date_retour < date_emprunt:
                    return False

        except ValueError:
            return False

    # Verifier le stock

    for livre in nouveaux_livres:

        empruntes = 0

        for pret in nouveaux_prets:

            if pret["id_livre"] == livre["id"]:
                if pret["date_retour"] == "":
                    empruntes += 1

        if empruntes > livre["total"]:
            return False

    return True

# K. CHARGEMENT CSV

def charger():

    global livres, adherents, prets

    try:

        # Charger les livres

        with open("books.csv", "r", encoding="utf-8") as f:

            reader = csv.DictReader(f)

            champs = ["id", "titre", "auteur", "categorie", "annee", "total"]

            if reader.fieldnames is None or any(x not in reader.fieldnames for x in champs):
                raise ValueError

            nouveaux_livres = []

            for ligne in reader:

                livre = {
                    "id": int(ligne["id"]),
                    "titre": ligne["titre"],
                    "auteur": ligne["auteur"],
                    "categorie": ligne["categorie"],
                    "annee": int(ligne["annee"]),
                    "total": int(ligne["total"])
                }

                nouveaux_livres.append(livre)

        # Charger les adherents

        with open("members.csv", "r", encoding="utf-8") as f:

            reader = csv.DictReader(f)

            champs = ["id", "nom", "prenom", "contact", "actif"]

            if reader.fieldnames is None or any(x not in reader.fieldnames for x in champs):
                raise ValueError

            nouveaux_adherents = []

            for ligne in reader:

                adherent = {
                    "id": int(ligne["id"]),
                    "nom": ligne["nom"],
                    "prenom": ligne["prenom"],
                    "contact": ligne["contact"],
                    "actif": ligne["actif"].lower() == "true"
                }

                nouveaux_adherents.append(adherent)

        # Charger les prets

        with open("loans.csv", "r", encoding="utf-8") as f:

            reader = csv.DictReader(f)

            champs = [
                "id_pret", "id_livre", "id_adherent",
                "date_emprunt", "date_retour"
            ]

            if reader.fieldnames is None or any(x not in reader.fieldnames for x in champs):
                raise ValueError

            nouveaux_prets = []

            for ligne in reader:

                pret = {
                    "id_pret": int(ligne["id_pret"]),
                    "id_livre": int(ligne["id_livre"]),
                    "id_adherent": int(ligne["id_adherent"]),
                    "date_emprunt": ligne["date_emprunt"],
                    "date_retour": ligne["date_retour"]
                }

                nouveaux_prets.append(pret)

        # Verifier toutes les donnees avant de les utiliser

        if verifier_donnees(nouveaux_livres, nouveaux_adherents, nouveaux_prets):

            livres = nouveaux_livres
            adherents = nouveaux_adherents
            prets = nouveaux_prets

            print("Donnees chargees avec succes")

        else:
            raise ValueError

    except (FileNotFoundError, ValueError, KeyError, TypeError, csv.Error):

        livres = [x.copy() for x in livres_demo]
        adherents = [x.copy() for x in adherents_demo]
        prets = [x.copy() for x in prets_demo]

        print("Fichiers absents ou incorrects")
        print("Donnees de demonstration utilisees")

# L. MENU PRINCIPAL

charger()

while True:

    print("\n================================")
    print("    BIBLIOTHEQUE INTELLIGENTE")
    print("================================")

    print("1. Ajouter un livre")
    print("2. Afficher les livres")
    print("3. Emprunter un livre")
    print("4. Retourner un livre")
    print("5. Rechercher un livre")
    print("6. Trier les livres")
    print("7. Statistiques")
    print("8. Detecter les retards")
    print("9. Recommander des livres")
    print("10. Sauvegarder")
    print("0. Quitter")

    choix = input("\nVotre choix : ")

    if choix == "1":
        ajouter_livre()

    elif choix == "2":
        afficher_livres()

    elif choix == "3":
        emprunter()

    elif choix == "4":
        retourner()

    elif choix == "5":
        rechercher()

    elif choix == "6":
        trier()

    elif choix == "7":
        statistiques()

    elif choix == "8":

        resultat = detecter_retards()

        if len(resultat) == 0:
            print("Aucun retard")

        else:
            print("Prets en retard :")
            for pret in resultat:
                print(pret)

    elif choix == "9":
        recommander()

    elif choix == "10":
        sauvegarder()

    elif choix == "0":
        sauvegarder()
        print("Au revoir !")
        break

    else:
        print("Choix invalide")
