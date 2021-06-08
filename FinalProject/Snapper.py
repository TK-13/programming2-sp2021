# API Imports: these are required to interface with the Google Drive API
# https://developers.google.com/drive/api/v3/quickstart/python
from __future__ import print_function
import pickle
import os.path
from apiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Imports: GPIO ZERO for input/output devices, picamera for controlling PiCamera, time for creating
# pauses (ex. when camera waits to see if user wants to stop), PIL for converting images into PDFs
from time import sleep
from PIL import Image
from picamera import PiCamera
from gpiozero import Button, LED, LightSensor

# Pygame is used to take in keyboard button inputs, as well as input from digital buttons.
import pygame

WHITE = (255, 255, 255)
GRAY = (52, 52, 52)
BLACK = (0, 0, 0)
GREEN = (93, 202, 143)
RED = (201, 93, 98)
BLUE = (93, 131, 201)

mx = 0  # TODO: Do the pass thing.
my = 0

# These variables are meant to keep track of button coordinates.
button1x = 40
button2x = 160
button3x = 280
buttonY = 340

# Devices: These define the different hardware devices used with the Snap, using the GPIO library. The PiCamera
# required that the rotation setting, which is part of the picamera library, be set to 90 degrees from default due to
# it's stand mount.
cam = PiCamera()
cam.rotation = 180

# The LEDs had to be grouped into lists, to make it easier to control large groups of them with fewer lines of code.
# This also allowed for some fun lighting patterns, such as the upload progress bar and PDF conversion indicator.
led = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(10)
led5 = LED(23)
led6 = LED(18)
led7 = LED(15)
led8 = LED(24)
light_list = [led, led2, led3, led4, led5, led6, led7, led8]
half_light_list = [led, led3, led5, led7]

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

pdf_tally_path = '/home/pi/testtest.txt'


# This class makes a relatively simple button which players can interact with.
class PygameButton(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, color, surface, width=80, height=40, ):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x_pos
        self.rect.y = y_pos
        self.rect.width = width
        self.rect.height = height

        border_width = 4
        pygame.draw.line(surface, WHITE, (x_pos, y_pos - 2), (x_pos + width, y_pos - 2), border_width)
        pygame.draw.line(surface, WHITE, (x_pos, y_pos + height), (x_pos + width, y_pos + height), border_width)

        pygame.draw.line(surface, WHITE, (x_pos - 2, y_pos), (x_pos - 2, y_pos + height), border_width)
        pygame.draw.line(surface, WHITE, (x_pos + width, y_pos), (x_pos + width, y_pos + height), border_width)


# This function is meant to make it easier to make buttons, and also gives them a bit more life by having two
# different colors for when the cursor is/isn't in contact.
def add_button(x, y, mouse_x, mouse_y, buttons, color, surface, w=80, h=40):
    if x <= mouse_x <= (x + w) and y <= mouse_y <= (y + h):
        button = PygameButton(x, y, color, surface, w, h)
    else:
        button = PygameButton(x, y, BLACK, surface, w, h)
    buttons.add(button)


# This function is just mean to make it easier to read text files into a string.
def read_data(path):
    file_for_read = open(path)
    content = file_for_read.read()
    file_for_read.close()
    return content


# An old favorite function, used to validate certain command-line based user inputs, such as y/n questions.
def user_input(message, options_list, response="", options_message="Valid Inputs: ", print_options=False):
    if print_options:
        print(options_message)
        for option in options_list:
            print(option)
    entry = input(message)
    while entry not in options_list:
        print(response)
        entry = input(message)
    return entry


# Adaptive Lighting: a relic from Physical Computing.
# One of my pet peeves is having bad lighting when taking a picture of a homework submission.
# The HUT gauges the ambient light using the light sensor, and turns on none, some, or all of the while
# overhead-mounted LEDs accordingly.
def adaptive_lighting(lights):
    ldr.wait_for_light(3)
    if boundary[0] >= ldr.value >= 0:
        for q in lights:
            q.on()
    elif boundary[1] >= ldr.value >= boundary[0]:
        for q in lights:
            q.off()
        for q in half_light_list:
            q.on()
    elif ldr.value >= boundary[1]:
        for q in lights:
            q.off()


# Image to pdf conversion: this is where the PIL library comes into play. Each photo is defined as an Image, using the
# names saved from earlier (either within name_list, or within each value of the photo dictionary. All images are
# appended to the ready list, except for the first. Then, the first image is saved as the PDF, while the other
# images are added on. This way, the PDF stays in order.
def convert_pdf(names, storing_list, ready, tally_placeholder, custom_name=False):
    for q in names:  # TODO: consider streamlining.
        print(q)
        image = Image.open(str(q))
        im1 = image.convert('RGB')
        out = im1
        storing_list.append(out)

    for j in storing_list[1:]:
        ready.append(j)

    if custom_name:
        pdf_name = input("Enter PDF name: ")
    else:
        pdf_name = str(tally_placeholder)

    storing_list[0].save(r'/home/pi/Desktop/TransferFiles/' + pdf_name + '.pdf',
                         save_all=True, append_images=ready)
    # Clearing out the different lists allows this function to be reused. Otherwise, the order of the PDFs would be
    # completely scrambled (hypothetically of course. Definitely wasn't a problem for several days.
    names.clear()
    storing_list.clear()
    ready.clear()
    return pdf_name


