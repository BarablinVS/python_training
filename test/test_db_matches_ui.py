__author__ = "viktor"
from model.group import Group
from model.contact import Contact
import pytest


def test_group_list(app, db):
    with pytest.allure.step("Given a group list from group page"):
        ui_list = app.group.get_group_list()
    with pytest.allure.step("Given a group list from db"):
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        db_list = map(clean, db.get_group_list())
    with pytest.allure.step("Then the group list from group page is equal to the group list from db"):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    with pytest.allure.step("Given a contact list from contact page"):
        ui_list = app.contact.get_contact_list()
    with pytest.allure.step("Given a group list from db"):
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address.strip(), home_number=contact.home_number.strip())
        db_list = map(clean, db.get_contact_list())
    with pytest.allure.step("Then the contact list from contact page is equal to the contact list from db"):
        assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)




