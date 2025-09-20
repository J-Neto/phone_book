from contact import Contact
from phone_book import PhoneBook
import os

def wait_and_clear_screen():
  input("")
  os.system('cls' if os.name == "nt" else "clear")

def delete_contact(phone_book, contact_index):
  contact_index = contact_index - 1
  if contact_index >= 0 and contact_index < len(phone_book):
    phone_book.pop(contact_index)
    print(f"Contato removido com sucesso!")
  else:
    print("Contato inexistente!")
  return
  
# -------------------
phone_book = PhoneBook()

while True:
  print("Agenda Telefônica 🕮")
  option = int(input("1- Adicionar contato\n2- Ver contatos\n3- Favoritar/desfavoritar contato\n4- Ver favoritos\n5- Apagar contato\n6- Sair do programa\nOpção: "))
  os.system('cls' if os.name == "nt" else "clear")
  
  match option:
    case 1:
      print("--Adicionar contato--")
      name = input("Insira o nome: ")
      phone_number = input("Insira o telefone: ")
      email = input("Insira o email: ")

      contact = Contact(name, phone_number, email)
      phone_book.add_contact(contact)
      
      print("Contato adicionado com sucesso!")
      wait_and_clear_screen()
      
    case 2:
      phone_book.list_contacts()
      wait_and_clear_screen()
    
    case 3:
      phone_book.list_contacts()
      contact_index = int(input("Insira o índice do contato: "))
      phone_book.check_favorite_contact(contact_index)
      wait_and_clear_screen()
    
    case 4:
      phone_book.list_favorites()
      wait_and_clear_screen()

    case 5:
      if (len(phone_book.contacts) > 0):
        phone_book.list_contacts()
        contact_index = int(input("Insira o índice do contato: "))
        phone_book.delete_contact(contact_index)
      else:
        print("Lista vazia!")
      wait_and_clear_screen()
    case 6:
      break
    case _:
      print("Opção inválida!")