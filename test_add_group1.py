# -*- coding: utf-8 -*-
import pytest


from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_group1(app):
        app.open_home_page()
        app.login( username="admin", password="secret")
        app.init_group_creation()
        app.fill_the_form(Group(firstname="new group", middlename="1", lastname="1", nickname="1", title="1", company="1"))
        app.submit_group_creation()
        app.logout()

def test_add_empty_group1(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.init_group_creation()
        app.fill_the_form(Group(firstname="", middlename="", lastname="", nickname="", title="",
                           company=""))
        app.submit_group_creation()
        app.logout()

