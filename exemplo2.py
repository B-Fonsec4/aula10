#  Dicionario de Dicionário
pessoas ={}
for i in range(1):
    nome = input('Digite o nome: ')
    email = input('Digite o email: ')
    idade = input('Digite a idade: ')
    cpf = input('Digite o cpf: ')

    pessoas[nome] = {
        'EMAIL': email,
        'IDADE': idade,
        'CPF': cpf
    }

print(pessoas[nome]['EMAIL'])