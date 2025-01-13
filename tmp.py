import shutil
from datetime import datetime, timezone
from ics import Calendar
from typing import Dict
import json

from requests.auth import HTTPBasicAuth

from core.lib import (
    filter_events_by_name,
    save_calendars,
    filter_events_by_date_range,
    load_calendar_from_url
)
from core.lib_algav import get_algav_calendars
from core.lib_archi import get_archi_calendars
from core.lib_ares import get_ares_calendars
from core.lib_dlp import get_dlp_calendars
from core.lib_noyau import get_noyau_calendars
from core.lib_pscr import get_pscr_calendars
from core.lib_sc import get_sc_calendars
from core.lib_vlsi import get_vlsi_calendars
from core.lib_mlbda import get_mlbda_calendars
from core.lib_pnl import get_pnl_calendars
from core.lib_ar import get_ar_calendars
from core.lib_srcs import get_srcs_calendars
from core.lib_sftr import get_sftr_calendars
from core.lib_sas import get_sas_calendars
from core.lib_anglais_sar import get_anglais_sar_calendars

# Replace 'username' and 'password' with your correct credentials
username = 'student.master'
password = 'guest'
auth = HTTPBasicAuth(username, password)

# Base URL
host = 'https://obnitram.github.io/sorbonne-calendar/'
link_file = 'public/link.md'
json_file = 'public/calendars.json'

def get_school_year_dates():
    """Détermine dynamiquement les dates de début et de fin de l'année scolaire actuelle."""
    today = datetime.now(timezone.utc)
    current_year = today.year

    if today.month >= 9:  # Année scolaire commence en septembre de l'année actuelle
        start_date = datetime(current_year, 9, 1, tzinfo=timezone.utc)
        end_date = datetime(current_year + 1, 6, 30, tzinfo=timezone.utc)
    else:  # Année scolaire a commencé en septembre de l'année précédente
        start_date = datetime(current_year - 1, 9, 1, tzinfo=timezone.utc)
        end_date = datetime(current_year, 6, 30, tzinfo=timezone.utc)

    return start_date, end_date

MODULE_FUNCTIONS = {
    "RES.ARES": get_ares_calendars,
    "SAR.NOYAU": get_noyau_calendars,
    "SAR.PSCR": get_pscr_calendars,
    "SAR.PNL": get_pnl_calendars,
    "SAR.AR": get_ar_calendars,
    "SAR.SRCS": get_srcs_calendars,
    "SAR.SFTR": get_sftr_calendars,
    "SAR.SAS": get_sas_calendars,
    "SAR.ANGLAIS": get_anglais_sar_calendars,
    "SESI.ARCHI": get_archi_calendars,
    "SESI.VLSI": get_vlsi_calendars,
    "SFPN.SC": get_sc_calendars,
    "STL.ALGAV": get_algav_calendars,
    "STL.DLP": get_dlp_calendars,
    "DAC.MLBDA": get_mlbda_calendars,
}

def get_filtered_calendars_from_url(url: str) -> Calendar:
    raw_calendar = load_calendar_from_url(url, auth)
    return filter_events_by_date_range(raw_calendar, *get_school_year_dates())


class UE :
    name: str = ""
    year: str = ""
    semester: str = ""
    master: str = ""
    paths: Dict[str, Calendar] = {}
    def __init__(self, calendar: Dict[str, Calendar], ue: str, year: str, semester: str, master: str):
        self.name = ue
        self.year = year
        self.semester = semester
        self.master = master
        key = f"{master}.{ue}"  # Génère une clé composite
        self.paths = save_calendars(MODULE_FUNCTIONS[key](calendar[ue]), f"{year}/{master}/{ue}".lower())

    def to_json(self):
        return {
            "name": self.name,
            "year": self.year,
            "semester": self.semester,
            "groups": [{
                "group": f"{name}",
                "url": f"{host}{path}"
            } for name, path in self.paths.items()]
        }

    def to_markdown(self):
        return f"## {self.name} ({self.year}, {self.semester})\n" + ''.join(f"### {name}\n{host}{path}\n\n" for name, path in self.paths.items())


class Master :
    name: str = ""
    ues: list[UE] = []
    def __init__(self, master: str, input_url: str, ues: list[dict]):
        # ues is now a list of dictionaries with keys: 'name', 'year', 'semester'

        calendar = get_filtered_calendars_from_url(input_url)
        filtered_calendars: Dict[str, Calendar] = filter_events_by_name(calendar, [ue['ue'] for ue in ues])

        self.name = master
        self.ues = [
            UE(filtered_calendars, **ue, master=master)
            for ue in ues
        ]

    def to_json(self):
        return {
            "master": self.name,
            "ues": [ue.to_json() for ue in self.ues]
        }

    def to_markdown(self):
        return f"## Calendrier des cours de M1 {self.name}\n\n" + ''.join(ue.to_markdown() for ue in self.ues)


def main() -> None:

    calendars: list[Master] = [
        Master("RES", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/RES/M1_RES", [
            {"ue": "ARES", "year": "M1", "semester": "S1"}
        ]),
        Master("SAR", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/SAR/M1_SAR", [
            {"ue": "NOYAU", "year": "M1", "semester": "S1"},
            {"ue": "PSCR", "year": "M1", "semester": "S1"},
            {"ue": "PNL", "year": "M1", "semester": "S2"},
            {"ue": "AR", "year": "M1", "semester": "S2"},
            {"ue": "SRCS", "year": "M1", "semester": "S2"},
            {"ue": "SFTR", "year": "M1", "semester": "S2"},
            {"ue": "SAS", "year": "M1", "semester": "S2"},
            {"ue": "ANGLAIS", "year": "M1", "semester": "S2"}
        ]),
        Master("SESI", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/SESI/M1_SESI", [
            {"ue": "ARCHI", "year": "M1", "semester": "S1"},
            {"ue": "VLSI", "year": "M1", "semester": "S1"}
        ]),
        Master("SFPN", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/SFPN/M1_SFPN-AFTI", [
            {"ue": "SC", "year": "M1", "semester": "S1"}
        ]),
        Master("STL", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/STL/M1_STL", [
            {"ue": "ALGAV", "year": "M1", "semester": "S1"},
            {"ue": "DLP", "year": "M1", "semester": "S1"}
        ]),
        Master("DAC", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/DAC/M1_DAC", [
            {"ue": "MLBDA", "year": "M1", "semester": "S1"}
        ]),
    ]

    with open(link_file, 'w') as f:
        f.write("".join(calendar.to_markdown() for calendar in calendars))

    with open(json_file, 'w') as f:
        json.dump([calendar.to_json() for calendar in calendars], f)

    shutil.copy("index.html", 'public/index.html')


if __name__ == '__main__':
    main()
