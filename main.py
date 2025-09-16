from contact import Contact
import os

def wait_and_clear_screen():
  input("")
  os.system('cls' if os.name == "nt" else "clear")

def list_phone_book(phone_book):
  print("--Contatos--")
  for index, contact in enumerate(phone_book, start=1):
    favorite_icon = "☆" if contact.is_favorite else ""
    print(f"{index} - {contact} {favorite_icon}")
  return

def check_favorite_contact(phone_book, contact_index):
  contact_index = contact_index - 1
  if contact_index >= 0 and contact_index < len(phone_book):
    if phone_book[contact_index].is_favorite:
      unfavorite_contact(phone_book, contact_index)
    else:
      favorite_contact(phone_book, contact_index)
  else:
    print("Contato inexistente!")
  return

def favorite_contact(phone_book, contact_index):
  phone_book[contact_index].is_favorite = True
  print(f"Contato {phone_book[contact_index]} favoritado com sucesso!")
  return

def unfavorite_contact(phone_book, contact_index):
  phone_book[contact_index].is_favorite = False
  print(f"Contato {phone_book[contact_index]} desfavoritado com sucesso!")
  return

def list_favorites(phone_book):
  for index, contact in enumerate([item for item in phone_book if item.is_favorite]):
    print(f"{index} - {contact}")

# -------------------
phone_book = []

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
      phone_book.append(contact)
      
      print("Contato adicionado com sucesso!")
      wait_and_clear_screen()
      
    case 2:
      list_phone_book(phone_book) 
      wait_and_clear_screen()
    
    case 3:
      list_phone_book(phone_book) 
      contact_index = int(input("Insira o índice do contato: "))
      check_favorite_contact(phone_book, contact_index)
      wait_and_clear_screen()
    
    case 4:
      list_favorites(phone_book)
      wait_and_clear_screen()

    case 6:
      break
    case _:
      print("Opção inválida!")