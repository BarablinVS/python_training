# -*- coding: utf-8 -*-
from model.group import Group


def test_mod_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="dfgdfg1", header="dfgdfg2", footer="dfgdfgdfg3"))
    app.session.logout()
