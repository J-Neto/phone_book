class PhoneBook:
  def __init__(self):
    self.contacts = []

  def add_contact(self, contact):
    self.contacts.append(contact)
  
  def list_contacts(self):
    if self.is_phone_book_empty():
      print("Agenda telefônica vazia!")
    else:
      print("--Contatos--")
      for index, contact in enumerate(self.contacts, start=1):
        favorite_icon = "☆" if contact.is_favorite else ""
        print(f"{index} - {contact} {favorite_icon}")

  def toggle_favorite_contact(self, index):
    index = index - 1
    if self.is_out_of_bounds(index):
      print("Contato inexistente")
    else:
      if self.contacts[index].is_favorite:
        self.unfavorite_contact(index)
      else:
        self.favorite_contact(index)
      
  def list_favorites(self):
    if self.is_phone_book_empty():
      print("Agenda telefônica vazia!")
    else:
      print("--Favoritos--")
      for index, contact in enumerate([item for item in self.contacts if item.is_favorite]):
        print(f"{index} - {contact}")
      
  def delete_contact(self, index):
    if self.is_phone_book_empty():
      print("Agenda telefônica vazia!")
    else:
      index = index - 1
      if self.is_out_of_bounds(index):
        print("Contato inexistente!")
      else:
        self.contacts.pop(index)
        print("Contato removido com sucesso!")
        
  def favorite_contact(self, index):
    self.contacts[index].is_favorite = True
    print(f"Contato favoritado com sucesso!")
  
  def unfavorite_contact(self, index):
    self.contacts[index].is_favorite = False
    print(f"Contato desfavoritado com sucesso!")      
  
  def is_out_of_bounds(self, index):
    if index < 0 or index >= len(self.contacts):
      return True
    else:
      return False  
  
  def is_phone_book_empty(self):
    return not len(self.contacts)