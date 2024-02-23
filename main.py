import tkinter as tk
from tkinter import filedialog
import json
from pprint import pprint
import os
from venv import logger

# script para instalar todas as dependências
# pip freeze > requirements.txt
# pip install -r requirements.txt
# pip install --upgrade pip


def escolher_arquivo():
    root = tk.Tk()
    root.withdraw()  # para esconder a janela principal
    caminho_arquivo = filedialog.askopenfilename()
    return caminho_arquivo

# lê o objeto json do documento escolhido
    
# {
#     "uid": "t5318n64i",
#     "type": "core_logger",
#     "data": {
#         "x": 4389,
#         "y": 310,
#         "message_type": "message_parsed_text",
#         "message": "Status {{json msg.response.status}} : EAN {{msg.product_response.sku}} ID {{msg.product_response.id}}",
#         "description": "Operação - Adobe Commerce - Integração de produto",
#         "label": "Operação - Adobe Commerce - Integração de produto"
#     }
# }

# função para acessar o tipo do objeto e verificar se é do tipo core_logger 
def verificar_tipo_core_logger(objeto):
    if 'type' in objeto:
        if objeto['type'] == 'core_logger':
            return True
    return False

def ler_arquivos_json(diretorio):
    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio)

    # Filtra apenas os arquivos .json
    arquivos_json = [arquivo for arquivo in arquivos if arquivo.endswith('.json')]
    loggers_por_arquivo = {}  # Cria um dicionário vazio
    # Itera sobre cada arquivo .json e lê seu conteúdo
    for arquivo_json in arquivos_json:
        caminho_arquivo = os.path.join(diretorio, arquivo_json)
        with open(caminho_arquivo, 'r') as f:
            lista_dados = json.load(f)
        
        loggers = []  # Cria uma lista vazia para armazenar os loggers deste arquivo
        # Itera sobre cada dicionário na lista
        for dados in lista_dados:
            # Agora você pode acessar 'nodes' em 'dados'
            for objeto in dados['nodes']:
                if verificar_tipo_core_logger(objeto):
                    uid = objeto['uid']
                    tipo = objeto['type']
                    # Usa o método get() para obter o label, ou 'Label não encontrado' se não existir
                    label = objeto['data'].get('label', 'Label não encontrado')
                    loggers.append({'uid': uid, 'type': tipo, 'label': label})
        
        # Adiciona os loggers deste arquivo ao dicionário
        loggers_por_arquivo[arquivo_json] = loggers
    return loggers_por_arquivo

def ler_arquivo():
    caminho_arquivo = escolher_arquivo()  
    print(f"Arquivo escolhido: {caminho_arquivo}")
    conteudo = json.load(open(caminho_arquivo))
    # nomeio o objeto json com o nome do arquivo escolhido
    nome_arquivo = caminho_arquivo.split('/')[-1].split('.')[0]
    dados = {}
    loggers = []
    
    # acessa o coneudo.nodes e verifica se o tipo é core_logger
    for objeto in conteudo['nodes']:
        if verificar_tipo_core_logger(objeto):
            # retorna os atributos uid, type, data.label
            uid = objeto['uid']
            tipo = objeto['type']
            if 'data' in objeto:
                if 'label' in objeto['data']:
                    label = objeto['data']['label']
                else:
                    label = ''
            loggers.append({'uid': uid, 'type': tipo, 'label': label.encode('utf-8').decode('utf-8')})
    dados['loggers'] = loggers
    dados['arquivo'] = nome_arquivo
    return dados

def atualizar_loggers(loggers):
    with open('loggers.json', 'r') as f:
        data = json.load(f)
    data[loggers['arquivo']] = loggers['loggers']
    with open('loggers.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)
    return data

try:
    diretorio = "./flows/"
    logs = ler_arquivo()
    atualizar_loggers(logs)
    
    print(f"Loggers atualizados.")
    
except Exception as e:
    print(f"Erro: {e}")
    