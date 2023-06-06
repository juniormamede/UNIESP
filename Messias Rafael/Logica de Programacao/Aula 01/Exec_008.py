# coding=utf-8
'''
Exercicio 08
Exercício da Conversão de Moedas: Escreva um programa em Python que solicite ao usuário um valor em Real (BRL) e
faça a conversão desse valor para Dólar Americano (USD). Considere a taxa de câmbio fixa de 1 USD = 5 BRL. Exiba o
valor convertido na tela.
'''

v_real = float(input('Digite o Valor em Real : '))

calculo_dolar = (v_real / 5)
#print(f'O valor digitado em Real e de R$ : {v_real}, convertido fica UR$ {calculo_dolar}' )

#opcao 02
print(f'O valor digitado em Real e de R$ : {v_real}, convertido fica UR$ {v_real / 5}' )

#opcao 03
print('O valor digitado em Real é de R$ {}, convertido para dólar fica US$ {:.2f}'.format(v_real, v_real / 5))