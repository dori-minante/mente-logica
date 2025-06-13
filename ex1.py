# Crie um programa que declare as seguintes variáveis: 
# ● nome: seu nome.
# ● idade: sua idade.
# ● altura: sua altura.
# ● estudante: se você é estudante ou não (True/False).

nome = "Dori"
idade = 31
altura = 1.60
estudante = True

print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("Estudante: ", estudante)

# Ano do nascimento
ano_nascimento = 2025 - idade
print("Ano do nascimento: ", ano_nascimento)

# Verificar se é maior de idade
maior_de_idade = idade >= 18
print("Maior de idade: ", maior_de_idade)

# Manipulação de Strings
# Crie uma variável frase que contenha a mensagem: "Olá, meu nome é [seu nome] e eu tenho [sua idade] anos."
# Dica: Use str(idade) para converter o número inteiro em string antes de concatenar.
frase = ("Olá, meu nome é " + nome + " e eu tenho " + str(idade) + " anos.")
print(frase)
