pessoas = {}

for i in range(3):
    cpf = int(input('CPF: '))
    nome = input('Nome: ')
    idade = int(input('Idade: '))

    pessoas[cpf] = { 'nome':nome, 'idade':idade }

print(pessoas)