from ics import Calendar
from typing import Dict

from core.lib import (
    filter_events_by_name,
    merge_calendars
)


def get_sc_calendars(raw_calendar: Calendar) -> Dict[str, Calendar]:
    class_type_filters = ["Cours", "TME 1", "TME 2"]
    filtered_calendars = filter_events_by_name(raw_calendar, class_type_filters)

    group1 = merge_calendars([
        filtered_calendars["Cours"],
        filtered_calendars["TME 1"],
        filtered_calendars["default"]
    ])

    group2 = merge_calendars([
        filtered_calendars["Cours"],
        filtered_calendars["TME 2"],
        filtered_calendars["default"]
    ])

    return {
        "group1": group1,
        "group2": group2,
    }
