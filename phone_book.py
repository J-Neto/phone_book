class PhoneBook:
  def __init__(self):
    self.contacts = []
    
  def add_contact(self, contact):
    self.contacts.append(contact)
  
  def list_contacts(self):
    print("--Contatos--")
    for index, contact in enumerate(self.contacts, start=1):
      favorite_icon = "☆" if contact.is_favorite else ""
      print(f"{index} - {contact} {favorite_icon}")
      
  def favorite_contact(self, index):
    self.contacts[index].is_favorite = True
    print(f"Contato favoritado com sucesso!")
  
  def unfavorite_contact(self, index):
    self.contacts[index].is_favorite = False
    print(f"Contato desfavoritado com sucesso!")
    
  def check_favorite_contact(self, index):
    index = index - 1
    if index >= 0 and index < len(self.contacts):
      if self.contacts[index].is_favorite:
        self.unfavorite_contact(index)
      else:
        self.favorite_contact(index)
    else:
      print("Contato inexistente")
      
  def list_favorites(self):
    print("--Favoritos--")
    for index, contact in enumerate([item for item in self.contacts if item.is_favorite]):
      print(f"{index} - {contact}")
      
  def delete_contact(self, index):
    index = index - 1
    if index >= 0 and index < len(self.contacts):
      self.contacts.pop(index)
      print("Contato removido com sucesso!")
    else:
      print("Contato inexistente")