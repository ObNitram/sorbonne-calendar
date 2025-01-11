from ics import Calendar
from typing import Dict

from core.lib import (
    filter_events_by_name,
    merge_calendars
)


def get_sftr_calendars(raw_calendar: Calendar) -> Dict[str, Calendar]:
    course_type_filters = [ "Cours", "TD", "TP"]
    filtered_calendars = filter_events_by_name(raw_calendar, course_type_filters)

    group1 = merge_calendars([
        filtered_calendars["Cours"],
        filtered_calendars["TD"],
        filtered_calendars["TP"],
        filtered_calendars["default"]
    ])

    return {
        "group1": group1
    }
