import datetime
import os.path
from googleapiclient.discovery import build
from google.auth import load_credentials_from_file


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def calendar_info3():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # Load credential file for service account
    creds = load_credentials_from_file(
        'cistlt-calendar.json', SCOPES
    )[0]

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    # NOTE: Set your calendar id
    events_result = service.events().list(calendarId='cist.lt.club@gmail.com', timeMin=now,
                                        maxResults=3, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    schedule = []
    if not events:
        return -1
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        schedule.append((start, event['summary']))

    return schedule

def to_datetime(schedule):
    day_time = str(schedule[0]).split("T")
    sche_day = str(day_time[0]).split("-")
    sche_time = str(day_time[1]).split(":")

    return datetime.datetime(year=int(sche_day[0]), month=int(sche_day[1]), day=int(sche_day[2]), hour=int(sche_time[0]), minute=int(sche_time[1]))

def ctrl_index(now, schedule):
    for sche_index in range(3):
        if to_datetime(schedule[sche_index]) - now > datetime.timedelta(days=1):
            return sche_index
        
    return None

if __name__ == "__main__":
    # print(calendar_info3())
    print(to_datetime(calendar_info3()[ctrl_index(datetime.datetime.now(), calendar_info3())]))
