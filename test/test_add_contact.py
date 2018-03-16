# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", home_number="", mobile_number="", work_number="",
                    address="", email="", email2="", email3="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            home_number=random_string("home_number", 10), mobile_number=random_string("mobile_number", 10),
            work_number=random_string("work_number", 10), address=random_string("address", 20),
            email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20))
    for i in range(5)
]


@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="Test1", lastname="Test2", home_number="1111111", mobile_number="2222222",
#                      address="Moskow", email="test@mail.ru", email2="test@gmail.com", email3="test@yandex.ru")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
