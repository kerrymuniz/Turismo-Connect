import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
class PontosTuristicos:

    def __init__(self):

        self.diretorio = os.getenv("path_directory")
        self.arquivo_csv = os.path.join(self.diretorio, "Pontos_turisticos.csv")
        

        if os.path.exists(self.arquivo_csv):
            self._pontos_turisticos = pd.read_csv(self.arquivo_csv)

        else:
            self._colunas = ["ID", "Nome", "Endereço", "Descrição", "Horários de funcionamento", "Média das avaliações"]
            self._pontos_turisticos = pd.DataFrame(columns=self._colunas)

    def criar_arquivo_csv(self):

        try:

            if not os.path.exists(self.diretorio):
                os.makedirs(self.diretorio)

            self._pontos_turisticos.to_csv(self.arquivo_csv, sep=',', index=False, encoding='utf-8')
            print(f"Arquivo CSV criado com sucesso em {self.arquivo_csv}!")
            
        except Exception as exc:

            print(f'Não foi possível criar o arquivo CSV: {exc}')
        
        finally:

            print("Não foi necessário criar um novo arquivo csv")

    def cadastrar_ponto_turistico(self, nome, endereco, descricao, horario_de_funcionamento, media_de_avaliacoes):

        novo_ponto_turistico = pd.DataFrame({
            'ID': [self._pontos_turisticos["ID"].iloc[-1] + 1],
            'Nome': nome,
            'Endereço': endereco,
            'Descrição': descricao,
            'Horários de funcionamento': horario_de_funcionamento,
            'Média das avaliações': media_de_avaliacoes
        })

        self._pontos_turisticos = pd.concat([self._pontos_turisticos, novo_ponto_turistico], ignore_index=True)

        self._pontos_turisticos.to_csv(self.arquivo_csv, sep=',', index=False, encoding='utf-8')
        print("Ponto cadastrado com sucesso!")

    def listar_pontos_turisticos_cadastrados(self):

        return print(self._pontos_turisticos.to_string(index= False)) #N mostra o index

    def editar_informacao_ponto_turistico(self, id_ponto_turistico, campo_de_alteracao, nova_informacao):

        if id_ponto_turistico not in self._pontos_turisticos['ID'].values:
            print("ID do ponto turístico não encontrado.")

        self._pontos_turisticos.loc[self._pontos_turisticos["ID"] == id_ponto_turistico, campo_de_alteracao] = nova_informacao
        
        self._pontos_turisticos.to_csv(self.arquivo_csv, sep=',', index=False, encoding='utf-8')

        print(f"A informacao {campo_de_alteracao} do ponto turístico de id {id} foi alterada com sucesso!")

    def deletar_ponto_turistico(self, id_ponto_turistico):

        if id_ponto_turistico not in self._pontos_turisticos['ID'].values:
            print("ID do ponto turístico não encontrado.")

        self._pontos_turisticos= self._pontos_turisticos[self._pontos_turisticos["ID"] != id_ponto_turistico]
        self._pontos_turisticos.to_csv(self.arquivo_csv, sep=',', index=False, encoding='utf-8')
