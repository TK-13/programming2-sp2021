from PIL import Image
import pygame

pdf_tally_path = '/Users/tkmuro/PycharmProjects/tkProgramming/FinalProject/tally.txt'

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
        # self.world_shift = 0
        # self.world_raise = 0


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

    storing_list[0].save(r'/Users/tkmuro/PycharmProjects/tkProgramming/FinalProject/pdfs/' + pdf_name + '.pdf',
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
    # if groups_num_place > 0:
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
    # elif groups_num_place == 0:
    #     print("\nConfirmed: single group")
    #     if do_custom_names:
    #         pdf_name = convert_pdf(name_list_place, dummy_list_place, ready_list_place, tally_place, custom_name=True)
    #         final_pdf_list.append(pdf_name)
    #     elif not do_custom_names:
    #         pdf_name = convert_pdf(name_list_place, dummy_list_place, ready_list_place, tally_place)
    #         final_pdf_list.append(pdf_name)
    #     tally_place += 1

    print("Final tally within multi: ", tally_place, '\n')
    return tally_place, pdf_name


# Keyboard functions
# These functions consolidate the commands associated with each keyboard key, which also allows for the reuse of some
# actions, as you can see in key_q.
def key_a(names, current, place):
    photo_id = '/Users/tkmuro/PycharmProjects/tkProgramming/FinalProject/Samples/hw%s.jpeg' % (str(place))
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
            print("\nIn key z")
            print(transition_list)
            print(current)
            print(photo_dict_place)
            print(num_place)
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
                    print(current_photos_list)
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


if __name__ == '__main__':
    main()
