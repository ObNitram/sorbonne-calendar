from ics import Calendar
from typing import Dict

from core.lib import (
    filter_events_by_name,
    merge_calendars
)


def get_ares_calendars(raw_calendar: Calendar) -> Dict[str, Calendar]:
    noyau_filters = ["CS", "TME1", "TME3", "TME4"]
    noyau_filtered_calendars = filter_events_by_name(raw_calendar, noyau_filters)


    group1 = merge_calendars([
        noyau_filtered_calendars["CS"],
        noyau_filtered_calendars["TME1"],
        noyau_filtered_calendars["default"]
    ])

    group3 = merge_calendars([
        noyau_filtered_calendars["CS"],
        noyau_filtered_calendars["TME3"],
        noyau_filtered_calendars["default"]
    ])

    group4 = merge_calendars([
        noyau_filtered_calendars["CS"],
        noyau_filtered_calendars["TME4"],
        noyau_filtered_calendars["default"]
    ])


    # Save each filtered calendar to a separate ICS file
    return {
        "group1": group1,
        "group3": group3,
        "group4": group4,
    }
