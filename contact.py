class Contact:
  def __init__(self, name, phone_number, email, is_favorite = False):
    self.name = name
    self.phone_number = phone_number
    self.email = email
    self.is_favorite = is_favorite
    
  def __str__(self):
    return (f"Nome: {self.name}, Telefone: {self.phone_number}, Email: {self.email}")