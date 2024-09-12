from datetime import datetime, timezone
from ics import Calendar
from typing import Dict


from lib import (
    load_calendar_from_file,
    load_calendar_from_url,
    display_events,
    filter_events_by_name,
    save_calendars,
    filter_events_by_date_range,
    merge_calendars
)

from lib_noyau import get_noyau_calendars


# URL of the CalDAV resource
url = 'https://cal.ufr-info-p6.jussieu.fr/caldav.php/SAR/M1_SAR'

# Replace 'username' and 'password' with your correct credentials
username = 'student.master'
password = 'guest'


# Main logic
def main() -> None:
    # Load the calendar from a file or a URL
    raw_calendar = load_calendar_from_file('evenement.ics')
    # raw_calendar = load_calendar_from_url(url, username, password)

    # Filter events by date range
    start_date = datetime(2024, 9, 1, tzinfo=timezone.utc)
    end_date = datetime(2024, 12, 31, tzinfo=timezone.utc)
    raw_calendar = filter_events_by_date_range(raw_calendar, start_date, end_date)

    # Display the events in the calendar
    #display_events(raw_calendar)

    # Define filters to create separate calendars
    filters = ["NOYAU", "PSCR"]
    filtered_calendars: Dict[str, Calendar] = filter_events_by_name(raw_calendar, filters)


    save_calendars(get_noyau_calendars(filtered_calendars["NOYAU"]), "m1/sar/noyau")


if __name__ == '__main__':
    main()
