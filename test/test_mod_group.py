# -*- coding: utf-8 -*-
from model.group import Group
__author__ = 'viktor'


def test_mod_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test_group2"))
    app.group.modify_first_group(Group(name="New group"))


def test_mod_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test_group3"))
    app.group.modify_first_group(Group(header="New header"))

