import sys

em_uso = open("reservas.txt").readlines()

print("Segue nosso catálogo de quartos disponíveis para reserva")

try:
    quartos = open("quartos.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
print(quartos)

valores = {
    1: 500,
    2: 200,
    3: 100,
    4: 50
}

catalogo = {
    1: "Suite Master",
    2: "Quarto Familia",
    3: "Quarto Single",
    4: "Quarto Simples"
}

nome_cliente = input("Digite seu nome")
quarto_desejado = int(input("Qual o quarto desejado?"))
if quarto_desejado not in valores:
    print("Escolha inválida, tente novamente escolhendo um quarto por vez com 1, 2, 3 ou 4")
    sys.exit(1)

for itens in em_uso[1:]:
    if quarto_desejado == int(itens.split(",")[1].strip()):
        print("Este quarto já está em uso")
        sys.exit(1)
    else:
        continue
dias_reserva = int(input("A reserva é para quantos dias?"))

with open("reservas.txt", "a") as file:
    novo_cliente = f"{nome_cliente}, {quarto_desejado}, {dias_reserva}\n"
    file.write(novo_cliente)


quarto_escolhido = catalogo[quarto_desejado]
preco_final = valores[quarto_desejado] * dias_reserva

resumo_do_pedido = f"Sua reserva do quarto {quarto_escolhido} para {dias_reserva} dia(s) ficou no valor de R${preco_final}"
print(resumo_do_pedido)