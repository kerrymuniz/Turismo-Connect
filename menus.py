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
                crud_pontos_turisticos.criar_arquivo_csv()
                crud_pontos_turisticos.cadastrar_ponto_turistico(nome="Gilvando", endereco="rua do gil", descricao="Lugar Aberto",horario_de_funcionamento= "Seg - Sex: 6:00 - 22:00", media_de_avaliacoes= "4.9" )
                continuar = input("Deseja continuar manipulando ( (S)im / (N)ão )? ")
                if continuar == "N":
                    

            if menuCrud1 == "2":
                ...
            if menuCrud1 == "3":
                ...
            if menuCrud1 == "4":
                ...
            if menuCrud1 == "5":
                ...

        elif menuPrincipal == "2":
            ...
            
        elif menuPrincipal == "3":
            ...

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