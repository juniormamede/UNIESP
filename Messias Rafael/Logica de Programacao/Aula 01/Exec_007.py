# coding=utf-8
'''
Exercicio 07
Exercício do Tempo de Viagem: Escreva um programa em Python que solicite ao usuário a distância de uma viagem (em
km) e a velocidade média (em km/h). Calcule o tempo de viagem em horas e exiba o resultado.
'''

v_distancia = float(input('Digite a Distância Percorrida em KM :'))
v_velomedia = float(input('Digite a Velocidade Média : '))

v_tempoviagem = v_distancia / v_velomedia

# Tempo em Horas
c_media_horas = int(v_tempoviagem)
# Tempo em Minutos
c_media_minutos = int((v_tempoviagem - c_media_horas) * 60 )

print('A distância percorrida foi de {} km em uma velocidade média de {} km/h' .format(v_distancia, v_velomedia) )
print('Esta viagem demorou {} hora(s) e {} minutos'.format( c_media_horas, c_media_minutos))