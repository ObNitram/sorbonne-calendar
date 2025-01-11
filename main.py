import shutil
from datetime import datetime, timezone
from ics import Calendar
from typing import Dict

from requests.auth import HTTPBasicAuth

from core.lib import (
    write_links_to_file,
    filter_events_by_name,
    save_calendars,
    filter_events_by_date_range,
    load_calendar_from_url,
    write_string_to_file
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
link_file = 'link.md'

start_date = datetime(2024, 9, 1, tzinfo=timezone.utc)
end_date = datetime(2025, 6, 30, tzinfo=timezone.utc)


def get_filtered_calendars_from_url(url: str) -> Calendar:
    raw_calendar = load_calendar_from_url(url, auth)
    return filter_events_by_date_range(raw_calendar, start_date, end_date)


# course_type_filters = [ "Cours", "cours", "TD1", "TD2", "TD3", "TD", "TME1", "TME2", "TME3", "TME", "TP", "anglais", "Anglais", "ANGLAIS"]

# Main logic
def main() -> None:
    with open(link_file, 'w'):
        pass

    # M1 RES
    write_string_to_file(f"## Calendrier des cours de M1 RES\n\n", link_file)

    calendar = get_filtered_calendars_from_url('https://cal.ufr-info-p6.jussieu.fr/caldav.php/RES/M1_RES')
    filters = ["ARES"]
    filtered_calendars: Dict[str, Calendar] = filter_events_by_name(calendar, filters)

    paths = save_calendars(get_ares_calendars(filtered_calendars["ARES"]), "m1/res/ares")
    write_links_to_file(paths, link_file, host, "ARES")

    # M1 SAR
    write_string_to_file(f"## Calendrier des cours de M1 SAR\n\n", link_file)

    calendar = get_filtered_calendars_from_url('https://cal.ufr-info-p6.jussieu.fr/caldav.php/SAR/M1_SAR')
    filters = ["NOYAU", "PSCR", "PNL", "AR", "SRCS", "SFTR", "SAS", "ANGLAIS"]
    filtered_calendars: Dict[str, Calendar] = filter_events_by_name(calendar, filters)

    paths = save_calendars(get_noyau_calendars(filtered_calendars["NOYAU"]), "m1/sar/noyau")
    write_links_to_file(paths, link_file, host, "NOYAU")

    paths = save_calendars(get_pscr_calendars(filtered_calendars["PSCR"]), "m1/sar/pscr")
    write_links_to_file(paths, link_file, host, "PSCR")

    # M1 SAR 2nd semestre
    write_string_to_file(f"## Calendrier des cours de M1 SAR 2nd semestre\n\n", link_file)

    paths = save_calendars(get_pnl_calendars(filtered_calendars["PNL"]), "m1/sar/pnl")
    write_links_to_file(paths, link_file, host, "PNL")
    
    paths = save_calendars(get_ar_calendars(filtered_calendars["AR"]), "m1/sar/ar")
    write_links_to_file(paths, link_file, host, "AR")

    paths = save_calendars(get_srcs_calendars(filtered_calendars["SRCS"]), "m1/sar/srcs")
    write_links_to_file(paths, link_file, host, "SRCS")

    paths = save_calendars(get_sftr_calendars(filtered_calendars["SFTR"]), "m1/sar/sftr")
    write_links_to_file(paths, link_file, host, "SFTR")

    paths = save_calendars(get_sas_calendars(filtered_calendars["SAS"]), "m1/sar/sas")
    write_links_to_file(paths, link_file, host, "SAS")

    # paths = save_calendars(get_anglais_sar_calendars(filtered_calendars["ANGLAIS"]), "m1/sar/anglais")
    # write_links_to_file(paths, link_file, host, "ANGLAIS")

    # M1 SESI
    write_string_to_file(f"## Calendrier des cours de M1 SESI\n\n", link_file)

    calendar = get_filtered_calendars_from_url('https://cal.ufr-info-p6.jussieu.fr/caldav.php/SESI/M1_SESI')
    filters = ["ARCHI", "VLSI"]
    filtered_calendars: Dict[str, Calendar] = filter_events_by_name(calendar, filters)

    paths = save_calendars(get_archi_calendars(filtered_calendars["ARCHI"]), "m1/sesi/archi")
    write_links_to_file(paths, link_file, host, "ARCHI")

    paths = save_calendars(get_vlsi_calendars(filtered_calendars["VLSI"]), "m1/sesi/vlsi")
    write_links_to_file(paths, link_file, host, "VLSI")

    # M1 SFPN
    write_string_to_file(f"## Calendrier des cours de M1 SFPN\n\n", link_file)

    calendar = get_filtered_calendars_from_url('https://cal.ufr-info-p6.jussieu.fr/caldav.php/SFPN/M1_SFPN-AFTI')
    filters = ["SC"]
    filtered_calendars: Dict[str, Calendar] = filter_events_by_name(calendar, filters)

    paths = save_calendars(get_sc_calendars(filtered_calendars["SC"]), "m1/sfpn/sc")
    write_links_to_file(paths, link_file, host, "SC")

    # M1 STL
    write_string_to_file(f"## Calendrier des cours de M1 STL\n\n", link_file)

    calendar = get_filtered_calendars_from_url('https://cal.ufr-info-p6.jussieu.fr/caldav.php/STL/M1_STL')
    filters = ["ALGAV", "DLP"]
    filtered_calendars: Dict[str, Calendar] = filter_events_by_name(calendar, filters)

    paths = save_calendars(get_algav_calendars(filtered_calendars["ALGAV"]), "m1/stl/algav")
    write_links_to_file(paths, link_file, host, "ALGAV")

    paths = save_calendars(get_dlp_calendars(filtered_calendars["DLP"]), "m1/stl/dlp")
    write_links_to_file(paths, link_file, host, "DLP")

    # M1 DAC
    write_string_to_file(f"## Calendrier des cours de M1 DAC\n\n", link_file)

    calendar = get_filtered_calendars_from_url('https://cal.ufr-info-p6.jussieu.fr/caldav.php/DAC/M1_DAC')
    filters = ["MLBDA"]
    filtered_calendars: Dict[str, Calendar] = filter_events_by_name(calendar, filters)

    paths = save_calendars(get_mlbda_calendars(filtered_calendars["MLBDA"]), "m1/dac/mlbda")
    write_links_to_file(paths, link_file, host, "MLBDA")

    shutil.copy(link_file, 'public/' + link_file)


if __name__ == '__main__':
    main()
