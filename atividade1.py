alunos = {}

for i in range(2):
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a nota: '))
    nota2 = float(input('Digite a nota: '))
    nota3 = float(input('Digite a nota: '))
    nota4 = float(input('Digite a nota: '))

    media = ( nota1 + nota2 + nota3 + nota4) /4

    alunos[nome] ={
        'Primeira_Nota': nota1,
        'Segunda_Nota': nota2,
        'Terceira_Nota': nota3,
        'Quarta_Nota': nota4,
        'Media': media
    } 
print(alunos)