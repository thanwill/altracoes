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


# função para acessar o tipo do objeto e verificar se é do tipo core_logger 
def verificar_tipo_core_logger(objeto):
    if 'type' in objeto:
        if objeto['type'] == 'core_logger':
            return True
    return False

def ler_diretorio(cliente):
    # Lista todos os arquivos no diretório
    arquivos = os.listdir("./flows/")
    
    # limpa a string cliente
    cliente = cliente.replace(' ', '')
    
    dados = []
    for arquivo in arquivos:
        dado = ler_arquivo(f"./flows/{arquivo}")
        dados.append(dado)
    with open(cliente+'-loggers.json', 'w') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4, sort_keys=True)
    print("Quantidade de arquivos listados: ", len(arquivos))
    return dados

def ler_arquivo(caminho_arquivo):
         
    conteudo = json.load(open(caminho_arquivo))
    # nomeio o objeto json com o nome do arquivo escolhido
    # staging-sincronizao-de-categorias-20240223173739
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
    dados['ambiente'] = nome_arquivo.split('-')[0]
    dados['loggers'] = loggers
    dados['arquivo'] = '-'.join(nome_arquivo.split('-')[:-1])
    return dados


try:
    print("Iniciando")
    print("Defina um nome de cliente")
    cliente = input()
    ler_diretorio(cliente)
    print("Finalizado")
except Exception as e:
    print(f"Erro: {e}")
    