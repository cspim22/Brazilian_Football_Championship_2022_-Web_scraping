# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class SqlitePipeline(object):
    # Função responsavel por criar o banco de dados
    def open_spider(self, spider):
        
        # cria um banco de dados e salva em uma variavel chamada self.connection
        self.connection = sqlite3.connect('brasileirao2022.db')

        # Cria um cursor para habilitar a comunicação com o banco de dados
        self.cursor = self.connection.cursor()

        # Cria a tabela do banco de dados, a tabela recebe o nome de tabela (após o comando CREATE TABLE IF NOT EXISTS)
        # Os campos Time, Pontos e Vitorias recebem os mesmo que está definidos no Spider
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabela(
        TIMES TEXT NOT NULL PRIMARY KEY,
        PONTOS NUMBER,
        VITORIAS NUMBER
        )
        ''')
        self.connection.commit()

    # Função responsavel por finalizar a conecção com o banco de dados
    def close_spider(self, spider):
        self.connection.close()

    # Função responsavel por adicionar valores/ manipular o banco de dados
    def process_item(self, item ,spider):
        self.cursor.execute(''' 
        INSERT OR IGNORE INTO tabela(TIMES,PONTOS,VITORIAS) VALUES (?,?,?)''', (
            item.get('time'),
            item.get('pontos'),
            item.get('vitorias')
        ))
        self.connection.commit()
        return item
    



# No arquivo settings modificar a linha:

# ITEM_PIPELINES = {
#   "nome_do_arquivo.pipelines.nome_da_classe_criada_em_pipelines": 300,
#}