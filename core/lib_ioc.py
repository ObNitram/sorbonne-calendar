import icalendar
#from ics import Calendar
from typing import Dict

from core.lib import (
    filter_events_by_name,
    merge_calendars
)


def get_ioc_calendars(raw_calendar: Calendar) -> Dict[str, Calendar]:
    course_type_filters = ["Cours", "TME"]
    filtered_calendars = filter_events_by_name(raw_calendar, course_type_filters)

    group1 = merge_calendars([
        filtered_calendars["Cours"],
        filtered_calendars["TME"],
        filtered_calendars["default"]
    ])
    return {
        "group1": group1
    }
