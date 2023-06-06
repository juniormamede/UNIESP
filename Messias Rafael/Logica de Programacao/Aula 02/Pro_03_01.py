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

print('--- INICIANDO PROGRAMA IDADE II---')

data_nascimento = int(input('Digite sua Data de Nascimento : '))
ano_atual = date.today().year
idade = ano_atual - data_nascimento

print(idade)
if idade >= 18:

    print('Acesso Permitido')
    tipo_ingresso   = input('Digite a Senha do Ingresso (VIP) ou (PISTA): ')
    tipo_ingresso = tipo_ingresso.upper()

    if tipo_ingresso == 'VIP':
        print('Ingresso Validado com Sucesso')
        print('Siga para o Primeiro Andar!!!')
    elif tipo_ingresso == 'PISTA':
        print('Ingresso Validado com Sucesso')
        print('Siga pelo Corredor !!!')
    else:
        print('Ingresso Inválido!!!!')
else:
    print('Você não tem permissão')


print('--- FINALIZANDO PROGRAMA IDADE II---')