from ics import Calendar
from typing import Dict

from core.lib import (
    filter_events_by_name,
    merge_calendars
)


def get_ares_calendars(raw_calendar: Calendar) -> Dict[str, Calendar]:
    course_type_filters = ["CS", "TME1", "TME3", "TME4"]
    filtered_calendars = filter_events_by_name(raw_calendar, course_type_filters)

    group1 = merge_calendars([
        filtered_calendars["CS"],
        filtered_calendars["TME1"],
        filtered_calendars["default"]
    ])

    group3 = merge_calendars([
        filtered_calendars["CS"],
        filtered_calendars["TME3"],
        filtered_calendars["default"]
    ])

    group4 = merge_calendars([
        filtered_calendars["CS"],
        filtered_calendars["TME4"],
        filtered_calendars["default"]
    ])

    return {
        "group1": group1,
        "group3": group3,
        "group4": group4,
    }
