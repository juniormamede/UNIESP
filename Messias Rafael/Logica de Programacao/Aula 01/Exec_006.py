# coding=utf-8

'''
Exercicio 06
Exercício do Cálculo de Área: Escreva um programa em Python que solicite ao usuário a largura e a altura de um
retângulo. Calcule a área desse retângulo e exiba o resultado.
'''


v_altura  = float(input('Digite a Altura do Retangulo : '))
v_largura = float(input('Digite a Largura do Retangulo : '))

area = v_altura * v_largura

print('A area do retangulo é {}' .format(area))