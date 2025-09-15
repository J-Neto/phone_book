from contact import Contact
import os

def wait_and_clear_screen():
  input("")
  os.system('cls' if os.name == "nt" else "clear")

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
      print("--Contatos--")
      print(*phone_book, sep="\n")
      wait_and_clear_screen()
    case 6:
      break
    case _:
      print("Opção inválida!")