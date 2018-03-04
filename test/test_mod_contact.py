from model.contact import Contact


def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact2"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test123", lastname="Test234", home_number="11111119", mobile_number="22222229")
    contact.id = old_contacts[0].id
    app.contact.modify(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)