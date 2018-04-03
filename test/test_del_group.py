__author__ = 'viktor'
from model.group import Group
import random
import time
import pytest


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        with pytest.allure.step("When I add a group to the list"):
            app.group.create(Group(name="test_group"))
    with pytest.allure.step("Given a group list from db"):
        old_groups = db.get_group_list()
    with pytest.allure.step("Given a group list from db"):
        group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)