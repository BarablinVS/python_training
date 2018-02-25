# -*- coding: utf-8 -*-
from model.group import Group
__author__ = 'viktor'


def test_mod_group_name(app):
    app.group.modify_first_group(Group(name="New group"))


def test_mod_group_header(app):
    app.group.modify_first_group(Group(header="New header"))

