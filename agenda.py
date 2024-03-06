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


def editar_contato(contatos, indice_contato, dado_editar, novo_nome=None, novo_telefone=None, novo_email=None):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        if dado_editar == "1":
            if novo_nome is not None:
                contatos[indice_contato_ajustado]["nome"] = novo_nome
                print(f"Nome do contato {
                      indice_contato} atualizado para {novo_nome}")
        elif dado_editar == "2":
            if novo_telefone is not None:
                contatos[indice_contato_ajustado]["telefone"] = novo_telefone
                print(f"Telefone do contato {
                      indice_contato} atualizado para {novo_telefone}.")
        elif dado_editar == "3":
            if novo_email is not None:
                contatos[indice_contato_ajustado]["email"] = novo_email
                print(
                    f"E-mail do contato {indice_contato} atualizado para {novo_email}.")
    else:
        print("Contato não existe")
    return


def editar_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        if contatos[indice_contato_ajustado]["favorito"]:
            contatos[indice_contato_ajustado]["favorito"] = False
            print(f"Contato {indice_contato} removido dos favoritos")
        else:
            contatos[indice_contato_ajustado]["favorito"] = True
            print(f"Contato {indice_contato} adicionados aos favoritos")
    return


def mostra_favoritos(contatos):
    print("\nContatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{indice}. Nome do contato: {nome} - Telefone: {
                telefone} - E-mail: {email} ☆")
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

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o contato a editar: ")
        print("\nDado a editar: ")
        print("1. Nome")
        print("2. Telefone")
        print("3. E-mail")
        dado_editar = input("Digite o dado a editar: ")
        novo_nome = None
        novo_telefone = None
        novo_email = None
        if dado_editar == "1":
            novo_nome = input("Digite o novo nome: ")
        elif dado_editar == "2":
            novo_telefone = input("Digite o novo telefone: ")
        elif dado_editar == "3":
            novo_email = input("Digite o novo E-mail: ")
        editar_contato(contatos, indice_contato, dado_editar,
                       novo_nome, novo_telefone, novo_email)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input(
            "Digite o contato a marcar ou desmarcar como favorito: ")
        editar_favorito(contatos, indice_contato)

    elif escolha == "5":
        mostra_favoritos(contatos)

    elif escolha == "7":
        break


print("Programa finalizado!")
