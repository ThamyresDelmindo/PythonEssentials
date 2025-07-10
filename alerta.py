#! usr/bin/venv python3

"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e  o índice de
umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo
das condições:

temp maior 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
temp entre 10 e 30: Normal
temp entre 0 e 10: Frio
temp <0: ALERTA: Frio extremo
"""

temp_atual = float(input("Qual a temperatura atual?\n>>").strip())
ind_umid = float(input("Qual o índice de umidade do ar atual?\n>>").strip())

if temp_atual > 45:
    print("ALERTA!!! Perigo calor extremo")
elif temp_atual * 3 >= ind_umid:
    print("ALERTA!!! Perigo de calor úmido")
elif 10 <= temp_atual  <= 30:
    print("Normal")
elif 0 < temp_atual <= 10:
    print("Frio")
elif temp_atual < 0:
    print("ALERTA: Frio extremo")