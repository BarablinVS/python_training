# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Test1", lastname="Test2", home_number="1111111", mobile_number="2222222"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", home_number="", mobile_number=""))
