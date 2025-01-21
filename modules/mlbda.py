from ics import Calendar
from typing import Dict

from core.lib import (
    filter_events_by_name,
    merge_calendars
)


def get_mlbda_calendars(raw_calendar: Calendar) -> Dict[str, Calendar]:
    course_type_filters = ["Cours", "TD1", "TD2", "TD3", "TME1", "TME2", "TME3"]
    filtered_calendars = filter_events_by_name(raw_calendar, course_type_filters)

    group1 = merge_calendars([
        filtered_calendars["Cours"],
        filtered_calendars["TD1"],
        filtered_calendars["TME1"],
        filtered_calendars["default"]
    ])

    group2 = merge_calendars([
        filtered_calendars["Cours"],
        filtered_calendars["TD2"],
        filtered_calendars["TME2"],
        filtered_calendars["default"]
    ])

    group3 = merge_calendars([
        filtered_calendars["Cours"],
        filtered_calendars["TD3"],
        filtered_calendars["TME3"],
        filtered_calendars["default"]
    ])

    return {
        "group1": group1,
        "group2": group2,
        "group3": group3,
    }
