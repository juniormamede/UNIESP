# coding=utf-8
'''
Ecercico 03
Exercício da Média: Escreva um programa em Python que solicite ao usuário duas notas e calcule a média entre elas. Em
seguida, exiba o resultado na tela.

nota1 = None
while nota1 is None or nota1 == 0:
    valor_nota = input('Digite a 1ª Nota : ')
    if valor_nota.strip() != '':
        nota1 = float(valor_nota)
'''

nota1 = None
while nota1 is None:
    valor_nota = input('Digite a 1ª Nota : ')
    try:
        nota1 = float(valor_nota)
    except ValueError:
        print('Valor inválido. Digite novamente.')


nota2 = None
while nota2 is None:
    valor_nota = input('Digite a 2ª Nota : ')
    try:
        nota2 = float(valor_nota)
    except ValueError:
        print('Valor inválido. Digite novamente.')

nota3 = None
while nota3 is None:
    valor_nota = input('Digite a 3ª Nota : ')
    try:
        nota3 = float(valor_nota)
    except ValueError:
        print('Valor inválido. Digite novamente.')



media = (nota1 + nota2 + nota3)/3

'''print(f'Media Alcancada : {media}')'''
print('Media Alcancada : {} !!!!'.format(media))


if   media >= 8              :
        print('SUA MÉDIA FOI : {:.2f} '.format(media))
        print(' =) ')
        print('VOCE ESTA DE PARABENS!!!!')
elif media >= 6 and media < 8:
        print('SUA MÉDIA FOI : {:.2f}' .format(media) )
        print(' =/ ' )
        print('VOCE ESTA NO CAMINHO CERTO!!!!')
elif media >= 4 and media < 6:
        print('SUA MÉDIA FOI : {:.2f}' .format(media) )
        print(' =( ' )
        print('PRECISA MELHORAR!!!!')
else                         :
        print('ABAIXO DA MÉDIA : {:.2f} ' .format(media) )
        print(' ¬¬ ')
        print('ESTUDE MAIS!!!!')
