#!/usr/bin/env python3

original = [1, 2, 3]
# For loops / Laço for
dobrada = []
# for n in original:
#     dobrada.append(n * 2)
# print(dobrada)

# dobrada = [n * 2 for n in original] #List comprehension 
# print(dobrada)
# dict comprehension
dados = [line for line in open("post.txt")]
print(dados)

# dados = {}
# for line in open("post.txt"):
#     if line == "---\n":
#         break
#     key, valor = line.split(":")
#     dados[key] = valor.strip()

# print(dados)