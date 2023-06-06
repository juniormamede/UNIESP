'''
Situação Problema 6

A partir do ano de nascimento de uma pessoa mostrar sua idade, se já tem idade para votar (16 anos ou
mais) e se já pode ser candidato a uma carteira de habilitação.

Dados de entrada : ano de nascimento
Saída            : idade, idade para votar, idade para dirigir
'''

import datetime
from datetime import date

print('---- INICIANDO PROGRAMA IDADE/HABILITACAO ----')

data_nascimento = int(input('Digite sua Data de Nascimento : '))

ano_atual = date.today().year

idade = ano_atual - data_nascimento

if idade >= 18:
    print(f'Voce tem {idade} anos, ja pode VOTAR e DIRIGIR')
elif 15 < idade <18:
    print(f'Voce tem {idade} anos, ja pode VOTAR')
else:
    print(f'Voce tem {idade} anos, você ainda e muito novo')

print('---- FINALIZANDO PROGRAMA IDADE/HABILITACAO ----')