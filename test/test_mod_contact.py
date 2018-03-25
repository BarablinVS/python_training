from model.contact import Contact
import random


def test_mod_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test_contact2"))
    old_contacts = db.get_contact_list()
    print(old_contacts)
    random_contact = random.choice(old_contacts)
    print("id = " + str(random_contact.id))
    print(len(old_contacts))
    new_contact = Contact(firstname="Test123", lastname="Test234", home_number="11111119", mobile_number="22222229")
    app.contact.modify_contact_by_id(random_contact.id, new_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())

        db_list = map(clean, db.get_contact_list())
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
