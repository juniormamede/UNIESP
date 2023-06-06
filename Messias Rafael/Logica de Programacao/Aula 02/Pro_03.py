'''
Um programa que verifique se existe permissão, a partir da idade, para entrar em uma festa.

https://www.tabnews.com.br/PeduCosta/como-pegar-data-atual-em-python-formatada-no-padrao-brasileiro-considerando-os-zeros

'''
import datetime
from datetime import date
# para importar toda a biblioteca
# import datetime as dt # substituindo o nome datetime por dt dentro do código
# from datetime import date # quando se quer apenas 1 dos submódulos
# data = date.today()  # ANO ATUAL
# print(data)          # ANO ATUAL

print('--- INICIANDO PROGRAMA IDADE ---')

data_nascimento = int(input('Digite sua Data de Nascimento : '))
tipo_ingresso   = input('Digite a Senha do Ingresso (VIP) ou (PISTA): ')
tipo_ingresso   = tipo_ingresso.upper()

ano_atual = date.today().year
idade = ano_atual - data_nascimento

if  18 =< idade < 100 and tipo_ingresso == 'VIP':
    print('Acesso Permitido')
    print('Ingresso Validado com Sucesso')
    print('Siga para o Primeiro Andar!!!')
elif idade >= 18 and tipo_ingresso == 'PISTA':
    print('Acesso Permitido')
    print('Ingresso Validado com Sucesso')
    print('Siga pelo Corredor !!!')
else:
    print('VOCÊ NAO TEM PERMISSÃO')
