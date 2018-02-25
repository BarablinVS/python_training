__author__ = 'viktor'


def test_delete_contact(app):
    app.contact.delete()