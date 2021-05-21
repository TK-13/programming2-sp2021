'''
API Imports: these are required to interface with the Google Drive API
https://developers.google.com/drive/api/v3/quickstart/python
'''
from __future__ import print_function
import pickle
import os.path
from apiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

'''
Imports: GPIOZERO for input/output devices, picamera for controlling PiCamera, time for creating
pauses (ex. when camera waits to see if user wants to stop), PIL for converting images into PDFs
'''
from gpiozero import Button, LED, LightSensor
from time import sleep
from PIL import Image
import random
try:
    from picamera import PiCamera

except:
    print("Picamera doesn't work. Dummy Picam on.")
    dummy_picam = True

'''
Devices: These define the different hardware devices used with the Snap, using the GPIO library. The PiCamera required that
the rotation setting, which is part of the picamera library, be set to 90 degrees from default due to it's stand mount.

The LEDs had to be grouped into lists, to make it easier to control large groups of them with fewer lines of code. This also allowed
for some fun lighting patterns, such as the upload progress bar and PDF conversion indicator.
'''
if not dummy_picam:
    cam = PiCamera()
    cam.rotation = 180
else:

btn = Button(26)
btn2 = Button(19)

led = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(10)
led5 = LED(23)
led6 = LED(18)
led7 = LED(15)
led8 = LED(24)
lightlist = [led, led2, led3, led4, led5, led6, led7, led8]
halflist = [led, led3, led5, led7]

ledA = LED(16)
ledB = LED(12)
ledC = LED(7)
ledD = LED(8)
ledE = LED(25)

progressbar = [ledA, ledB, ledC, ledD, ledE]
for i in (progressbar):
    i.off()

greenlight = [ledC, ledD, ledE]


def loading():
    greenlight = [ledC, ledD, ledE]
    c = -1
    f = 1
    for i in range(11):
        sleep(0.5)
        c += f
        greenlight[c].on()
        greenlight[c - f].off()
        if c >= 2:
            f = -1
        elif c <= 0:
            f = 1
        sleep(0.5)
    for b in greenlight:
        b.off()


ldr = LightSensor(20)
ldr.threshold = 0.6
boundary = [0.6, 0.7]

'''
PDF Conversion lists: these are where the names of each photo taken by the camera will be stored whenever the program is run,
so that they're kept in the proper order for conversion into a single PDF. The tally variable adds a random number between 0-500
to the end of the pdf's title, to prevent files with the same name from being uploaded. 
'''
photolist = []
namelist = []
dummylist = []
readylist = []
tally = random.randrange(0, 500)
imagelist = []


