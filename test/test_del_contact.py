from model.contact import Contact
import random
import time
import pytest
__author__ = 'viktor'


def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        with pytest.allure.step("When I add a contact to the list"):
            app.contact.create(Contact(firstname="test_contact"))
    with pytest.allure.step("Given a contact list from db"):
        old_contacts = db.get_contact_list()
    with pytest.allure.step("Given a random contact"):
        contact = random.choice(old_contacts)
    with pytest.allure.step("When I delete the contact %s to the list" % contact):
        app.contact.delete_contact_by_id(contact.id)
    time.sleep(1)
    with pytest.allure.step("Given a new contact list from db"):
        new_contacts = db.get_contact_list()
    with pytest.allure.step("Then length of old contact list minus 1 is equal to length of new contact list "):
        assert len(old_contacts) - 1 == len(new_contacts)
    with pytest.allure.step("When I remove the contact from old contacts list"):
        old_contacts.remove(contact)
    with pytest.allure.step("Then the old contact list is equal to the new contact list"):
        assert old_contacts == new_contacts
    if check_ui:
        with pytest.allure.step("Given a contact list from db"):
            def clean(contact):
                return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
            db_list = map(clean, db.get_contact_list())
        with pytest.allure.step("Then the contact list from contact page is equal to the contact list from db"):
            assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
