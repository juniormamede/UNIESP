# coding=utf-8
'''
Ecercico 11
Desenvolva um programa para calcular a venda de maçãs em uma banca de feira. O cliente compra maçãs custando
R$ 1,37 cada uma, mas caso ele compre a partir de uma dúzia pagará com desconto de 10%, portanto o valor da unidade
ficará por R $1,24. O programa deverá receber o número de maçãs desejadas pelo cliente, e retornar o valor total da
compra
'''

v_qt01     = float(input('Digite a Quantide de Maça Desejada : '))
v_unit     = 1.37
v_unitdesc = 1.24
v_economia = ( 1.37 - 1.24 )



if v_qt01 < 12:
     print('A quantidade Comprada é de : {:.2f}'.format(v_qt01))
     print('Preco Sem Desconto........ : {:.2f}' .format(v_unit))
     print('Total..................... : {:.2f}'.format(v_qt01 * v_unit))
elif v_qt01 >= 12:
     print('A quantidade Comprada é de : {:.2f}'.format(v_qt01))
     print('Preco C/ Desconto......... : {:.2f}'.format(v_unitdesc))
     print('Voce teve uma economia de  : {:.2f}'.format(v_qt01 * v_economia))
     print('Total..................... : {:.2f}'.format(v_qt01 * v_unitdesc))
elif v_qt01 == 0:
     print('A quantidade Comprada é de: {:.2f}'.format(v_qt01))
     print('Total: {:.2f}'.format(v_qt01 * v_unit))