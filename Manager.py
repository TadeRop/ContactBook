from Person import Person

class Manager(object):
    contact_book = []

    def __init__(self, contact_book):
        self.contact_book = contact_book

    def output_contact(self):
        i = 1
        for person in self.contact_book:
            print str(i) + ". "
            i += 1
            print "First Name: " + person.first_name
            print "Last Name: " + person.last_name
            print "Email: " + person.email
            print "Phone: " + person.phone
            print "Birth year: " + person.birth

    def add_new(self):
        first_name = raw_input("Enter first name: ")
        last_name = raw_input("Enter last name: ")
        email = raw_input("Enter email: ")
        phone = raw_input("Enter phone number: ")
        birth = raw_input("Enter year of birth: ")

        person = Person(first_name, last_name, email, phone, birth)
        self.contact_book.append(person)

    def edit_contact(self):
        i = int(raw_input("Select the number of the contact: "))
        first_name = raw_input("Enter first name: ")
        if i <= len(self.contact_book) and i > 0:
            self.contact_book[i - 1].first_name = first_name
        last_name = raw_input("Enter last name: ")
        if i <= len(self.contact_book) and i > 0:
            self.contact_book[i - 1].last_name = last_name
        email = raw_input("Enter email: ")
        if i <= len(self.contact_book) and i > 0:
            self.contact_book[i - 1].email = email
        phone = raw_input("Enter phone number: ")
        if i <= len(self.contact_book) and i > 0:
            self.contact_book[i - 1].phone = phone
        birth = raw_input("Enter year of birth: ")
        if i <= len(self.contact_book) and i > 0:
            self.contact_book[i - 1].birth = birth

    def delete_contact(self):
        i = int(raw_input("Select the number of the contact: "))

        if i <= len(self.contact_book) and i > 0:
            self.contact_book.pop(i - 1)



