from ics import Calendar

# Lire le fichier .ics
with open('evenement.ics', 'r') as file:
    calendrier_data = file.read()

# Créer un objet Calendar
calendrier = Calendar(calendrier_data)

# Parcourir et afficher les événements du calendrier
for evenement in calendrier.events:
    print(f"Titre de l'événement : {evenement.name}")
    print(f"Date de début : {evenement.begin}")
    print(f"Date de fin : {evenement.end}")
    print(f"Description : {evenement.description}")
    print(f"Lieu : {evenement.location}")
    print("=" * 40)
