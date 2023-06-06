# coding=utf-8
'''
O IMC - Índice de Massa Corporal - é um critério da Organização Mundial da Saúde para indicar
a condição de peso de uma pessoa. A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o peso e a altura de
um adulto e mostre sua condição.

IMC em adultos              Condição
abaixo de 18,5              abaixo do peso
entre 18,5 e 25             peso normal
entre 25 e 30               acima do peso
acima de 30                 obeso
'''

peso   = float(input('Digite o seu Peso .....: ').replace(',', '.'))
altura = float(input('Digite o sua Altura ...: ').replace(',', '.'))

imc = peso / (altura**2)

if imc > 30 :
     print('Seu IMC e de ...: {:.2f}' .format(imc))
     print('Condição Atual .: Obseso')
elif imc > 25 and imc <= 30 :
     print('Seu IMC e de ...: {:.2f}'.format(imc))
     print('Condição Atual .: Acima do Peso')
elif imc >= 18.5 and imc <= 25 :
     print('Seu IMC e de ...: {:.2f}'.format(imc))
     print('Condição Atual .: Peso Normal')
else :
     print('Seu IMC e de ...: {:.2f}'.format(imc))
     print('Condição Atual .: Abaixo Normal')