from model.contact import Contact


def test_properties_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()

    print("\n")
    print(contact_from_home_page)
    print(contact_from_db)
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
    db_list = map(clean, contact_from_db)
    assert sorted(db_list, key=Contact.id_or_max) == sorted(contact_from_home_page, key=Contact.id_or_max)



