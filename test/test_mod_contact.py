from model.contact import Contact


def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_contact2"))
    app.contact.modify(Contact(firstname="Test123", lastname="Test234", home_number="11111119", mobile_number="22222229"))
