from contact import Contact

phone_book = []

while True:
  print("Agenda Telefônica")
  option = int(input("1- Adicionar contato\n2- Ver contatos\n3- Favoritar/desfavoritar contato\n4- Ver favoritos\n5- Apagar contato\n6- Sair do programa\nOpção: "))

  match option:
    case 1:
      print("--Adicionar contato--")
      name = input("Insira o nome: ")
      phone_number = input("Insira o telefone: ")
      email = input("Insira o email: ")

      contact = Contact(name, phone_number, email)
      phone_book.append(contact)
      print("Contato adicionado com sucesso!")
    case 6:
      break
    
    case _:
      print("Opção inválida!")