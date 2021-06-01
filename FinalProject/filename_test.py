pdf_tally_path = '/Users/tkmuro/PycharmProjects/tkProgramming/FinalProject/testtest.txt'
pdf_name = 'default_name'


def read_data(path):
    file_for_read = open(path)
    content = file_for_read.read()
    file_for_read.close()
    return content


def convert_pdfs(tally):
    pdf_name = input("Enter PDF name: ")
    # storing_list[0].save(r'/home/pi/Desktop/TransferFiles/' + pdf_name + '.pdf', save_all=True, append_images=ready)
    print(tally)
    tally += 1  # ^^^ PDF NAMES
    print(tally)
    print()
    return tally


i = 0
tally = int(read_data(pdf_tally_path))
print('Tally:', tally)

print(pdf_name)
tally = convert_pdfs(tally)
print(pdf_name)

tally_rewrite = open(pdf_tally_path, 'w')
print('Tally:', tally)
tally_rewrite.write(str(tally))
print('Tally:', tally)
tally_rewrite.close()
