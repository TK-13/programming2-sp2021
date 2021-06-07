from PIL import Image
import pygame

pdf_tally_path = '/Users/tkmuro/PycharmProjects/tkProgramming/FinalProject/tally.txt'

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (93, 202, 143)
RED = (201, 93, 98)
BLUE = (93, 131, 201)
ORANGE = (201, 147, 93)
GRAY = (52, 52, 52)
YELLOW = (255, 204, 0)
PURPLE = (102, 0, 204)

mx = 0
my = 0

button1x = 32
button1y = 338


class Ntrct(pygame.sprite.Sprite):
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


def buttonadd(x, y, mouse_x, mouse_y, buttons, color, surface, button_key, w=80, h=40):
    if x <= mouse_x <= (x + w) and y <= mouse_y <= (y + h) or button_key:
        button = Ntrct(x, y, color, surface, w, h)
    else:
        button = Ntrct(x, y, BLACK, surface, w, h)
    buttons.add(button)


def read_data(path):
    file_for_read = open(path)
    content = file_for_read.read()
    file_for_read.close()
    return content


def convert_pdf(names, storing_list, ready, tally_placeholder, custom_name=False):
    # pdf_name = str(tally_placeholder)
    print('\nStart of function:')
    # print('Names: ', names)
    # print('Storing list: ', storing_list)
    # print('Ready list:', ready)
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
    # tally += 1
    print('\nEnd of function:')
    # print('Names: ', names)
    # print('Storing list: ', storing_list)
    # print('Ready list:', ready)

    names.clear()
    storing_list.clear()
    ready.clear()

    return pdf_name


def multi_convert_check(groups_num_place, photo_groups_place, tally_place,
                        name_list_place, dummy_list_place, ready_list_place,
                        do_custom_names=False):
    if groups_num_place > 0:
        print("\nConfirmed: multiple groups")
        for g in photo_groups_place:
            print(g, photo_groups_place[g])
            print()
            print("pre-run tally within convert: ", tally_place)
            if do_custom_names:
                pdf_name = convert_pdf(photo_groups_place[g], dummy_list_place, ready_list_place, tally_place,
                                       custom_name=True)
            elif not do_custom_names:
                pdf_name = convert_pdf(photo_groups_place[g], dummy_list_place, ready_list_place, tally_place)
            print("post-run tally within convert: ", tally_place)
            photo_groups_place[g] = []
            tally_place += 1
    elif groups_num_place == 0:
        print("\nConfirmed: single group")
        if do_custom_names:
            pdf_name = convert_pdf(name_list_place, dummy_list_place, ready_list_place, tally_place, custom_name=True)
        elif not do_custom_names:
            pdf_name = convert_pdf(name_list_place, dummy_list_place, ready_list_place, tally_place)
        tally_place += 1

    print("Final tally within multi: ", tally_place, '\n')
    return tally_place, pdf_name


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


def key_a(names, current, place):
    photo_id = '/Users/tkmuro/PycharmProjects/tkProgramming/FinalProject/Samples/hw%s.jpeg' % (str(place))
    names.append(photo_id)
    current.append(photo_id)
    print(current)
    place += 1
    return photo_id, names, current, place


def main():
    # Changed
    pygame.init()

    current_photos_list = []
    photo_list = []
    name_list = []
    dummy_list = []
    ready_list = []
    image_list = []

    a_triggered = False

    # Changed
    button_list = pygame.sprite.Group()

    photo_groups = {}
    groups_num = 0

    size = [400, 400]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Window")

    run = True
    clock = pygame.time.Clock()

    i = 0
    tally = int(read_data(pdf_tally_path))
    print(tally)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    photo_id, name_list, current_photos_list, i = key_a(name_list, current_photos_list, i)
                    a_triggered = True

                elif event.key == pygame.K_z:
                    transition_list = current_photos_list.copy()
                    photo_groups[groups_num] = transition_list
                    current_photos_list.clear()
                    groups_num += 1
                    print(photo_groups)
                    print()

                # Changed
                elif event.key == pygame.K_q:
                    if current_photos_list:  # Auto-save, if you forgot to make a final new group.
                        do_auto_save = user_input(
                            'You have ungrouped photos remaining. Would you like for them to be converted? ',
                            ['y', 'n'])
                        if do_auto_save == 'y':
                            transition_list = current_photos_list.copy()
                            photo_groups[groups_num] = transition_list
                            current_photos_list.clear()
                            groups_num += 1
                    run = False
                    print('Groups: ', photo_groups)
                    print("num of groups: ", groups_num)
                    pygame.quit()
                    break

            # Work in Progress
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    a_triggered = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1x <= mouse[0] <= (button1x + 80) and button1y <= mouse[1] <= (button1y + 40):
                    photo_id, name_list, current_photos_list, i = key_a(name_list, current_photos_list, i)

        if run:
            mouse = pygame.mouse.get_pos()
            mx = mouse[0]
            my = mouse[1]

            screen.fill(GRAY)
            buttonadd(button1x, button1y, mx, my, button_list, GREEN, screen, a_triggered)

            button_list.update()
            button_list.draw(screen)

            pygame.display.flip()
            clock.tick(60)

    custom_names = user_input('Would you like to enter a custom name? (y/n) ', ['y', 'n'],
                              response='That is not a valid answer.')

    print()
    print("pre-multi function tally: ", tally)
    if custom_names.lower() == 'y':
        tally, pdf_name = multi_convert_check(groups_num, photo_groups, tally,
                                              name_list, dummy_list, ready_list,
                                              do_custom_names=True)
    elif custom_names.lower() == 'n':
        tally, pdf_name = multi_convert_check(groups_num, photo_groups, tally,
                                              name_list, dummy_list, ready_list)
    print("post-multi function tally: ", tally)
    print()

    # if groups_num > 0:
    #     for g in photo_groups:
    #         print(g, photo_groups[g])
    #         tally, pdf_name = convert_pdf(photo_groups[g], dummy_list, ready_list, tally)
    #         photo_groups[g] = []
    # elif groups_num == 0:
    #     tally, pdf_name = convert_pdf(name_list, dummy_list, ready_list, tally)

    # if groups_num > 0:
    #     print('\nConversion')
    #     for g in photo_groups:
    #         print()
    #         print(g, photo_groups[g])
    #         tally, pdf_name = convert_pdfs(photo_groups[g], dummy_list, ready_list, tally)
    #         photo_groups[g] = []
    #     # tally, pdf_name = convert_pdfs(photo_groups[1], dummy_list, ready_list, tally)
    #     # When isolated, converting the second group works. Consecutive conversions are the issue.
    # elif groups_num == 0:
    #     tally, pdf_name = convert_pdfs(name_list, dummy_list, ready_list, tally)

    '''
    custom_names = user_input('Would you like to enter a custom name? (y/n) ', ['y', 'n'],
                              response='That is not a valid answer.')
    if custom_names == 'y':
        print(pdf_name)
        tally, pdf_name = convert_pdfs(name_list, dummy_list, ready_list, tally, photo_groups, custom_name=True)
        print(pdf_name)
    elif custom_names == 'n':
        # pdf_name = str(tally)
        print(pdf_name)
        tally, pdf_name = convert_pdfs(name_list, dummy_list, ready_list, tally, photo_groups)
        print(pdf_name)
    '''

    '''
    service, page_token, folder_id = authenticate_scopes()
    already_file, file_metadata, media = redundancy_check(tally, service, page_token, folder_id, pdf_name)
    if already_file:
        print("Aforementioned error")
    else:
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
    '''


if __name__ == '__main__':
    main()
