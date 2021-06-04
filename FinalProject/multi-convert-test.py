from PIL import Image
import pygame

photo_list = []
name_list = []
dummy_list = []
ready_list = []
image_list = []
pdf_tally_path = '/Users/tkmuro/PycharmProjects/tkProgramming/FinalProject/testtest.txt'

current_photos_list = []


def read_data(path):
    file_for_read = open(path)
    content = file_for_read.read()
    file_for_read.close()
    return content


def convert_pdfs(names, storing_list, ready, tally, custom_name=False):
    pdf_name = str(tally)
    # print()
    # print("--Starting PDF Conversion--")
    print('\nStart of function:')
    print('Names: ', names)
    print('Storing list: ', storing_list)
    print('Ready list:', ready)
    for q in names:
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
        pdf_name = str(tally)

    storing_list[0].save(r'/Users/tkmuro/PycharmProjects/tkProgramming/FinalProject/pdfs/' + pdf_name + '.pdf', save_all=True, append_images=ready)
    tally += 1
    print('\nEnd of function:')
    print('Names: ', names)
    print('Storing list: ', storing_list)
    print('Ready list:', ready)

    names.clear()
    storing_list.clear()
    ready.clear()

    return tally, pdf_name


def main():
    pdf_name = 'default_name'
    photo_groups = {}
    groups_num = 0

    size = [200, 200]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Window")

    run = True
    i = 0
    tally = int(read_data(pdf_tally_path))
    print(tally)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    photo_id = '/Users/tkmuro/PycharmProjects/tkProgramming/FinalProject/Samples/hw%s.jpeg' % (str(i))
                    name_list.append(photo_id)
                    current_photos_list.append(photo_id)
                    print(current_photos_list)
                    i += 1

                elif event.key == pygame.K_z:
                    transition_list = current_photos_list.copy()
                    photo_groups[groups_num] = transition_list
                    current_photos_list.clear()
                    groups_num += 1
                    print(photo_groups)
                    print()

                elif event.key == pygame.K_q:
                    if current_photos_list:  # Auto-save, if you forgot to make a final new group.
                        transition_list = current_photos_list.copy()
                        photo_groups[groups_num] = transition_list
                    run = False
                    print(photo_groups)
                    pygame.quit()
                    break

    if groups_num > 0:
        print('\nConversion')
        for g in photo_groups:
            print()
            print(g, photo_groups[g])
            tally, pdf_name = convert_pdfs(photo_groups[g], dummy_list, ready_list, tally)
            photo_groups[g] = []
        # tally, pdf_name = convert_pdfs(photo_groups[1], dummy_list, ready_list, tally)
        # When isolated, converting the second group works. Consecutive conversions are the issue.
    elif groups_num == 0:
        tally, pdf_name = convert_pdfs(name_list, dummy_list, ready_list, tally)

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
