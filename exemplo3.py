import os
os.system('cls')


import pandas as pd 



dados = {
    'cargos': ['assistente', 'auxiliar', 'gerente'],
    'salarios': [2500, 1800, 750]
}
dados_bi = pd.DataFrame(dados)
print(dados_bi)

# dados_cargos = pd.Series(dados['cargos'])
# print(dados_cargos.values) printa os valores
# print(dados_cargos.index) printa os indices

# imprime a linha do indice
# df_linha = dados_bi.iloc[1]
# print(df_linha)


# mais indicado para 'rotulos em texto'
# df_linha = dados_bi.loc[1]
# print(df_linha)

# acessando os valores individuais
print(dados_bi.iloc[1]['cargos'])
print(dados_bi.iloc[1]['salarios'])