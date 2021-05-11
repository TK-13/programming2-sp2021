class Person:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.address = None
        self.phone_number = None

    # KEEP THIS IN MERGE: Setter function. If an attribute is not defined in init,
    # you can do that here.
    def add_address(self, address):
        self.address = address

    def add_phone_number(self, phone_number):
        self.phone_number = phone_number

    def print_contact_info(self):
        print(self.name)
        print(self.email_address)
        if self.address:
            print(self.address)
        if self.phone_number:
            print("H: {0}".format(self.phone_number))


def main():
    ms_ifft = Person("Ms. Ifft", "bifft@fwparker.org")
    ms_ifft.add_phone_number('333-333-3333')
    ms_ifft.add_address('Chicago, IL 60647')

    ryan = Person("Ryan Kershner", "rkershner@fwparker.org")
    ryan.add_phone_number('444-444-4444')
    ryan.add_address('Chicago, IL 60611')

    tk = Person("TK Muro", "tmuro@fwparker.org")
    tk.add_phone_number('555-555-5555')
    tk.add_address('Chicago, IL 60657')

    aaron = Person("Aaron Rothman", "arothman@fwparker.org")
    aaron.add_phone_number('666-666-6666')
    aaron.add_address('Chicago, IL 60614')

    alex = Person("Alex Shapiro", "aschapiro@fwparker.org")
    alex.add_phone_number('777-777-7777')
    alex.add_address('Chicago, IL 60614')

    our_class = [ms_ifft, ryan, tk, aaron, alex]

    print()
    for person in our_class:
        person.print_contact_info()
        print()


if __name__ == '__main__':
    main()

