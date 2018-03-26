__author__ = 'viktor'

from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_link_text("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.firstname)
        self.change_field("lastname", contact.lastname)
        self.change_field("home", contact.home_number)
        self.change_field("mobile", contact.mobile_number)
        self.change_field("work", contact.work_number)
        self.change_field("address", contact.address)
        self.change_field("email", contact.email)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)



    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(2+index) + "]/td[8]/a/img").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[" + str(2+index) + "]/td[7]/a/img").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None


    def add_contact_in_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value=" + group_id + "]").click()
        wd.find_element_by_name("add").click()

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("//select[@name='group']/option[@value=" + group_id + "]").click()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()

    def delete_first_contact(self):
        self.delete_group_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # select first group
        self.select_contact_by_index(index)
        # click Delete button
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.edit_contact_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        for element in wd.find_elements_by_name("entry"):
                columns = element.find_elements_by_tag_name("td")
                idx = element.find_element_by_name("selected[]").get_attribute("value")
                print(idx)
                if idx == id:
                    break
        columns[7].click()

        print("Test")

        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_cache = None

    contact_cache = None


    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                columns = element.find_elements_by_tag_name("td")
                lastname = columns[1].text
                firstname = columns[2].text
                address = columns[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_emails = columns[4].text
                all_phones = columns[5].text
                if len(all_phones.splitlines()) == 3:
                    home_number = all_phones.splitlines()[0]
                    mobile_number = all_phones.splitlines()[1]
                    work_number = all_phones.splitlines()[2]
                else:
                    home_number=''
                    mobile_number=''
                    work_number=''

                if len(all_emails.splitlines()) == 3:
                    email = all_emails.splitlines()[0]
                    email2 = all_emails.splitlines()[1]
                    email3 = all_emails.splitlines()[2]
                else:
                    email = ''
                    email2 = ''
                    email3 = ''

                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                                  address=address, all_phones_from_home_page=all_phones, home_number=home_number,
                                                  mobile_number=mobile_number, work_number=work_number,
                                                  all_emails_from_home_page=all_emails,
                                                  email=email,
                                                  email2=email2, email3=email3))

        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, home_number=home_number, work_number=work_number,
                       address=address, email=email, email2=email2, email3=email3,
                       mobile_number=mobile_number, id=id)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H: (.*)", text).group(1)
        mobile_number = re.search("M: (.*)", text).group(1)
        return Contact(home_number=home_number, mobile_number=mobile_number)









