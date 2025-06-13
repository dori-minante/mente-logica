# ● Peça ao usuário para inserir dois números e armazene-os em variáveis.
# ● Calcule a soma, subtração, multiplicação e divisão desses números.
# ● Exiba os resultados.

# Observação: A função input() permite que o usuário insira dados. 
# Usamos float()para converter a entrada em um número de ponto flutuante.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("Soma: ", soma)
print("Subtração: ", subtracao)
print("Multiplicação: ", multiplicacao)
print("Divisão: ", divisao)