# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random
import pytest


def test_del_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        with pytest.allure.step("When I add a contact to the list"):
            app.contact.create(Contact(firstname="test_contact"))
    with pytest.allure.step("Given a random group"):
        group = random.choice(orm.get_group_list())
    with pytest.allure.step("Given a random contact"):
        contact = random.choice(orm.get_contact_list())
    if contact not in orm.get_contacts_in_group(Group(id="%s" % group.id)):
        with pytest.allure.step("When I add the contact %s to the group %" % contact.id % group.id):
            app.contact.add_contact_in_group(contact.id, group.id)
    with pytest.allure.step("When I delete the contact %s from the group %s" % contact.id % group.id):
        app.contact.delete_contact_from_group(contact.id, group.id)
    with pytest.allure.step("Then the contact is not in group list"):
        assert contact in orm.get_contacts_not_in_group(Group(id="%s" % group.id))