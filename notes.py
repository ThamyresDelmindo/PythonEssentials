#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia

$ notes.py read --tag=tech
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

if arguments[0]  == "read":
    # leitura das notas
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {"title"}")
            print(f"text: {"text"}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    title = arguments[1] #TODO: Tratar exception
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
    # \t - tsv - separa por tag (n entendi muito bem)
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")