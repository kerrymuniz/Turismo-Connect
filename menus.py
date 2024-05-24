#importando biblioteca
import os
#importando arquivos .py dos cruds
import crud_pontos_turisticos
import crud_usuarios
import crud_estabelecimentos_comerciais

#Instanciando os CRUDs
crud_pontos_turisticos = crud_pontos_turisticos.PontosTuristicos()
crud_usuarios = crud_usuarios.Usuarios()
crud_estabelecimentos_comerciais = crud_estabelecimentos_comerciais.EstabelicimentoComerciais()

#Menu Principal
def menu_principal():
    print("""
        ----------------------------------
        SEJA BEM VINDO AO NOSSO SITEMA!
        ----------------------------------
        Escolha uma opção para ter acesso
        ao nosso conteúdo. DIVIRTA-SE!
        ----------------------------------
        1 - Acessar Pontos Turísticos
        2 - Acessar Usuários
        3 - Acessar Estabelecimentos
            Comerciais
        4 - Sair 
        ----------------------------------
        """
    )
    
def menu_pontos_turisticos():
    print(
                """
                ------------------------------
                CRUD PONTOS TURÍSTICOS
                ------------------------------
                1 - Cadastrar ponto turístico
                2 - Editar ponto turístico
                3 - Deletar ponto turístico
                4 - Listar ponto(s) turístico(s)
                5 - Sair
                ------------------------------
                """
        )
    
def menu_usuarios():
    print(
                """
                ------------------------------
                CRUD USUÁRIOS
                ------------------------------
                1 - Cadastrar usuário
                2 - Editar usuário
                3 - Deletar usuário
                4 - Listar usuário(s)
                5 - Sair
                ------------------------------
                """
        )
    
def menu_estabelecimentos_comerciais():
    print(
                """
                ------------------------------
                CRUD ESTABELECIMENTOS 
                COMERCIAIS (E.C)
                ------------------------------
                1 - Cadastrar E.C
                2 - Editar E.C
                3 - Deletar E.C
                4 - Listar E.C(s)
                5 - Sair
                ------------------------------
                """
        )

