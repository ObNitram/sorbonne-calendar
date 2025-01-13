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

start_date = datetime(2024, 9, 1, tzinfo=timezone.utc)
end_date = datetime(2025, 6, 30, tzinfo=timezone.utc)

MODULE_FUNCTIONS = {
    "ARES": get_ares_calendars,
    "NOYAU": get_noyau_calendars,
    "PSCR": get_pscr_calendars,
    "PNL": get_pnl_calendars,
    "AR": get_ar_calendars,
    "SRCS": get_srcs_calendars,
    "SFTR": get_sftr_calendars,
    "SAS": get_sas_calendars,
    "ANGLAIS": get_anglais_sar_calendars,
    "ARCHI": get_archi_calendars,
    "VLSI": get_vlsi_calendars,
    "SC": get_sc_calendars,
    "ALGAV": get_algav_calendars,
    "DLP": get_dlp_calendars,
    "MLBDA": get_mlbda_calendars,
}

def get_filtered_calendars_from_url(url: str) -> Calendar:
    raw_calendar = load_calendar_from_url(url, auth)
    return filter_events_by_date_range(raw_calendar, start_date, end_date)


class Master :
    def __init__(self, master: str, input_url: str, ues: list[str]):

        calendar = get_filtered_calendars_from_url(input_url)
        filtered_calendars: Dict[str, Calendar] = filter_events_by_name(calendar, ues)

        self.name = master
        self.ues = [UE(filtered_calendars, f"m1/{master}", ue) for ue in ues]

    def to_json(self):
        return {
            "master": self.name,
            "ues": [ue.to_json() for ue in self.ues]
        }

    def to_markdown(self):
        return f"## Calendrier des cours de M1 {self.name}\n\n" + ''.join(ue.to_markdown() for ue in self.ues)


class UE :
    def __init__(self, calendar: Dict[str, Calendar], output_path: str, ue: str):
        self.name = ue
        self.paths = save_calendars(MODULE_FUNCTIONS[ue](calendar[ue]), f"{output_path}/{ue}".lower())

    def to_json(self):
        return {
            "name": self.name,
            "groups": [{
                "group": f"{name}",
                "url": f"{host}{path}"
            } for name, path in self.paths.items()]
        }

    def to_markdown(self):
        return f"## {self.name}\n" + ''.join( f"### {name}\n{host}{path}\n\n" for name, path in self.paths.items())

def main() -> None:

    calendars: list[Master] = [
        Master("RES", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/RES/M1_RES", ["ARES"]),
        Master("SAR", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/SAR/M1_SAR", ["NOYAU", "PSCR", "PNL", "AR", "SRCS", "SFTR", "SAS", "ANGLAIS"]),
        Master("SESI", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/SESI/M1_SESI", ["ARCHI", "VLSI"]),
        Master("SFPN", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/SFPN/M1_SFPN-AFTI", ["SC"]),
        Master("STL", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/STL/M1_STL", ["ALGAV", "DLP"]),
        Master("DAC", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/DAC/M1_DAC", ["MLBDA"]),
    ]

    with open(link_file, 'w') as f:
        f.write("".join(calendar.to_markdown() for calendar in calendars))

    with open(json_file, 'w') as f:
        json.dump([calendar.to_json() for calendar in calendars], f)

    shutil.copy("index.html", 'public/index.html')


if __name__ == '__main__':
    main()