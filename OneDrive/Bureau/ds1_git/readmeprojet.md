# =====================================================================
#  SYSTEME DE GESTION DE BIBLIOTHEQUE INTELLIGENTE
# =====================================================================
# 
# Bienvenue dans le depot du projet de gestion de bibliotheque developpe 
# en Python par Farouk et Baha. Ce projet met en place une bibliotheque 
# de fonctions complete pour gerer les livres, les adherents et les prets.
# 
# ---------------------------------------------------------------------
#  BIBLIOTHEQUE DE FONCTIONS (MODULES DU CODE & RESPONSABLES)
# ---------------------------------------------------------------------
# 
# * A. Catalogue (ajouter_livre, afficher_livres) - Responsable : Baha
#   Permet d'ajouter de nouveaux ouvrages au catalogue en verifiant 
#   l'unicite des identifiants et la validite des quantites.
# 
# * B. Disponibilite (disponibles) - Responsable : Farouk
#   Calcule en temps reel le nombre d'exemplaires disponibles pour un livre 
#   donne en comparant le stock total et les prets en cours.
# 
# * C. Emprunts et Retours (emprunter, retourner) - Responsable : Farouk
#   Gere la logique d'emprunt (statut adherent, stock, limite de 3 prets) 
#   et l'enregistrement de la date de retour.
# 
# * D. Recherche (rechercher) - Responsable : Farouk
#   Permet de trouver des livres par titre, auteur, categorie ou identifiant.
# 
# * E. Tri (trier) - Responsable : Farouk
#   Trie et affiche les livres par titre, auteur ou popularite (emprunts).
# 
# * F. Retards (detecter_retards) - Responsable : Farouk
#   Identifie les prets qui depassent la duree limite autorisee (14 jours).
# 
# * G. Statistiques & Alertes (statistiques) - Responsable : Farouk
#   Affiche un tableau de bord complet (totaux, prets actifs, categories, 
#   alertes de stock faible et Top 5 des livres).
# 
# * H. Recommandation (recommander) - Responsable : Farouk
#   Suggere les meilleurs livres disponibles selon une categorie demandee.
# 
# * I. Sauvegarde CSV (sauvegarder) - Responsable : Baha
#   Enregistre l'etat actuel dans books.csv, members.csv et loans.csv.
# 
# * J. Verification (verifier_donnees) - Responsable : Baha
#   Valide l'integrite des donnees chargees (unicite, coherence, stocks).
# 
# * K. Chargement CSV (charger) - Responsable : Baha
#   Restaure les donnees au demarrage avec repli sur le mode demonstration.
# 
# * L. Menu Principal - Responsables : Farouk & Baha
#   Boucle interactive permettant d'acceder a toutes les fonctionnalites.
# 
# ---------------------------------------------------------------------
#  DEMARCHE FACILE (GUIDE D'UTILISATION)
# ---------------------------------------------------------------------
# 
# 1. Prerequis : 
#    Installez Python 3 (aucune bibliotheque externe requise).
# 
# 2. Lancement du script : 
#    Executez le fichier Python principal dans votre terminal :
#    $ python nom_du_script.py
# 
# 3. Utilisation : 
#    Le programme charge les fichiers CSV ou initialise la demo. 
#    Naviguez via le menu interactif (choix de 1 a 10, ou 0 pour quitter).
# 
# 4. Sauvegarde : 
#    Effectuee automatiquement a la sortie (option 0) ou manuellement (option 10).
# =====================================================================