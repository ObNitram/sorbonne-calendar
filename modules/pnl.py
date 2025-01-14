from ics import Calendar
from typing import Dict

from core.lib import (
    filter_events_by_name,
    merge_calendars
)


def get_pnl_calendars(raw_calendar: Calendar) -> Dict[str, Calendar]:
    course_type_filters = ["Cours", "TD1", "TD2", "TME"]
    filtered_calendars = filter_events_by_name(raw_calendar, course_type_filters)

    group1 = merge_calendars([
        filtered_calendars["Cours"],
        filtered_calendars["TD1"],
        filtered_calendars["TME"],
        filtered_calendars["default"]
    ])

    group2 = merge_calendars([
        filtered_calendars["Cours"],
        filtered_calendars["TD2"],
        filtered_calendars["TME"],
        filtered_calendars["default"]
    ])

    return {
        "group1": group1,
        "group2": group2
    }
