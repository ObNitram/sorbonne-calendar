from ics import Calendar

from requests.auth import HTTPBasicAuth

from core.lib import (
    filter_events_by_name,
    load_calendar_from_url,
    filter_events_by_date_range,
    get_school_year_dates,
    get_filtered_calendars_from_url
)

from core.UE import UE

class Master :
    name: str = ""
    ues: list[UE] = []
    def __init__(self, master: str, input_url: str, ues: list[dict]):
        # ues is now a list of dictionaries with keys: 'name', 'year', 'semester'

        calendar = get_filtered_calendars_from_url(input_url)
        filtered_calendars: dict[str, Calendar] = filter_events_by_name(calendar, [ue['ue'] for ue in ues])

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
