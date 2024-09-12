import os
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
from ics import Calendar
from typing import Dict, List


def load_calendar_from_file(filename: str) -> Calendar:
    """Load the calendar from an ICS file."""
    try:
        with open(filename, 'r') as f:
            raw_calendar = Calendar(f.read())
        return raw_calendar
    except FileNotFoundError:
        print(f"File {filename} not found.")
        exit(1)


def load_calendar_from_url(url: str, username: str, password: str) -> Calendar:
    """Load the calendar from a CalDAV URL."""
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
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


def filter_events_by_name(calendar: Calendar, filters: List[str]) -> Dict[str, Calendar]:
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


def save_calendars(calendars: Dict[str, Calendar], path: str = "") -> None:
    """Save the filtered calendars to separate ICS files, creating directories if needed."""

    # Create the directory if it doesn't exist
    full_path = os.path.join("../docs", path)
    os.makedirs(full_path, exist_ok=True)

    # Iterate over the filtered calendars and save each one
    for name, cal in calendars.items():
        filename = os.path.join(full_path, f"calendar_{name}.ics")
        with open(filename, 'w') as f:
            ics_content = cal.serialize()  # Correctly handle ics serialization
            f.write(ics_content)
            print(f"Calendar '{name}' saved to file '{filename}'.")


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


def merge_calendars(calendars: List[Calendar]) -> Calendar:
    """Merge multiple calendars into a single calendar by combining all events."""
    merged_calendar = Calendar()

    # Iterate over each calendar and add all its events to the merged calendar
    for calendar in calendars:
        for event in calendar.events:
            merged_calendar.events.add(event)

    return merged_calendar
