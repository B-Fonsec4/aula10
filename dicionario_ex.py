import os

os.system('cls')
dicionario = {
           'nome': 'João',
            'telefone': '92345-6789',
            'idade': 25,
            'cpf': '023.548.985.54'
}

# Acesaar valores do dicionario
print(dicionario['nome'])
print(dicionario['telefone'])
print(dicionario['idade'])

# Aletera valores do dicionario
dicionario['nome'] = 'paula'
print(dicionario)

# criando novas chaves e valores para o dicionario
dicionario['email'] = 'maria@gmail.com'
dicionario['idade'] = 25

# REmover chaves do dicionario - del
del dicionario['email']
print(dicionario)

# Remover chaves do dicionario - pop retorna o valor da chave apagada
print(dicionario.pop('idade' , 'não encontrado'))
print(dicionario)