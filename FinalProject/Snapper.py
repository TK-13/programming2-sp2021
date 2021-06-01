""" API Imports: these are required to interface with the Google Drive API
https://developers.google.com/drive/api/v3/quickstart/python """
from __future__ import print_function
import pickle
import os.path
from apiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Imports: GPIOZERO for input/output devices, picamera for controlling PiCamera, time for creating
# pauses (ex. when camera waits to see if user wants to stop), PIL for converting images into PDFs
from time import sleep
from PIL import Image
from picamera import PiCamera
from gpiozero import Button, LED, LightSensor

# Version 2 Imports: pygame for new interface
import pygame

# Devices: These define the different hardware devices used with the Snap, using the GPIO library. The PiCamera
# required that the rotation setting, which is part of the picamera library, be set to 90 degrees from default due to
# it's stand mount.

# The LEDs had to be grouped into lists, to make it easier to control large groups of them with fewer lines of code.
# This also allowed for some fun lighting patterns, such as the upload progress bar and PDF conversion indicator.
cam = PiCamera()
cam.rotation = 180

# btn = Button(26)
# btn2 = Button(19)

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200

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

PROGRESS_BAR = [ledA, ledB, ledC, ledD, ledE]
for i in PROGRESS_BAR:
    i.off()

GREEN_LIGHTS = [ledC, ledD, ledE]

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
imagelist = []
pdf_tally_path = '/home/pi/testtest.txt'


def loading(greenlight):
    c = -1
    f = 1
    for i in range(11):
        sleep(0.2)
        c += f
        greenlight[c].on()
        greenlight[c - f].off()
        if c >= 2:
            f = -1
        elif c <= 0:
            f = 1
        sleep(0.2)
    for b in greenlight:
        b.off()


# This function is just mean to make it easier to put the datasets into a string.
def read_data(path):
    file_for_read = open(path)
    content = file_for_read.read()
    file_for_read.close()
    return content


# Adaptive Lighting: one of my pet peeves is having bad lighting when taking a picture of a homework submission.
# The Snap gauges the ambient light using the light sensor, and turns on none, some, or all of the while overhead-mounted
# LEDs accordingly.
def adaptive_lighting(lights):
    ldr.wait_for_light(3)
    if boundary[0] >= ldr.value >= 0:
        for q in lights:
            q.on()
    elif boundary[1] >= ldr.value >= boundary[0]:
        for q in lights:
            q.off()
        for q in halflist:
            q.on()
    elif ldr.value >= boundary[1]:
        for q in lights:
            q.off()


# Image to pdf conversion: this is where the PIL library comes into play. Each photo is defined as an Image, using the names saved from
# earlier. All images are appended to the ready list, except for the first. Then, the first image is saved as the PDF, while the other
# images are added on. This way, the PDF stays in order.
def convert_pdfs(names, storing_list, ready, tally):
    # print()
    # print("--Starting PDF Conversion--")
    for q in names:
        image = Image.open(str(q))
        im1 = image.convert('RGB')
        out = im1.rotate(-90)
        storing_list.append(out)

    for j in storing_list[1:]:
        ready.append(j)

    # pdf_name = input("Enter PDF name: ")
    storing_list[0].save(r'/home/pi/Desktop/TransferFiles/' + str(tally) + '.pdf', save_all=True, append_images=ready)
    tally += 1  # ^^^ PDF NAMES


def keyboard_input(target_key):
    # print("Keyboard input function reached")
    # sleep(3)
    # print("Delay period expired")
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == target_key:
                print("%s Triggered" % target_key)
                return True
        else:
            print("Event not triggered")
            return False


def main():
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Window")

    run = True
    i = 0
    tally = int(read_data(pdf_tally_path))
    print(tally)
    cam.start_preview(fullscreen=False, window=(300, 200, 640, 480))

    while run:
        take_pic = keyboard_input(pygame.K_a)
        if take_pic:
            print("Button a triggered")
            cam.capture('/home/pi/Desktop/hw%s.jpg' % (str(i)))
            namelist.append('/home/pi/Desktop/hw%s.jpg' % (str(i)))
            i += 1
        
        user_quits = keyboard_input(pygame.K_q)
        if user_quits:
            run = False
            print(run)
            break
        
        
#         adaptive_lighting(lightlist)

        # Capture Loop: every time the left button is pressed, the camera takes a picture, whose name is saved to one
        # of the PDF Conversion lists for later. Then, the user has three seconds (indicated by the green LEDs) to
        # either stop the loop by holding the right button, or to let it continue, in which case the program
        # reevaluates the lighting and re-prompts the user to take a picture.

        # for item in GREEN_LIGHTS:
        #     item.on()

        # print("\nWaiting for button a.")
        # sleep(3)
        # print("Delay period expired")
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_a:
        #             print("Button a Triggered")
        #             for item in GREEN_LIGHTS:
        #                 item.off()
        #             sleep(1)
        #             cam.capture('/home/pi/Desktop/hw%s.jpg' % (str(i)))
        #             namelist.append('/home/pi/Desktop/hw%s.jpg' % (str(i)))
        #             i += 1
        #     else:
        #         print("Event not triggered")


