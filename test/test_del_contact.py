__author__ = 'viktor'


def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete()
    app.session.logout()