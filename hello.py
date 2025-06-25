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
    python3 hello.py --lang=en_US (Count só se quiser a repetição em si)
"""
__version__ = "0.0.3"
__license__ = "Unlicense"

import os
import sys
#Meu python3 Hello World não vai sozinho, por alguma config sistêmica que não irei mecher
#Mas se eu rodar a lang corretamente que quero, ele roda tranquilo o Hello World
#python3 hello.py --lang=en_US --count=2
arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        #TODO: Substituir essas linhas com loggin
        print(f"[ERROR] {str(e)}")
        print("You need to use `=`")
        print(f"You passed {arg}")
        print("Try with --key=value")
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()
    
    # Validação
    if key not in  arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()

    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello World",
    "pt_BR": "Olá, Mundo",
    "it_IT": "Ciao, Mondo",
    "es_SP": "Hola, Mundo",
    "fr_FR": "Bonjour, Monde",
}

"""
message = msg.get(current_language, msg["en_US"])
"""

# EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(
    message * int(arguments["count"])
)  

#Ordem de complexidade - código está complexo demais - chamado de O(n)
#if current_language == "pt_BR":
 #   msg = "Olá, Mundo!"
#elif current_language == "it_IT":
#    msg = "Ciao, Mondo!"
#elif current_language == "es_SP":
 #   msg = "Hola, Mundo!"
#elif current_language == "fr_FR":
 #   msg = "Bonjour Monde"
    
