import re
from random import randrange


def test_properties_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_properties_like_on_home_page\
        ([contact_from_edit_page.home_number, contact_from_edit_page.mobile_number])
    assert contact_from_home_page.all_emails_from_home_page == merge_properties_like_on_home_page\
        ([contact_from_edit_page.email, contact_from_edit_page.email2, contact_from_edit_page.email3])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_properties_like_on_home_page(params):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, params))))
