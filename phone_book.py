class PhoneBook:
  def __init__(self):
    self.contacts = []
    
  def add_contact(self, contact):
    self.contacts.append(contact)
  
  def list_contacts(self):
    for index, contact in enumerate(self.contacts, start=1):
      favorite_icon = "☆" if contact.is_favorite else ""
      print(f"{index} - {contact} {favorite_icon}")