import json 
import os

""" ONDE SERÁ SALVO O ARQUIVO """
NOME_ARQUIVO = 'aula177.json'

CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

str_json = {
    'workbench_colorTheme': 'Default Dark Modern', 'workbench_iconTheme': 'material-icon-theme', 'editor_fontSize': 20, 'editor_fontWeight': '500', 'editor_fontFamily': 'Raleway', 'editor_minimap.enabled': False, 'editor_wordWrap': 'on', 'terminal_integrated.fontSize': 22, 'terminal_integrated.fontFamily': 'monospace', 'terminal_integrated.fontWeight': 'bold'
            }

#ABRIR O ARQUIVO EM MODO DE ESCRITA 
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(str_json, arquivo)
 
#LER O ARQUIVO
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    leitor = json.load(arquivo)
    for a in leitor:
        print(a)
    