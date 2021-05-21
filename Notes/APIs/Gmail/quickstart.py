# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gmail_quickstart]
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API to get labels
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

    # Call the Gmail API to get messages
    # https://support.google.com/mail/answer/7190?hl=en
    result = service.users().messages().list(userId='me', q='(college university)').execute()
    messages = result.get('messages')
    next_page_token = result.get('nextPageToken')
    counter = 0
    while next_page_token:
        counter += len(messages)
        for msg in messages:
            # Get the message from its id
            txt = service.users().messages().get(userId='me', id=msg['id']).execute()

            # Get value of 'payload' from dictionary 'txt'
            payload = txt['payload']
            headers = payload['headers']
        result = service.users().messages().list(userId='me', q='(college university)', pageToken=next_page_token).execute()
        messages = result.get('messages')
        next_page_token = result.get('nextPageToken')
        print(counter)
        print(str(next_page_token))

            # body is in payload['body'] but needs to be decoded; mimeType is in payload['mimeType']


if __name__ == '__main__':
    main()
# [END gmail_quickstart]