#         take_pic = keyboard_input(pygame.K_a)
#         if take_pic:
#             print("Button a triggered")
#             cam.capture('/home/pi/Desktop/hw%s.jpg' % (str(i)))
#             namelist.append('/home/pi/Desktop/hw%s.jpg' % (str(i)))
#             i += 1

#         print("\nProceeding 1")

        # for item in GREEN_LIGHTS:
        #     sleep(1)
        #     item.on()

        # print("Waiting for button s")
        # sleep(3)
        # print("Delay period expired")
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_s:
        #             print("Button S Triggered")
        #             run = False
        #             for item in GREEN_LIGHTS:
        #                 item.on()
        #             sleep(1)
        #         else:
        #             print("\nProceeding 2. Looping program.")

#     button_s = keyboard_input(pygame.K_s)
#     if button_s:
#         print("button 2 true, but button 2 False?")
#         run = False
#         # for item in GREEN_LIGHTS:
#         #     item.on()
#         #     sleep(1)
#     print("\nProceeding 2. Looping program.")

    cam.stop_preview()
    cam.close()
    print("/nCamera Off")

    # for item in lightlist:
    #     item.off()
    # for item in GREEN_LIGHTS:
    #     item.off()

    convert_pdfs(namelist, dummylist, readylist, tally)
    # loading(GREEN_LIGHTS)

    # Drive API Credentials: this is where the user is authorized to use the Drive API. If they don't have token.pickle
    # (if they've never used the Snap before), they will be prompted to log into their google account. A new
    # token.pickle file is created, which stores the user's access and refresh tokens. SCOPES determines what the user
    # does and does not have permission to do. Although the scope can be narrowed down, this broad-access one was the
    # only one that worked.
    # From this point forward, Ms. Ifft helped me a lot with the code and figuring out the API.

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/drive']
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            credentials = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    service = build('drive', 'v3', credentials=credentials)

    # look for a specific folder and get its id
    page_token = None
    folder_name = "File Transfer"
    folder_id = None

    # q means query. If there are a lot of results, Google sends first x results, and a Token of where it left off.
    # This makes the program continue to query until there are no more results
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

        # ID saved to send file to correct folder, regardless of name. Prints name and behind-scenes ID.
        # Folders can have same name, but all have unique IDs
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

    # check if file with same name already exists
    file_to_upload_path = '/home/pi/Desktop/TransferFiles/' + str(tally) + '.pdf'  # <<< PDF NAMES
    name_of_uploaded_file = ('hw%s.pdf' % tally)
    response = service.files().list(
        q="trashed = false and name = '" + name_of_uploaded_file + "' and parents in '" + str(folder_id) + "'",
        spaces='drive',
        fields='nextPageToken, files(id, name)',
        pageToken=page_token).execute()

    # this query checks if there's already a file with that name. 'trashed = false', and omits results found in Trash.
    # If no response(no pre-existing file), returns None
    files = response.get('files', [])
    if files:
        print("There is already a file with that name in File Transfer")
        # ledB.on()
    else:
        file_metadata = {'name': name_of_uploaded_file, 'parents': [folder_id]}
        media = MediaFileUpload(file_to_upload_path, mimetype='application/pdf')
        # for progress in PROGRESS_BAR:
        #     progress.on()
        #     sleep(0.2)

        # Upload: this is where the program uses the "create" method from the Drive API. If the file is missing it's
        # ID, or has no size, (which might indicate an upload issue in which content was damaged), the program throws
        # an error LED.
        # Communicating with the Drive API to figure out just what error happened, or whether there was an upload
        # issue, was challenging, so we decided to use this general try/except, so that any issue will
        # result in the error going off.
        try:
            file = service.files().create(body=file_metadata,
                                          media_body=media,
                                          fields='id, size').execute()
            if not file.get("id") or file.get("size") == 0:
                print("Incomplete Upload")
                # ledB.on()
                # for x in range(5):
                #     ledB.toggle()
        except:
            # ledA.on()
            print("An error occurred")

        sleep(2)
        # for light in PROGRESS_BAR:
        #     light.off()

        tally_rewrite = open(pdf_tally_path, 'w')
        print(tally)
        tally_rewrite.write(str(tally))
        tally_rewrite.close()


if __name__ == '__main__':
    main()
