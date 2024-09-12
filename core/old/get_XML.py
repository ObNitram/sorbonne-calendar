import requests
from requests.auth import HTTPBasicAuth

# URL du serveur CalDAV
url = 'https://cal.ufr-info-p6.jussieu.fr/caldav.php/SAR/M1_SAR/'

# En-têtes HTTP
headers = {
    'Depth': '1',
    'Content-Type': 'application/xml; charset="utf-8"'
}

# Corps de la requête PROPFIND
propfind_body = '''<?xml version="1.0" encoding="UTF-8"?>
<d:propfind xmlns:d="DAV:">
  <d:prop>
    <d:displayname />
    <d:resourcetype />
  </d:prop>
</d:propfind>
'''

# Tenter avec des identifiants vides
response = requests.request(
    method="PROPFIND",
    url=url,
    headers=headers,
    data=propfind_body,
    auth=HTTPBasicAuth('student.master', 'guest')  # Identifiants vides
)

# Vérifier le statut de la réponse
if response.status_code == 207:  # Multistatus = succès pour PROPFIND
    print("Requête PROPFIND réussie!")
    print(response.text)  # Afficher la réponse du serveur
else:
    print(f"Erreur: {response.status_code}")

# Enregistrer la réponse dans un fichier
with open('propfind_response.xml', 'w') as file:
    file.write(response.text)