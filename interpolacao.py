#!/usr/bin/env python

"""Imprime a mensagem de um e-mail

NÃO MANDE SPAM!!!
"""
__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informa o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

for line in open(filepath):
    name, email = line.split(",")
    print(f"Enviando email para: {email}")
    print(
        open(templatepath).read()
        % {
            "nome": name,   
            "produto": "caneta", 
            "texto": "Problemas de má escrita e dores no pulso", 
            "link": "https://canetaslegais.com", 
            "quantidade": 1, 
            "preço": 50.5, 
        }
    ) 
    print("-" * 50)