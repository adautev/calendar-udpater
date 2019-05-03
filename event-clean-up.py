from __future__ import print_function

import argparse

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime

# Setup the Calendar API
from utilities.calendar_title_parser import CalendarTitleParser

parser = argparse.ArgumentParser(description='Google Calendar Parser')
parser.add_argument('-c', '--create-credentials', dest='create_credentials',
                    help='Use client secret generated from your Google Project to obtain service credentials')

args = parser.parse_args()
store = file.Storage('credentials/oogle-service-account.json')
SCOPES = 'https://www.googleapis.com/auth/calendar'


def run_oauth_authorization():
    global creds
    flow = client.flow_from_clientsecrets('credentials/client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)


if args.create_credentials != None:
    run_oauth_authorization()

creds = store.get()
if not creds or creds.invalid:
    run_oauth_authorization()

service = build('calendar', 'v3', http=creds.authorize(Http()))

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

before = datetime.datetime.utcnow() + datetime.timedelta(days=-220)
before=before.isoformat() + 'Z'  # 'Z' indicates UTC time
print('Setting events visivility to public')
events_result = service.events().list(calendarId='primary', timeMin=before,
                                      maxResults=100,
                                      singleEvents=True).execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    event['visibility'] = 'public'
    if CalendarTitleParser.calendar_title_should_be_changed(event['summary']):
        event['summary'] = CalendarTitleParser.clean_up_calendar_title(event['summary'])
    updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()
    print('Updated: ' + updated_event['summary'])
