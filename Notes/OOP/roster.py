class Person:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.address = None
        self.phone_number = None

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


# Student inherits from (is a child of) Person
class Student(Person):  # parent or super class is Person
    def __init__(self, name, email_address, year):
        super().__init__(name, email_address)
        self.year = year
        self.group = None

    def add_group(self, group):
        self.group = group

    def print_contact_info(self):
        print("{0} '{1}".format(self.name, self.year))
        print(self.email_address)
        if self.address:
            print(self.address)
        if self.phone_number:
            print("H: {0}".format(self.phone_number))
        if self.group:
            print("C: ({0})".format(self.group))




def main():
    ms_ifft = Person("Ms. Ifft", "bifft@fwparker.org")
    ms_ifft.add_phone_number('333-333-3333')
    ms_ifft.add_address('Chicago, IL 60647')

    ryan = Student("Ryan Kershner", "rkershner@fwparker.org", 23)
    ryan.add_phone_number('444-444-4444')
    ryan.add_address('Chicago, IL 60611')
    ryan.add_group('RB')

    tk = Student("TK Muro", "tmuro@fwparker.org", 21)
    tk.add_phone_number('555-555-5555')
    tk.add_address('Chicago, IL 60657')

    aaron = Student("Aaron Rothman", "arothman@fwparker.org", 21)
    aaron.add_phone_number('666-666-6666')
    aaron.add_address('Chicago, IL 60614')
    aaron.add_group('B')

    alex = Student("Alex Schapiro", "aschapiro@fwparker.org", 21)
    alex.add_phone_number('777-777-7777')
    alex.add_address('Chicago, IL 60614')
    alex.add_group('B')

    our_class = [ms_ifft, ryan, tk, aaron, alex]

    print()
    for person in our_class:
        person.print_contact_info()
        print()


if __name__ == '__main__':
    main()

