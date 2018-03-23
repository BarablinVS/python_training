# -*- coding: utf-8 -*-
from model.group import Group
import random

__author__ = 'viktor'


def test_mod_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group2"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="New group")
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_mod_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test_group3"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

