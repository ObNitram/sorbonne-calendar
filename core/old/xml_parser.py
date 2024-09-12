import xml.etree.ElementTree as ET


def extraire_liens_ics_et_noms(xml_file):
    # Namespace DAV utilisé dans le fichier XML
    namespace = {'dav': 'DAV:'}

    # Lire et parser le fichier XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Liste pour stocker les résultats
    resultats = []

    # Parcourir chaque élément <response> pour trouver les liens .ics et leurs noms
    for response in root.findall('dav:response', namespace):
        href_element = response.find('dav:href', namespace)
        displayname_element = response.find('.//dav:displayname', namespace)

        if href_element is not None and href_element.text.endswith('.ics'):
            href = href_element.text
            nom = displayname_element.text if displayname_element is not None else 'Sans nom'
            resultats.append((nom, href))

    return resultats


# Exemple d'utilisation :
xml_file = 'propfind_response.xml'
liens_ics_et_noms = extraire_liens_ics_et_noms(xml_file)

resultats_trie = sorted(liens_ics_et_noms, key=lambda x: x[0])

# Afficher les résultats
for nom, lien in resultats_trie:
    print(f"Nom du calendrier : {nom},\t \t Lien .ics : {lien}")