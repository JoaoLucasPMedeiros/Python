import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'


lista_clientes = [
    {'nome': 'joao', 'endereco':'rua rio congo, 139' },
    {'nome': 'lucas', 'endereco':'rua da polca, 382' }  
]


with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys() #CRIA UM TOPO
    escritor = csv.DictWriter( 
        arquivo,
        fieldnames=nome_colunas #NOME DOS CAMPOS
    )

    escritor.writeheader() #ESCREVENDO AS COLUNAS
    for cliente in lista_clientes:
         escritor.writerow(cliente) #ESCREVENDO AS LINHAS
  