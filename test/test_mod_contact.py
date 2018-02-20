from model.contact import Contact


def test_mod_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(firstname="Test123", lastname="Test234", home_number="11111119", mobile_number="22222229"))
    app.session.logout()
