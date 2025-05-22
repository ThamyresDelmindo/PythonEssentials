#!/usr/bin/env python3
"""Documentação do meu programa.
Hello World - Português - BR

Meu primeiro script em Python realizado pelo treinamento Phyton Base da 
LinuxTips.

Dependendo da língua configurada no ambiente o 
programa exibe a mensagem correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR
Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Thamyres Delmindo"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello World",
    "pt_BR": "Olá, Mundo",
    "it_IT": "Ciao, Mondo",
    "es_SP": "Hola, Mundo",
    "fr_FR": "Bonjour, Monde",
}

#Ordem de complexidade - código está complexo demais - chamado de O(n)
#if current_language == "pt_BR":
 #   msg = "Olá, Mundo!"
#elif current_language == "it_IT":
#    msg = "Ciao, Mondo!"
#elif current_language == "es_SP":
 #   msg = "Hola, Mundo!"
#elif current_language == "fr_FR":
 #   msg = "Bonjour Monde"
    
print(msg[current_language])