#Menu Principal
while True:
    menu_principal()
    menuPrincipal = input("Conteúdo de número ")

    while menuPrincipal != "4":
        if menuPrincipal == "1":
            os.system("cls")
            menu_pontos_turisticos()
            menuCrud1 = input("Escolha uma opção: ")
            if menuCrud1 == "1":
                #CADASTRAR
                crud_pontos_turisticos.criar_arquivo_csv()
                crud_pontos_turisticos.cadastrar_ponto_turistico(nome="Pedro", endereco="rua do pedro", descricao="Lugar Aberto",horario_de_funcionamento= "Seg - Sex: 6:00 - 22:00", media_de_avaliacoes= "4.9" )
                continuar = input("Deseja continuar manipulando ( (S)im / (N)ão )? ")
                if continuar == "N":
                    ...

            if menuCrud1 == "2":
                #EDITAR
                crud_pontos_turisticos.criar_arquivo_csv()
                crud_pontos_turisticos.editar_informacao_ponto_turistico(id_ponto_turistico= 1, campo_de_alteracao=["Nome", "Endereço"], nova_informacao=["Católica", "Rua do Prícipe"])
                continuar = input("Deseja continuar manipulando ( (S)im / (N)ão )? ")
                if continuar == "N":
                    ...

            if menuCrud1 == "3":
                #DELETAR
                crud_pontos_turisticos.criar_arquivo_csv()
                crud_pontos_turisticos.deletar_ponto_turistico(id_ponto_turistico= 2)
                continuar = input("Deseja continuar manipulando ( (S)im / (N)ão )? ")
                if continuar == "N":
                    ...

            if menuCrud1 == "4":
                #LISTAR
                crud_pontos_turisticos.criar_arquivo_csv()
                crud_pontos_turisticos.listar_pontos_turisticos_cadastrados()
                continuar = input("Deseja continuar manipulando ( (S)im / (N)ão )? ")
                if continuar == "N":
                    ...

            if menuCrud1 == "5":
                #SAIR
                break
        #--------------------------------
        elif menuPrincipal == "2":
            os.system("cls")
            menu_usuarios()
            menuCrud2 = input("Escolha uma opção: ")
            if menuCrud2 == "1":
                #CADASTRAR
                crud_usuarios.criar_arquivo_csv()
                crud_usuarios.cadatrar_usuario(nome="Kerry", cpf= 39821937, idade= 19, email= "kkk@cesar.school", telefone= 321311, endereco="iwjiawhdihawdjj")
                continuar = input("Deseja continuar manipulando ( (S)im / (N)ão )? ")
                if continuar == "N":
                    ...

            if menuCrud2 == "2":
                #EDITAR
                crud_usuarios.criar_arquivo_csv()
                crud_usuarios.editar_informacao_usuario(id_usuario= 2, campo_de_alteracao= "Idade", nova_informacao= 24)
                continuar = input("Deseja continuar manipulando ( (S)im / (N)ão )? ")
                if continuar == "N":
                    ...

            if menuCrud2 == "3":
                #DELETAR
                crud_usuarios.criar_arquivo_csv()
                crud_usuarios.deletar_usuario(id_usuario= 2)
                continuar = input("Deseja continuar manipulando ( (S)im / (N)ão )? ")
                if continuar == "N":
                    ...

            if menuCrud2 == "4":
                #LISTAR
                crud_usuarios.criar_arquivo_csv()
                crud_usuarios.listar_usuarios_cadastrados()
                if continuar == "N":
                    ...

            if menuCrud2 == "5":
                #SAIR
                break
        #--------------------------------
        elif menuPrincipal == "3":
            os.system("cls")
            menu_estabelecimentos_comerciais()
            menuCrud3 = input("Escolha uma opção: ")
            if menuCrud3 == "1":
                #CADASTRAR
                crud_estabelecimentos_comerciais.criar_arquivo_csv()
                crud_estabelecimentos_comerciais.cadastrar_novo_estabelecimento_comercial(nome="Bode do nó",endereco="BV",                                                                         descricao="Restaurante", horario_de_funcionamento= "Seg - Sex: 12-22",                                                                           medio_de_avaliacoes="4.5")
                continuar = input("Deseja continuar manipulando ( (S)im / (N)ão )? ")
                if continuar == "N":
                    ...

            if menuCrud3 == "2":
                #EDITAR
                crud_estabelecimentos_comerciais.criar_arquivo_csv()
                crud_estabelecimentos_comerciais.editar_informacao_estabelicimento_comercial(id_estabelecimento_comercial= 1, campo_de_alteracao="Nome", nova_informacao="Shopping Recife")
                continuar = input("Deseja continuar manipulando ( (S)im / (N)ão )? ")
                if continuar == "N":
                    ...

            if menuCrud3 == "3":
                #DELETAR
                crud_estabelecimentos_comerciais.criar_arquivo_csv()
                crud_estabelecimentos_comerciais.deletar_estabelicimento_comerciais(id_estabelecimento_comercial= 1)
                continuar = input("Deseja continuar manipulando ( (S)im / (N)ão )? ")
                if continuar == "N":
                    ...

            if menuCrud3 == "4":
                #LISTAR
                crud_estabelecimentos_comerciais.criar_arquivo_csv()
                crud_estabelecimentos_comerciais.listar_estabelicimento_comerciais_cadastrados()
                if continuar == "N":
                    ...

            if menuCrud3 == "5":
                #SAIR
                break
        #--------------------------------
        else:
            print("Digite um número válido entre as opções.")
    os.system("cls")
    if menuPrincipal == "4":
        #quebrando o menu principal se a escolha for sair
        break
print("""
    -----------------------------------------------------------------------
    Ahh poxa... Espero que possa voltar e conhecer nosso sistema. Obrigado!
    -----------------------------------------------------------------------
    """)