# coding=utf-8
'''
Exercicio 10
xercício do IMC (Índice de Massa Corporal): Escreva um programa em Python que solicite ao usuário sua altura em
metros e seu peso em quilogramas. Calcule o Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / (altura *
altura). Exiba o resultado do IMC na tela.
'''

peso =   float(input('Digite seu Peso   : ').replace(',', '.'))
altura = float(input('Digite sua Altura : ').replace(',', '.'))

imc = peso / (altura * altura )

#print(f'Seu IMC é : {imc:0.2f}')

print('Seu IMC : {}'.format(imc))
#\n -> Pular uma Linha
print('\nResposta 02 : Seu IMC : %.2f ' %imc)