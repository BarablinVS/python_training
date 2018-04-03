# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    with pytest.allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
    with pytest.allure.step("When I add a contact %s to the list" % contact):
        app.contact.create(contact)
    with pytest.allure.step("Then the new contact list is equal to the old list with the added contact"):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        with pytest.allure.step("Then the old contact list is equal to the contact list from contact page"):
            def clean(contact):
                return Contact(id=contact.id, firstname=contact.firstname.strip(),lastname=contact.lastname.strip())

            db_list = map(clean, db.get_contact_list())
            assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)