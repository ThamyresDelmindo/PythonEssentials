pseudo codigo
import ir, pegar, pedir, tem, comer, ficar

#Premissas
today - "Segunda"
hora = 15
natal = False
chovendo = True
frio = True
nevando = True
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
feriado = ["Quarta"]
horario_padaria = {
    "semana": 19,
    "fds": 12
}

# Algoritmo

if today in feriado and not natal:
    padaria_aberta = False
elif today not in semana and hora < horario_padaria["fds"]
    padaria_aberta = True
elif today in semana and hora < horario_padaria["semana"]:
    padaria_aberta = True
else:
    padaria_aberta = False