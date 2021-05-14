# https://developers.google.com/drive/api/v3/quickstart/python

from __future__ import print_function
import multiprocessing
import pickle
import os.path
from apiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']  # TODO: there might be a more restrictive one?


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    print()

    # look for a specific folder and get its id

    page_token = None
    folder_name = "Teaching!"
    folder_id = None
    while True:
        response = service.files().list(
            q="mimeType='application/vnd.google-apps.folder' and name = '" + folder_name + "'",
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=page_token).execute()
        for file in response.get('files', []):
            # Process change
            folder_id = file.get('id')
            print('Found folder: %s (%s)' % (file.get('name'), file.get('id')))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    print()
    print()

    # check if file with same name already exists
    file_to_upload_path = 'samplefiles/sky.jpg'
    name_of_uploaded_file = 'sky.jpg'
    response = service.files().list(
        q="trashed = false and name = '" + name_of_uploaded_file + "' and parents in '" + folder_id + "'",
        spaces='drive',
        fields='nextPageToken, files(id, name)',
        pageToken=page_token).execute()
    files = response.get('files', [])
    if files:
        print("File with name {0} in {1} already exists!".format(name_of_uploaded_file, folder_name))
        print('File info: %s (%s)' % (files[0].get('name'), files[0].get('id')))
    else:
        print("File with name {0} does not exist in {1}.".format(name_of_uploaded_file, folder_name))

        # do the upload
        print()
        print("Uploading file with name {0} to folder {1}".format(name_of_uploaded_file, folder_name))
        file_metadata = {'name': name_of_uploaded_file, 'parents': [folder_id]}
        manager = multiprocessing.Manager()  # need these lines because we have a return value we care about
        return_dict = manager.dict()

        p = multiprocessing.Process(target=upload_file, args=(service, file_metadata, file_to_upload_path, return_dict))
        p.start()
        p.join(10)
        if p.is_alive():
            print("still running... let's kill it")
            p.kill()
            p.join()
        file = return_dict['file']
        print()
        if file.get('id'):
            print('File uploaded successfully. File ID: %s' % file.get('id'))
        else:
            print('File failed to upload!')

    print()
    print()


def upload_file(service, file_metadata, file_to_upload_path, return_dict):
    return_dict['file'] = {}
    media = MediaFileUpload(file_to_upload_path, mimetype='image/jpg')
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    return_dict['file'] = file


if __name__ == '__main__':
    main()

