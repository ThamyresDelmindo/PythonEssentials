#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notes.py 1 tech
...
...
"""
__Version__ = "0.1.0"

import os
import sys

cmds = ("read", "new")
path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must specify subcommand {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")
while True:

    if arguments[0]  == "read":
        try:
            arg_tag = arguments[1].lower()
        except IndexError:
            arg_tag = input("Qual a tag?").strip().lower()
        # leitura das notas
        for line in open(filepath):
            title, tag, text = line.split("\t")
            if tag.lower() == arg_tag:
                print(f"title: {"title"}")
                print(f"text: {"text"}")
                print("-" * 30)
                print()

    if arguments[0] == "new":
        try:
            title = arguments[1] #TODO: Tratar exception
        except IndexError:
            title = input("qual é o título: ").strip().title()

        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),
        ]
        # \t - tsv - separa por tag (n entendi muito bem)
        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")
    cont = input("Quer continuar adicionando notas? [N/Y]").strip().lower()
    if cont != "y":
        break