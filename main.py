from contact import Contact
from phone_book import PhoneBook
import os

def clear_screen():
  os.system('cls' if os.name == "nt" else "clear")

def wait_and_clear_screen():
  input("Pressione Enter para continuar...")
  clear_screen()
  
# -------------------
phone_book = PhoneBook()

while True:
  print("Agenda Telefônica 🕮")
  option = int(input("1- Adicionar contato\n2- Ver contatos\n3- Favoritar/desfavoritar contato\n4- Ver favoritos\n5- Apagar contato\n6- Sair do programa\nOpção: "))
  clear_screen()
  
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
      if (phone_book.is_phone_book_empty()):
        print("Agenda telefônica vazia!")
      else:
        phone_book.list_contacts()
        contact_index = int(input("Insira o índice do contato: "))
        phone_book.toggle_favorite_contact(contact_index)
      wait_and_clear_screen()
    
    case 4:
      phone_book.list_favorites()
      wait_and_clear_screen()

    case 5:
      if (phone_book.is_phone_book_empty()):
        print("Agenda telefônica vazia!")
      else:
        phone_book.list_contacts()
        contact_index = int(input("Insira o índice do contato: "))
        phone_book.delete_contact(contact_index)
      wait_and_clear_screen()
    case 6:
      break
    case _:
      print("Opção inválida!")