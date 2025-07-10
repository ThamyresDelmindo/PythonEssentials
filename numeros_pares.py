#! usr/bin/env python3
"""
Faça um programa que imprima os números pareas de 1 a 200

ex
'python3 numeros_pares.py´
2
4
6
8
...
"""

for numero_par in range(1, 201):
    if numero_par % 2 != 0:
        continue
    print(numero_par)