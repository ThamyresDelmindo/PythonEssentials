#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10"""
__version__ = "0.1.0"
___author___ = "Thamyres"

# iterable(percorríveis, pode percorrer cada um dos itens, um a um)
# base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list (range(1,11))
largura = 18

for n in numeros:
    print("{:^{}}".format(f"Tabuada do {n}", largura), end="")
print()

print("-" * largura * len(numeros))

for linha in range (1, 11):
    for n in numeros:
        print("{:^{}}".format(f"{n} x {linha} = {n*linha}", largura), end="")  
    print()     

print("-" * largura * len(numeros))