# condicao para cada funcao da lista

# 1 - Adicionar Pessoas
# 2 - Pesquisar uma Pessoa
# 3 - Listar Pessoas]
# 4 - Remover

lista = []
while True:
    print('1 - ADICIONAR\n'
          '2 - PESQUISAR\n'
          '3 - LISTAR\n'
          '4 - REMOVER\n'
          '5 - ALTERAR')
    opcao = int(input('Digite a Opção Desejada : '))

    if opcao == 1:
        nome_pessoa = input('Digite o Nome da Pessoa : ').upper()
        lista.append(nome_pessoa)
        print(f'{nome_pessoa}, inserida com sucesso!', )
    elif opcao == 2:
        nome_pesquisa = input('Digite o nome a ser pesquisado :').upper()
        if nome_pesquisa in lista:
            print(f'O nome : {nome_pesquisa}, foi encontrado em nossa lista\nPosição : {lista.index(nome_pesquisa)}')
        else:
            print(f'Nome {nome_pesquisa}, não foi encontrado')
    elif opcao == 3:
        for nome in lista:
            print(f'-> Posicao : {lista.index(nome)} Nome Encontrado -> {nome}')
    elif opcao == 4:
        nome_remover = input('Digite o Nome a ser removido : ').upper()
        if nome_remover is lista:
            lista.remove(nome_remover)
        else:
            print('Nome não encontrado!')
    elif opcao == 5:
        print(lista)
        nome_alterar = input('Digite o nome a ser alterado : ').upper()
        if nome_alterar in lista:
            print(f'O nome {nome_alterar}, foi encontrado.')
            alteracao = input('Digite o novo nome : ').upper()
            lista[lista.index(nome_alterar)] = alteracao
        else:
            print('O nome nao foi Localizado')