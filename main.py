from Person import Person
from Manager import Manager

john = Person(first_name="John", last_name="Clark", phone="89348239429", birth="1979", email="john@clark.com")
marissa = Person(first_name="Marissa", last_name="Mayer", phone="83483204032", birth="1978", email="marissa@yahoo.com")
bruce = Person(first_name="Bruce", last_name="Wayne", phone="902432309443", birth="1939", email="bruce@batman.com")
contact_book = [john, marissa, bruce]
manager = Manager(contact_book)

while True:
    print "Choose (1-5)"
    print "1. Add new contact"
    print "2. Output all contacts"
    print "3. Edit contact information"
    print "4. Delete contact from contact book"
    print "5. Close"

    choice = raw_input("")

    if choice == "1":
        manager.add_new()
    elif choice == "2":
        manager.output_contact()
    elif choice == "3":
        manager.edit_contact()
    elif choice == "4":
        manager.delete_contact()
    elif choice == "5":
        break
    else:
        print "Please enter value between 1-5"
