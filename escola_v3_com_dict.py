#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala 
que frequentam cada uma das atividades.
"""

__version__ = "0.1.2"

# DICIONARIO

aulas = {
    "aula_ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"], 
    "aula_musica": ["Erik", "Carlos", "Maria"],
    "aula_danca": ["Gustavo", "Sofia", "Joana", "Antonio"],
}
salas = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["João", "Antonio", "Carlos", "Maria", "Isolda"],
}
nome_aulas = {
    "aula_ingles": "Ingles",
    "aula_musica": "Musica",
    "aula_danca": "Dança",
}

nome_salas = {
    "sala1": "Sala 01",
    "sala2": "Sala 02",
}
for aula in aulas:
    print(f"Alunos de {nome_aulas[aula]}\n")
    print("-" * 50)
    alunos_sala1 = []
    alunos_sala2 = []


    for aluno in aulas[aula]:
        if aluno in salas["sala1"]:
            alunos_sala1.append(aluno)
        elif aluno in salas["sala2"]:
            alunos_sala2.append(aluno)


    print("sala1", alunos_sala1)
    print("sala2", alunos_sala2)

    #print(salas, {nome_salas[salas]}\n")
   # print(aulas)
    print("-" * 50)
    

    # sala1 que tem interseção com a atividade


    
    

