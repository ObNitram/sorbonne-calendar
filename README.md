# _Deprecated: As of 2026, this project is no longer maintained because I have completed my studies at Sorbonne Université. The code remains available for reference and use, but it may not reflect the latest changes in the university’s calendar system._

> If you would like to continue this project, feel free to contact me on LinkedIn 
[LinkedIn <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="12" height="12" />](https://link.obnitram.cloud/linkedin-g) so I can add a link to your new repository here.






# Sorbonne Calendar

Un script Python non officiel qui génère des liens vers les calendriers des différentes matières de Sorbonne Université.

## 📅 Utilisation

1. Accédez aux fichiers URL des matières supportées en cliquant [ --> ici <-- ](https://obnitram.github.io/sorbonne-calendar/index.html) pour une interface web.
2. Copiez l'URL du calendrier correspondant à votre matière.
3. Ajoutez les calendriers à votre application de calendrier préférée (Google Calendar, Apple Calendar, etc.) en utilisant l'option d'ajout via URL.

### Exemple d'ajout dans Google Calendar :
   - Ouvrez Google Calendar.
   - Cliquez sur le signe **+** à côté de "Autres agendas", puis sélectionnez **Ajouter via URL**.
   - Collez l'URL correspondant à votre matière.

## ⚠️ Point Important

Les calendriers sont automatiquement mis à jour toutes les 4 heures. Cependant, les modifications peuvent prendre plus de temps avant d’être reflétées dans votre application de calendrier.

## 🤝 Contributions

Les contributions sont les bienvenues ! Si vous souhaitez ajouter un nouveau calendrier, corriger des erreurs ou améliorer le projet, vous pouvez !

### Comment ajouter un cours (example du cours de RTEL du master RES)

- si le cours appartient a un master pas encore supporter, il faut ajouter a la liste `calendars` dans `main.py` l'objet Master representant le nouveau master qui prends :
   - le nom du master
   - l'url du calendrier de ce master
   - la liste de ses ue (vous n'etes pas obliger de rajouter l'integralité des ues du master), une ue est representer pas un dictionnaire contenant 2 paire clé/valeur :
      - `ue`, le nom de l'ue 
      - `semester`, le semestre de la matiere
```python
Master("RES", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/RES/M1_RES", [
   {"ue": "ARES",  "semester": 1}
]),
```
- écrire le module pour parser correctement le calendrier de votre Master, pour visualiser les noms des evenements vous pouvez vous aider du script `test.py` :
    - `course_type_filters` represente la liste des evenement de la matiere dans notre cas `CS` represente le cours de RTEL, `TD` represente les tds, `TME` represente les tmes et `default` les evenements restant.
    - la fonction doit retourner un dictionnaire qui associe a chaque groupe le calendrier du groupe, dans notre cas le cours de rtel possede 2 groupes :
        - le groupe 2 `group2` qui fusione le cours `CS`, les tds `TD2`, les tmes `TME2`, et le reste `default`
        - le groupe 3 `group3` qui fusione le cours `CS`, les tds `TD3`, les tmes `TME3`, et le reste `default`
```python
from ics import Calendar

from core.lib import (
    filter_events_by_name,
    merge_calendars
)


def get_ares_calendars(raw_calendar: Calendar) -> dict[str, Calendar]:
    course_type_filters = ["CS", "TD2", "TD3", "TME2", "TME3"]
    filtered_calendars = filter_events_by_name(raw_calendar, course_type_filters)

    group2 = merge_calendars([
        filtered_calendars["CS"],
        filtered_calendars["TD2"],
        filtered_calendars["TME2"],
        filtered_calendars["default"]
    ])

    group3 = merge_calendars([
        filtered_calendars["CS"],
        filtered_calendars["TD2"],
        filtered_calendars["TME3"],
        filtered_calendars["default"]
    ])

    return {
        "group2": group2,
        "group3": group3
    }

```
- On ajoute le module au fichier `globals.py` :
    - ajouter l'import `from modules.lib_rtel import get_rtel_calendars`
    - on ajoute la fonction a la table de correspondante `MODULE_FUNCTIONS`, la clé est constituer du nom du master, `.`, le nom du cours renseigner dans l'object Master.

## 📬 Support

Si vous avez des questions ou des suggestions, vous pouvez ouvrir une issue pour contacter le mainteneur du projet.
