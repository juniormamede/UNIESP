# coding=utf-8
'''
Exercicio 09
Exercício do Volume de uma Esfera: Escreva um programa em Python que solicite ao usuário o raio de uma esfera.
Calcule o volume dessa esfera usando a fórmula V = (4/3) * pi * r³, onde pi é uma constante aproximada de 3.1415. Exiba
o volume calculado na tela.
'''

raio = float(input("Digite o Valor do Raio = "))
pi = 3.1415

volume = (4 / 3) * pi * (raio ** 3)

#print \n -> Pular uma Linha
print("\nO Volume da Esfera  = %.2f m³" %volume)