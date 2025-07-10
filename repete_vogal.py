"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palavras com suas vogais duplicadas.

ex.
python3 repete_vogal.py
'Digite uma palavra (ou Enter para sair):'Python
'Digite uma palavra (ou Enter para sair): 'Bruno
'Digite uma palavra (ou Enter para sair): <enter>
Pythoon
Bruunoo
"""
palavras = []
vogais = ["a", "e", "i", "o", "u"]
while True:
    palavra = input("Digite uma palavra (ou Enter para sair): ")
    if not palavra:
            break

    letra_final = ""
    for letra in palavra:
        if letra in "aeiou":
            letra_final += letra * 2 
        else:
            letra_final += letra 

    palavras.append(letra_final)
print(palavras)        
    