# This function is meant to streamline the process of converting PDFs, given all the new complexities of Version 2.
# If there's only one group of photos, it only runs the conversion function once. But if there is more than one group,
# the function loops through every group in the dictionary.
# this also checks whether or not the user would like to enter custom names.
def multi_convert_check(photo_groups_place, tally_place, dummy_list_place, ready_list_place, final_pdf_list,
                        do_custom_names=False):
    print("\nConfirmed: multiple groups")
    for g in photo_groups_place:
        if do_custom_names:
            pdf_name = convert_pdf(photo_groups_place[g], dummy_list_place, ready_list_place, tally_place,
                                   custom_name=True)
            final_pdf_list.append(pdf_name)
        elif not do_custom_names:
            pdf_name = convert_pdf(photo_groups_place[g], dummy_list_place, ready_list_place, tally_place)
            final_pdf_list.append(pdf_name)
        photo_groups_place[g] = []
        tally_place += 1
    return tally_place, pdf_name


# Drive API functions: Ms. Ifft helped a lot with these functions last semester.
# This function is purely organizational, meant to tidy up the Google API code.
def authenticate_scopes():  # If modifying these scopes, delete the file token.pickle.
    scopes = ['https://www.googleapis.com/auth/drive']
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
                'credentials.json', scopes)
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
    return service, page_token, folder_id


# This function is designed to check if there are already files with the same name as the one the user is trying to
# upload. If there is one, it tells the user and aborts the upload; if not, it proceeds.
def redundancy_check_upload(service_place, page_token_place, folder_id_place, pdf_name_place):
    # check if file with same name already exists
    file_to_upload_path = '/home/pi/Desktop/TransferFiles/' + pdf_name_place + '.pdf'
    name_of_uploaded_file = (str(pdf_name_place) + '.pdf')
    response = service_place.files().list(
        q="trashed = false and name = '" + name_of_uploaded_file + "' and parents in '" + str(folder_id_place) + "'",
        spaces='drive',
        fields='nextPageToken, files(id, name)',
        pageToken=page_token_place).execute()

    # this query checks if there's already a file with that name. 'trashed = false', and omits results found in Trash.
    # If no response(no pre-existing file), returns None
    files = response.get('files', [])
    print("files 2: ", files, "\n")
    if files:
        print("There is already a file with that name in File Transfer")
        return True, True, True

    else:
        print("\nNo files exist with that name. Proceeding...")
        file_metadata = {'name': name_of_uploaded_file, 'parents': [folder_id_place]}
        media = MediaFileUpload(file_to_upload_path, mimetype='application/pdf')
        return False, file_metadata, media,


# Keyboard functions
# These functions consolidate the commands associated with each keyboard key, which also allows for the reuse of some
# actions, as you can see in key_q.
def key_a(names, current, place):
    cam.capture('/home/pi/Desktop/hw%s.jpg' % (str(place)))
    photo_id = '/home/pi/Desktop/hw%s.jpg' % (str(place))
    names.append(photo_id)
    current.append(photo_id)
    print(current)
    place += 1
    return photo_id, names, current, place


def key_z(current, photo_dict_place, num_place):
    transition_list = current.copy()
    photo_dict_place[num_place] = transition_list
    current.clear()
    num_place += 1
    print(photo_dict_place)
    print()
    return transition_list, current, photo_dict_place, num_place


def key_q(current, photo_dict_place, num_place):
    if current:  # Auto-save, if you forgot to make a final new group.
        do_auto_save = user_input(
            'You have ungrouped photos remaining. Would you like for them to be converted? ',
            ['y', 'n'])
        if do_auto_save == 'y':
            transition_list, current, photo_dict_place, num_place = key_z(current, photo_dict_place, num_place)
            return transition_list, current, photo_dict_place, num_place
    return [], current, photo_dict_place, num_place


