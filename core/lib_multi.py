#from ics import Calendar
import icalendar
from typing import Dict

from core.lib import (
    filter_events_by_name,
    merge_calendars
)


def get_multi_calendars(raw_calendar: Calendar) -> Dict[str, Calendar]:
    course_type_filters = ["Cours", "Anglais-Cours", "TME"]
    filtered_calendars = filter_events_by_name(raw_calendar, course_type_filters)

    francais = merge_calendars([
        filtered_calendars["Cours"],
        filtered_calendars["TME"],
        filtered_calendars["default"]
    ])

    anglais = merge_calendars([
        filtered_calendars["Anglais-Cours"],
        filtered_calendars["TME"],
        filtered_calendars["default"]
    ])

    return {
        "Français": francais,
        "Anglais": anglais
    }
