class Person(object):
    first_name = ""
    last_name = ""
    email = ""
    phone = ""
    birth = ""

    def __init__(self, first_name, last_name, email, phone, birth):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.birth = birth

    def get_full_name(self):
        return self.first_name + " " + self.last_name


