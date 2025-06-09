#!/usr/bin/env python3
"""Cadastro de Produto"""
__version__ = "0.1.0"

import pprint

#dicionario
produto = {
    "nome": "Caneta",
    "cores": ["azul", "amarelo"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    }, 
    "estoque": True,
    "codigo": 45678,
    "codebar": None,
}

#selecionando a variável na ordem
compra = ("Bruno", "nome", 3)

#dicionario somente para o bruno
cliente = {
    "nome": "Bruno"
}

#colocando a variável criada conforme a ordem
compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

#pprint.pprint(compra)

#declarando uma variável nova para facilitar o código
total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']}" 
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}" 
    f" e pagou o total de {total_compra}"
)