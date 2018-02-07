# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Test1", lastname="Test2", home_number="1111111", mobile_number="2222222"))
    app.session.logout()
