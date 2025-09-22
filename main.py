import shutil
import json

from core.Master import Master
from core.config import publish_dir

def main() -> None:

    calendars: list[Master] = [
        # Master 1
        Master("M1-RES", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/RES/M1_RES", [
            {"ue": "ARES",  "semester": 1}
        ]),
        Master("M1-SAR", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/SAR/M1_SAR", [
            {"ue": "NOYAU",  "semester": 1},
            {"ue": "PSCR",  "semester": 1},
            {"ue": "PNL",  "semester": 2},
            {"ue": "AR",  "semester": 2},
            {"ue": "SRCS",  "semester": 2},
            {"ue": "SFTR",  "semester": 2},
            {"ue": "SAS",  "semester": 2},
            {"ue": "ANGLAIS",  "semester": 2}
        ]),
        Master("M1-SESI", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/SESI/M1_SESI", [
            {"ue": "ARCHI",  "semester": 1},
            {"ue": "VLSI",  "semester": 1},
            {"ue": "MULTI",  "semester": 2},
            {"ue": "IOC",  "semester": 2}
        ]),
        Master("M1-SFPN", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/SFPN/M1_SFPN-AFTI", [
            {"ue": "SC",  "semester": 1}
        ]),
        Master("M1-STL", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/STL/M1_STL", [
            {"ue": "ALGAV",  "semester": 1},
            {"ue": "DLP",  "semester": 1}
        ]),
        Master("M1-DAC", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/DAC/M1_DAC", [
            {"ue": "MLBDA",  "semester": 1}
        ]),
        
        # Master 2
        Master("M2-RES", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/RES/M2_RES", [
            {"ue": "SECRES",  "semester": 3}
        ]),
        Master("M2-SAR", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/SAR/M2_SAR", [
            {"ue": "ARA",  "semester": 3},
            {"ue": "DATACLOUD",  "semester": 3},
            {"ue": "NVM",  "semester": 3},
            {"ue": "ASTRE",  "semester": 3},
            
        ]),
        Master("M2-SESI", "https://cal.ufr-info-p6.jussieu.fr/caldav.php/SESI/M2_SESI", [
            {"ue": "PACC",  "semester": 3},
            {"ue": "SMC",  "semester": 3},
        ]),
    ]

    with open(f"{publish_dir}/link.md", 'w') as f:
        f.write("".join(calendar.to_markdown() for calendar in calendars))

    with open(f"{publish_dir}/calendars.json", 'w') as f:
        json.dump([calendar.to_json() for calendar in calendars], f)

    shutil.copy("index.html", f"{publish_dir}/index.html")


if __name__ == '__main__':
    main()
