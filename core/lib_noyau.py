from ics import Calendar
from typing import Dict, List

from lib import (
    load_calendar_from_file,
    load_calendar_from_url,
    display_events,
    filter_events_by_name,
    save_calendars,
    filter_events_by_date_range,
    merge_calendars
)


def get_noyau_calendars(raw_calendar: Calendar) -> Dict[str, Calendar]:
    noyau_filters = ["cours", "TD1", "TD2", "TD3"]
    noyau_filtered_calendars = filter_events_by_name(raw_calendar, noyau_filters)

    noyau_td1 = merge_calendars([
        noyau_filtered_calendars["cours"],
        noyau_filtered_calendars["TD1"],
        noyau_filtered_calendars["default"]
    ])

    noyau_td2 = merge_calendars([
        noyau_filtered_calendars["cours"],
        noyau_filtered_calendars["TD2"],
        noyau_filtered_calendars["default"]
    ])

    noyau_td3 = merge_calendars([
        noyau_filtered_calendars["cours"],
        noyau_filtered_calendars["TD3"],
        noyau_filtered_calendars["default"]
    ])

    # Save each filtered calendar to a separate ICS file
    return {
        "noyau_td1": noyau_td1,
        "noyau_td2": noyau_td2,
        "noyau_td3": noyau_td3,
    }
