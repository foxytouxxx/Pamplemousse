import itertools
from pyscript import document, window

### Le document.write() provient du python pour faire interagir le html directement dans la page web
###  Cela permet d'avoir un rendu html avec notre script python

# Fonction pour créer les groupes d'équipes
def creer_groupes(equipes, nb_groupes):
    # Initialisation d'une liste de listes, chaque sous-liste représente un groupe
    groupes = [[] for _ in range(nb_groupes)]
    
    # Boucle à travers les équipes et les répartit dans les groupes
    for i, equipe in enumerate(equipes):
        groupes[i % nb_groupes].append(equipe)
    
    return groupes

# Fonction pour affronter toutes les autres équipes d'un groupe
def affronter_tous_les_autres(equipe1, equipe2, groupe_index, match_index):
    # Affichage HTML du match entre deux équipes
    document.write(f"<div id='match-{groupe_index}-{match_index}'>")
    document.write(f"Match {match_index + 1}: {equipe1} vs {equipe2}<br>")
    document.write("</div>")

# Fonction pour organiser les matchs dans un groupe donné
def organiser_matchs_dans_groupe(groupe, groupe_index):
    # Début de la section HTML pour afficher les matchs d'un groupe
    document.write(f"<div id='groupe-{groupe_index}'>")
    document.write(f"<h3>Groupe {groupe_index + 1}</h3>")
    
    # Génération de toutes les combinaisons possibles de matchs entre les équipes du groupe
    combinaisons = itertools.combinations(groupe, 2)
    
    # Boucle à travers les combinaisons pour affronter chaque équipe contre toutes les autres
    for match_index, (equipe1, equipe2) in enumerate(combinaisons):
        affronter_tous_les_autres(equipe1, equipe2, groupe_index, match_index)
    
    # Fin de la section HTML pour afficher les matchs d'un groupe
    document.write("</div>")

# Fonction pour démarrer le tournoi
def start_tournament(event):
    # Demande à l'utilisateur le nombre total d'équipes
    nb_equipes = int(window.prompt("Entrez le nombre total d'équipes : "))
    equipes = [f"Equipe {i+1}" for i in range(nb_equipes)]  # Création d'une liste d'équipes
    
    # Demande à l'utilisateur s'il veut choisir le nombre de groupes
    choix = window.prompt("Voulez-vous choisir le nombre de groupes ? (Oui/Non) : ")
    if choix.lower() == "oui":
        nb_groupes = int(window.prompt("Entrez le nombre de groupes : "))  # Choix du nombre de groupes
    else:
        nb_groupes = min(5, nb_equipes)  # Par défaut, au moins 5 groupes ou autant que d'équipes s'il y en a moins
    
    # Création des groupes en répartissant les équipes
    groupes = creer_groupes(equipes, nb_groupes)

    # Affichage HTML de l'organisation des matchs
    document.write("<h2>Organisation des matchs</h2>")
    for i, groupe in enumerate(groupes):
        organiser_matchs_dans_groupe(groupe, i)

# Sélection du bouton sur la page HTML et ajout d'un événement pour démarrer le tournoi au clic
button = document.querySelector("button")
button.addEventListener("click", start_tournament)

