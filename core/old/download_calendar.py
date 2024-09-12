import requests
from requests.auth import HTTPBasicAuth

# URL de la ressource CalDAV
url = 'https://cal.ufr-info-p6.jussieu.fr/caldav.php/SAR/M1_SAR'

# Remplacer 'username' et 'password' par tes identifiants corrects
username = 'student.master'
password = 'guest'
url_with_credentials = f"https://{username}:{password}@cal.ufr-info-p6.jussieu.fr/caldav.php/SAR/M1_SAR"

print(url_with_credentials)

# Effectuer la requête GET avec authentification HTTP Basic
response = requests.get(url, auth=HTTPBasicAuth(username, password))
#response = requests.get(url_with_credentials)

# Vérification du statut de la réponse
if response.status_code == 200:
    print("Accès réussi!")

    print(response.content)

    # Enregistrer le fichier .ics localement
    with open('evenement.ics', 'wb') as file:
        file.write(response.content)


elif response.status_code == 401:
    print("Erreur 401 : Authentification requise ou informations incorrectes.")
else:
    print(f"Erreur {response.status_code}: La requête a échoué.")



