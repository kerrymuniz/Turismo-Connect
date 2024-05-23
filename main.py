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
while True:
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
    menuPrincipal = input("Conteúdo de número ")

    while menuPrincipal != "4":
        if menuPrincipal == "1":
            os.system("cls")
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
            menuCrud1 = input("Escolha uma opção: ")
            if menuCrud1 != "5":
                ...
            if menuCrud1 == "1":
                ...
        elif menuPrincipal == "2":
            ...
        elif menuPrincipal == "3":
            ...
        else:
            print("Digite um número válido entre as opções.")
    os.system("cls")
    if menuPrincipal == "4":
        break
print("""
    -----------------------------------------------------------------------
    Ahh poxa... Espero que possa voltar e conhecer nosso sistema. Obrigado!
    -----------------------------------------------------------------------
    """)

#1º CRUD -> Pontos Turísticos
#crud_pontos_turisticos.criar_arquivo_csv()
#crud_pontos_turisticos.cadastrar_ponto_turistico(nome="Kerry", endereco="lkkkkkkkkkkk", descricao="Lugar aberto",horario_de_funcionamento= "Seg - Sex: 6:00 - 22:00", media_de_avaliacoes= "4.9" )
#crud_pontos_turisticos.cadastrar_ponto_turistico(nome="Prainha Zs", endereco="BV", descricao="Lugar aberto",horario_de_funcionamento= "Seg - Sex: 6:00 - 22:00", media_de_avaliacoes= "4.9" )
#crud_pontos_turisticos.editar_informacao_ponto_turistico(id_ponto_turistico= 3, campo_de_alteracao="Endereço", nova_informacao="Rua do Príncipe")
#crud_pontos_turisticos.deletar_ponto_turistico(id_ponto_turistico= 13)
#crud_pontos_turisticos.listar_pontos_turisticos_cadastrados()

#2º CRUD -> Usuários cadastrados
# crud_usuarios.criar_arquivo_csv()
# crud_usuarios.cadatrar_usuario(nome="Gilvando", cpf= 39821938, idade= 12, email= "ggg@cesar.school", telefone= 321312, endereco="iwjiawhdihawd")
# crud_usuarios.editar_informacao_usuario(id_usuario= 1, campo_de_alteracao= "Nome", nova_informacao= "João")
# crud_usuarios.deletar_usuario(id_usuario= 1)
# crud_usuarios.listar_usuarios_cadastrados()

# #3º CRUD -> Estabelecimentos Comerciais
# crud_estabelecimentos_comerciais.criar_arquivo_csv()
# crud_estabelecimentos_comerciais.cadastrar_novo_estabelecimento_comercial(nome="Bode do nó", endereco="BV", 
#                                                                           descricao="Restaurante", horario_de_funcionamento= "Seg - Sex: 12-22",
#                                                                           medio_de_avaliacoes="4.5")
# crud_estabelecimentos_comerciais.editar_informacao_estabelicimento_comercial(id_estabelecimento_comercial= 1, campo_de_alteracao="Nome", nova_informacao="Shopping Recife")
# crud_estabelecimentos_comerciais.deletar_estabelicimento_comerciais(id_estabelecimento_comercial= 1)
# crud_estabelecimentos_comerciais.listar_estabelicimento_comerciais_cadastrados()