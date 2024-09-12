from ics import Calendar
from typing import Dict

from core.lib import (
    filter_events_by_name,
    merge_calendars
)


def get_noyau_calendars(raw_calendar: Calendar) -> Dict[str, Calendar]:
    noyau_filters = ["cours", "TD1", "TD2", "TD3"]
    noyau_filtered_calendars = filter_events_by_name(raw_calendar, noyau_filters)

    group1 = merge_calendars([
        noyau_filtered_calendars["cours"],
        noyau_filtered_calendars["TD1"],
        noyau_filtered_calendars["default"]
    ])

    group2 = merge_calendars([
        noyau_filtered_calendars["cours"],
        noyau_filtered_calendars["TD2"],
        noyau_filtered_calendars["default"]
    ])

    group3 = merge_calendars([
        noyau_filtered_calendars["cours"],
        noyau_filtered_calendars["TD3"],
        noyau_filtered_calendars["default"]
    ])

    # Save each filtered calendar to a separate ICS file
    return {
        "group1": group1,
        "group2": group2,
        "group3": group3,
    }