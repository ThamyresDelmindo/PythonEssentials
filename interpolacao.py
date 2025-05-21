#!/usr/bin/env python3
Olá, %(nome)s
    ...: 
    ...: Tem interesse em comprar uma  %(produto)s?
    ...: 
    ...: Este produto é ótimo para resolver 
    ...: %(texto)s
    ...: 
    ...: Clique agora em %(link)s
    ...: 
    ...: Apenas %(quantidade)d disponíveis!
    ...: 
    ...: Preço promocional %(preço).2f
    ...: """

In [71]: for cliente in clientes:
    ...:     print(email_tmpl % {"nome": cliente, "produto": "caneta", "texto": "Problemas de má escrita 
       ⋮ e dores no pulso", "link": "https://canetaslegais.com", "quantidade": 1, "preço": 50.5, }) 