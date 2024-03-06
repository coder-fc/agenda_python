def adiconar_contato(contatos, nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone,
               "email": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome} foi adicionado com sucesso!")
    return


def ver_contatos(contatos):
    print("\nLista de contatos: ")
    for indice, contato in enumerate(contatos, start=1):
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        favorito = "☆" if contato["favorito"] else " "
        print(f"{indice}. Nome do contato: {nome} - Telefone: {
              telefone} - E-mail: {email} {favorito}")
    return


contatos = []

while True:
    print("\nMenu da agenda: ")
    print("1. Adicionar contato")
    print("2. Visualizar contatos cadastrados")
    print("3. Editar contato")
    print("4. Marcar / Desmarcar contato como favorito")
    print("5. Visualizar contatos favoritos")
    print("6. Apagar contato")
    print("7. Exit")

    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        adiconar_contato(contatos, nome, telefone, email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "7":
        break


print("Programa finalizado!")