def main():
    pygame.init()

    # PDF Conversion lists: these are where the names of each photo taken by the camera will be stored whenever the
    # program is run so that they're kept in the proper order for conversion into a single PDF. The tally variable
    # keeps track of how many pdfs have been made, in the event that the user does not want to make a custom name.
    current_photos_list = []
    name_list = []
    dummy_list = []
    ready_list = []
    all_pdfs = []
    # This dictionary is meant to keep track of every group of photos made, so each one can be made into an individual
    # pdf.
    photo_groups_dict = {}
    groups_num = 0

    button_list = pygame.sprite.Group()
    size = [400, 400]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Homework Upload Tool V2")
    run = True
    clock = pygame.time.Clock()

    num_photos_taken = 0
    tally = int(read_data(pdf_tally_path))  # Tally, the total number of PDFs made in the program's lifespan, is
    # rewritten to a text file after each use to keep track continuously. Upon initialization, this line brings the
    # program back to where it left off.
    cam.start_preview(fullscreen=False, window=(300, 200, 640, 480))
    # Theoretically, the user would be able to see what the PiCamera sees through a window. However, there have been
    # issues with that beyond code.

    # adaptive_lighting(light_list)

    # "Game Loop": as long as run is true, the computer will always respond appropriately when the user presses a key,
    # or clicks a digital button.
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    photo_id, name_list, current_photos_list, num_photos_taken = key_a(name_list,
                                                                                       current_photos_list,
                                                                                       num_photos_taken)

                elif event.key == pygame.K_z:
                    transition_list, current_photos_list, photo_groups_dict, groups_num = key_z(current_photos_list,
                                                                                                photo_groups_dict,
                                                                                                groups_num)

                elif event.key == pygame.K_q:
                    transition_list, current_photos_list, photo_groups_dict, groups_num = key_q(current_photos_list,
                                                                                                photo_groups_dict,
                                                                                                groups_num)

                    run = False
                    break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1x <= mx <= (button1x + 80) and buttonY <= my <= (buttonY + 40):
                    photo_id, name_list, current_photos_list, num_photos_taken = key_a(name_list, current_photos_list,
                                                                                       num_photos_taken)
                elif button2x <= mx <= (button2x + 80) and buttonY <= my <= (buttonY + 40):
                    print("Contact")
                    transition_list, current_photos_list, photo_groups_dict, groups_num = key_z(current_photos_list,
                                                                                                photo_groups_dict,
                                                                                                groups_num)

        if run:
            # These three lines keep track of the cursor's x and y position.
            mouse = pygame.mouse.get_pos()
            mx = mouse[0]
            my = mouse[1]

            # Drawing: this section continuously updates what the pygame window displays.
            screen.fill(GRAY)
            add_button(button1x, buttonY, mx, my, button_list, GREEN, screen)
            add_button(button2x, buttonY, mx, my, button_list, BLUE, screen)
            add_button(button3x, buttonY, mx, my, button_list, RED, screen)

            button_list.update()
            button_list.draw(screen)

            pygame.display.flip()
            clock.tick(60)

    cam.stop_preview()
    cam.close()
    print("\nCamera Off")

    # for item in light_list:
    #     item.off()

    custom_names = user_input('Would you like to enter a custom name? (y/n) ', ['y', 'n'],
                              response='That is not a valid answer.')
    if custom_names.lower() == 'y':
        tally, pdf_name = multi_convert_check(photo_groups_dict, tally, dummy_list, ready_list,
                                              all_pdfs, do_custom_names=True)
    elif custom_names.lower() == 'n':
        tally, pdf_name = multi_convert_check(photo_groups_dict, tally, dummy_list, ready_list,
                                              all_pdfs)

    # Drive API Credentials: this is where the user is authorized to use the Drive API. If they don't have token.pickle
    # (if they've never used the Snap before), they will be prompted to log into their google account. A new
    # token.pickle file is created, which stores the user's access and refresh tokens. SCOPES determines what the user
    # does and does not have permission to do. Although the scope can be narrowed down, this broad-access one was the
    # only one that worked.
    # From this point forward, Ms. Ifft helped me a lot with the code and figuring out the API.
    service, page_token, folder_id = authenticate_scopes()
    already_file, file_metadata, media = redundancy_check_upload(service, page_token, folder_id, pdf_name)
    if already_file:
        print("Aforementioned error")
    else:
        try:
            file = service.files().create(body=file_metadata,
                                          media_body=media,
                                          fields='id, size').execute()
            if not file.get("id") or file.get("size") == 0:
                print("Incomplete Upload")
        except:
            print("An error occurred")

        if groups_num > 1:
            print("Multiple pdfs confirmed")
            print("pdf list: ", all_pdfs)
            print()
            for pdf in all_pdfs:
                already_file, file_metadata, media = redundancy_check_upload(service, page_token, folder_id, pdf)

                if already_file:
                    print("Aforementioned error")
                else:
                    try:
                        # Upload: this is where the program uses the "create" method from the Drive API. If the file is
                        # missing it's ID, or has no size, (which might indicate an upload issue in which content was
                        # damaged), the program states that a general error has occurred.
                        # Communicating with the Drive API to figure out just what error happened, or whether there was
                        # an upload issue, was challenging, so we decided to use this general try/except, so that any
                        # issue will result in the error going off.
                        file = service.files().create(body=file_metadata, media_body=media, fields='id, size').execute()
                        if not file.get("id") or file.get("size") == 0:
                            print("Incomplete Upload")
                    except:
                        print("An error occurred")

        # Here is where the tally of PDFs made is rewritten, so that the program can start from the same place the next
        # time it's run.
        tally_rewrite = open(pdf_tally_path, 'w')
        print(tally)
        tally_rewrite.write(str(tally))
        tally_rewrite.close()
        pygame.quit()
        print("\nProcess Complete\n")


if __name__ == '__main__':
    main()
