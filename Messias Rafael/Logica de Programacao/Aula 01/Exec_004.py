# coding=utf-8
'''
Ecercico 04
Exercício do Desconto: Escreva um programa em Python que solicite ao usuário o valor de um produto e o percentual de
desconto. Calcule o valor do desconto e exiba o valor final após o desconto.
'''

valor    = float(input('Digite o Valor do Produto : '))
desconto = float(input('Digite o Percentual de Desconto %: '))

vlr_desc = (valor * (desconto / 100))

vlr_final = ( valor - vlr_desc)

print('Sub-Total : {}' .format(valor))
print('Desconto  : {}' .format(vlr_desc))
print('Total C/Desconto : {}'. format(vlr_final))
