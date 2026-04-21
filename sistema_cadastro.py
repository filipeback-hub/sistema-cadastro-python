#Projeto
from time import sleep
print('\033[1;4mSISTEMA DE CADASTRO + ESTATISTICA\033[m')
total = 0
pessoas = []
TotIdade = 0
media = 1
velho = 0
NomeVelho = 0
homem = 0
mulher = 0
while True:
    print('==='*10)
    print('''Digite:
    [1] Para cadastrar pessoa
    [2] Para Ver estatistica
    [3] Para lista de pessoas
    [4] Para sair''')
    opcao = int(input('Qual sua opção? '))
    if opcao == 1:
        print('CADASTRO:')
        nome = str(input('Nome: ')).title()
        idade = int(input('Idade: '))
        sexo = str(input('Sexo:[M/F] ')).strip().upper()[0]
        pessoa = [nome, idade, sexo]
        pessoas.append(pessoa)
        total += 1
        TotIdade += idade
        media = TotIdade / total
        if idade > velho:
            velho = idade
            NomeVelho = nome
        if sexo in 'M':
            homem += 1
        if sexo in 'F':
            mulher += 1
    elif opcao == 2:
        print('ESTATISTICAS')
        print(f'Pessoas cadastradas: {total}')
        print(f'Média de idade das pessoas cadastradas: {media:.1f}')
        print(f'Pessoa de maior idade: {NomeVelho}, {velho} anos')
        print(f'Homem/ns cadastrado/os: {homem}')
        print(f'Mulher/es cadastrada/s: {mulher}')
    elif opcao == 3:
        print('LISTA DE PESSOAS CADASTRADAS')
        for p in pessoas:
            print(f'Nome: {p[0]} | Idade: {p[1]} | Sexo: {p[2]}')
    elif opcao == 4:
        print('FINALIZANDO')
        sleep(2)
        print('Fim do programa. Volte sempre')
        break
    else:
        print('Opção invalida. Tente novamente!')
