from ics import Calendar

from core.lib import (
    filter_events_by_name,
    get_filtered_calendars_from_url,
    display_events
)

input_url = "https://cal.ufr-info-p6.jussieu.fr/caldav.php/RES/M1_RES"
ue = "RTEL"

def main() -> None:
    calendar = get_filtered_calendars_from_url(input_url)
    filtered_calendars: dict[str, Calendar] = filter_events_by_name(calendar, [ue])

    display_events(filtered_calendars[ue])


if __name__ == '__main__':
    main()