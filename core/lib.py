import os
import requests
from datetime import datetime, timezone
from ics import Calendar

from requests.auth import HTTPBasicAuth
from core.config import publish_dir, username, password

auth = HTTPBasicAuth(username, password)

def get_filtered_calendars_from_url(url: str) -> Calendar:
    raw_calendar = load_calendar_from_url(url, auth)
    return filter_events_by_date_range(raw_calendar, *get_school_year_dates())

def load_calendar_from_file(filename: str) -> Calendar:
    """Load the calendar from an ICS file."""
    try:
        with open(filename, 'r') as f:
            raw_calendar = Calendar(f.read())
        return raw_calendar
    except FileNotFoundError:
        print(f"File {filename} not found.")
        exit(1)


def load_calendar_from_url(url: str, auth: HTTPBasicAuth) -> Calendar:
    """Load the calendar from a CalDAV URL."""
    response = requests.get(url, auth=auth)
    if response.status_code != 200:
        print(f"Error accessing URL: {response.status_code}")
        exit(1)
    return Calendar(response.text)


def display_events(calendar: Calendar) -> None:
    """Display the events in the calendar."""
    for event in calendar.events:
        print(f"Event Title : {event.name}")
        print(f"Start Date : {event.begin}")
        print(f"End Date : {event.end}")
        print(f"Description : {event.description}")
        print(f"Location : {event.location}")
        print("=" * 40)


def filter_events_by_name(calendar: Calendar, filters: list[str]) -> dict[str, Calendar]:
    """Filter the events in the calendar by name and return a 'default' calendar for unmatched events."""
    # Initialize the filtered calendars with a "default" calendar for unmatched events
    filtered_calendars: Dict[str, Calendar] = {filter: Calendar() for filter in filters}
    filtered_calendars["default"] = Calendar()  # Add a default calendar for unmatched events

    # Iterate through the events in the calendar
    for event in calendar.events:
        event_name = event.name
        added_to_filter = False

        # Check if the event matches any of the filters
        for keyword, filtered_calendar in filtered_calendars.items():
            if keyword != "default" and keyword in event_name:  # Skip the default calendar
                filtered_calendar.events.add(event)
                added_to_filter = True
                break  # Once the event is added, no need to check other filters

        # If the event was not added to any filtered calendar, add it to the default
        if not added_to_filter:
            filtered_calendars["default"].events.add(event)

    return filtered_calendars


def save_calendars(calendars: dict[str, Calendar], path: str = "") -> dict[str, str]:
    """Save the filtered calendars to separate ICS files, creating directories if needed."""

    # Create the directory if it doesn't exist
    full_path = os.path.join(publish_dir, path)
    os.makedirs(full_path, exist_ok=True)

    # paths
    paths: dict[str, str] = {}

    # Iterate over the filtered calendars and save each one
    for name, cal in calendars.items():
        filename = f"{path.replace('/', '-')}-{name}.ics"
        filename_and_path = os.path.join(full_path, filename)
        with open(filename_and_path, 'w') as f:
            ics_content = cal.serialize()
            f.write(ics_content)
            paths[name] = (os.path.join(path, filename))

    return paths


def filter_events_by_date_range(calendar: Calendar, start_date: datetime, end_date: datetime) -> Calendar:
    """Filter events in the calendar that occur between the specified start and end dates."""
    filtered_calendar = Calendar()

    # Iterate through the events in the calendar
    for event in calendar.events:
        event_start = event.begin.datetime

        # Check if the event's start date is within the specified range
        if start_date <= event_start <= end_date:
            filtered_calendar.events.add(event)

    return filtered_calendar


def merge_calendars(calendars: list[Calendar]) -> Calendar:
    """Merge multiple calendars into a single calendar by combining all events."""
    merged_calendar = Calendar()

    # Iterate over each calendar and add all its events to the merged calendar
    for calendar in calendars:
        for event in calendar.events:
            merged_calendar.events.add(event)

    return merged_calendar


def write_links_to_file(paths: dict[str,str], link_file: str, host: str, title: str) -> None:
    """Write the links to the file."""
    with open(link_file, 'a') as f:
        f.write(f"## {title}\n")
        for name, path in paths.items():
            f.write(f"### {name}\n")
            f.write(f"{host}{path}\n\n")
        f.write(f"\n")


def write_string_to_file(content: str, file: str) -> None:
    """Write the content to the file."""
    with open(file, 'a') as f:
        f.write(content)

def get_school_year_dates():
    """Détermine dynamiquement les dates de début et de fin de l'année scolaire actuelle."""
    today = datetime.now(timezone.utc)
    current_year = today.year

    if today.month >= 9:  # Année scolaire commence en septembre de l'année actuelle
        start_date = datetime(current_year, 9, 1, tzinfo=timezone.utc)
        end_date = datetime(current_year + 1, 6, 30, tzinfo=timezone.utc)
    else:  # Année scolaire a commencé en septembre de l'année précédente
        start_date = datetime(current_year - 1, 9, 1, tzinfo=timezone.utc)
        end_date = datetime(current_year, 6, 30, tzinfo=timezone.utc)

    return start_date, end_date