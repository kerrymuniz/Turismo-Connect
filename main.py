import crud_pontos_turisticos

crud_pontos_turisticos = crud_pontos_turisticos.PontosTuristicos()

crud_pontos_turisticos.criar_arquivo_csv()

crud_pontos_turisticos.cadastrar_ponto_turistico(nome="Pedro", endereco="lkkkkkkkkkkk", descricao="Lugar aberto",horario_de_funcionamento= "Seg - Sex: 6:00 - 22:00", media_de_avaliacoes= "4.9" )

#crud_pontos_turisticos.cadastrar_ponto_turistico(nome="Prainha Zs", endereco="BV", descricao="Lugar aberto",horario_de_funcionamento= "Seg - Sex: 6:00 - 22:00", media_de_avaliacoes= "4.9" )

#crud_pontos_turisticos.editar_informacao_ponto_turistico(id_ponto_turistico= 1, campo_de_alteracao="Endereço", nova_informacao="Rua apolo")

#crud_pontos_turisticos.deletar_ponto_turistico(id_ponto_turistico= 1)

crud_pontos_turisticos.listar_pontos_turisticos_cadastrados()


