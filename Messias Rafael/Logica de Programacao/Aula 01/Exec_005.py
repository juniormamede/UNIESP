# coding=utf-8
'''
Ecercico 05
Exercício da Conversão de Temperatura: Escreva um programa em Python que solicite ao usuário uma temperatura em
graus Celsius e faça a conversão para Fahrenheit. Exiba o resultado na tela
'''

temp_celsius = float(raw_input('Digite a Temperatura em Celsius: '))


v_fah = ((temp_celsius * 9/5) + 32 )
v_kel =  (temp_celsius + 273.15 )

v_conversao = raw_input("Digite o fator de Conversao [F - Fahrenheit / K - Kelvin]: ").lower()

if v_conversao == 'f':
   print('A temperatura em Fahrenheit: {}'.format(v_fah))
elif v_conversao == 'k':
   print('A temperatura em Kelvin: {}'.format(v_kel))
else:
   print('Você não digitou corretamente.')
