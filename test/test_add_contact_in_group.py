# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, orm):
    if len(orm.get_contact_list()) == 0 :
        app.contact.create(Contact(firstname="test_contact"))
    contact = random.choice(orm.get_contact_list())
    group = random.choice(orm.get_group_list())
    if contact in orm.get_contacts_not_in_group(Group(id="%s" % group.id)):
        app.contact.add_contact_in_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(Group(id="%s" % group.id))