import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula178.csv'

#LER O ARQUIVO
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)
    #print(next(leitor))
    for dados in leitor:
        print(dados[1])

#LER O ARQUIVO - DICIONARIO
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for dados in leitor:
        print(dados['Nome'])