def main():
    run = True
    i = 0

    cam.start_preview(fullscreen=False, window=(300, 200, 640, 480))

    while run == True:

        '''
        Adaptive Lighting: one of my pet peeves is having bad lighting when taking a picture of a homework submission. The Snap gauges the
        ambient light using the light sensor, and turns on none, some, or all of the while overhead-mounted LEDs accordingly. 
        '''
        ldr.wait_for_light(3)
        if ldr.value >= 0 and ldr.value <= boundary[0]:
            for q in lightlist:
                q.on()
        elif ldr.value >= boundary[0] and ldr.value <= boundary[1]:
            for q in lightlist:
                q.off()
            for q in halflist:
                q.on()
        #         print("Light setting: intermediate")
        elif ldr.value >= boundary[1]:
            for q in lightlist:
                q.off()
        #         print("Light setting: off")
        '''
        Capture Loop: every time the left button is pressed, the camera takes a picture, whose name is saved to one of the PDF Conversion
        lists for later. Then, the user has three seconds (indicated by the green LEDs) to either stop the loop by holding the right
        button, or to let it continue, in which case the program reevaluates the lighting and re-prompts the user to take a picture.
        '''
        for item in greenlight:
            item.on()
        btn.wait_for_press()
        for item in greenlight:
            item.off()
        sleep(1)
        cam.capture('/home/pi/Desktop/hw%s.jpg' % (str(i)))
        namelist.append('/home/pi/Desktop/hw%s.jpg' % (str(i)))
        i += 1
        #     print("Do you want to stop (press button2)?")
        for item in greenlight:
            sleep(1)
            item.on()
        if btn2.is_pressed == True:
            run = False
        else:
            #             print("Camera ready")
            for item in greenlight:
                item.on()
                sleep(1)
    #         continue

    cam.stop_preview()
    cam.close()

    for item in lightlist:
        item.off()
    for item in greenlight:
        item.off()

    '''
    Image to pdf conversion: this is where the PIL library comes into play. Each photo is defined as an Image, using the names saved from
    earlier. All images are appended to the ready list, except for the first. Then, the first image is saved as the PDF, while the other
    images are added on. This way, the PDF stays in order.
    '''
    # print()
    # print("--Starting PDF Conversion--")
    for q in namelist:
        image = Image.open(str(q))
        im1 = image.convert('RGB')
        out = im1.rotate(-90)
        dummylist.append(out)

    for j in dummylist[1:]:
        readylist.append(j)

    dummylist[0].save(r'/home/pi/Desktop/raw.pdf', save_all=True, append_images=readylist)
    loading()

    '''
    Drive API Credentials: this is where the user is authorized to use the Drive API. If they don't have token.pickle (if they've never
    used the Snap before), they will be prompted to log into their google account. A new token.pickle file is created, which stores
    the user's access and refresh tokens. SCOPES determines what the user does and does not have permission to do. Although the scope can
    be narrowed down, this broad-access one was the only one that worked.

    From this point forward, Ms. Ifft helped me a lot with the code and figuring out the API.
    '''
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/drive']
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
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

    #     print()

    # look for a specific folder and get its id

    page_token = None
    folder_name = "File Transfer"
    folder_id = None
    '''
    q means query. If there are a lot of results, Google sends first x results, and a Token of where it left off.
    This makes the program continue to query until there are no more results
    '''
    while True:

        response = service.files().list(
            q="mimeType='application/vnd.google-apps.folder' and name = '" + folder_name + "'",
            spaces='drive',
            fields='nextPageToken, files(id, name)',
            pageToken=page_token).execute()
        for file in response.get('files', []):
            # Process change
            folder_id = file.get('id')
            # print('Found folder: %s (%s)' % (file.get('name'), file.get('id')))

        '''
        ID saved to send file to correct folder, regardless of name. Prints name and behind-scenes ID.
        Folders can have same name, but all have unique IDs
        '''

        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    #     print()
    #     print()

    # check if file with same name already exists
    file_to_upload_path = '/home/pi/Desktop/raw.pdf'
    name_of_uploaded_file = ('hw%s.pdf' % (int(tally)))
    response = service.files().list(
        q="trashed = false and name = '" + name_of_uploaded_file + "' and parents in '" + str(folder_id) + "'",
        spaces='drive',
        fields='nextPageToken, files(id, name)',
        pageToken=page_token).execute()
    '''
    this query checks if there's already a file with that name. 'trashed = false', and omits results found in Trash. If no response
    (no pre-existing file), returns None
    '''
    files = response.get('files', [])
    if files:
        ledB.on()
        # print("File with name {0} in {1} already exists!".format(name_of_uploaded_file, folder_name))
        # print('File info: %s (%s)' % (files[0].get('name'), files[0].get('id')))
        # ^^ this was old diagnostic code, which told the user what happened with text. This has been replaced with LED indicators.
    else:
        #         print("File with name {0} does not exist in {1}.".format(name_of_uploaded_file, folder_name))

        # do the upload
        #         print()
        # print("Uploading file with name {0} to folder {1}".format(name_of_uploaded_file, folder_name))
        file_metadata = {'name': name_of_uploaded_file, 'parents': [folder_id]}
        media = MediaFileUpload(file_to_upload_path, mimetype='application/pdf')
        for i in (progressbar):
            i.on()
            sleep(1)

        '''
        Upload: this is where the program uses the "create" method from the Drive API. If the file is missing it's ID, or has no size,
        (which might indicate an upload issue in which content was damaged), the program throws an error LED.

        Communicating with the Drive API to figure out just what error happened, or whether there was an upload issue, was challenging,
        so we decided to put this whole upload in a try/except, so that any issue will result in the Red LED going off.
        '''
        try:
            file = service.files().create(body=file_metadata,
                                          media_body=media,
                                          fields='id, size').execute()
            if not file.get("id") or file.get("size") == 0:
                ledB.on()
                for i in range(5):
                    ledB.toggle()
        except:
            ledA.on()
            print("An error occurred")

        #         file.get('id')
        #         print(file)

        sleep(2)

        #         print()

        for i in (progressbar):
            i.off()


#     print()
#     print()

if __name__ == '__main__':
    main()
