'''
Precisamos de um programa de computador que calcule a quantidade de
latas de tinta e o custo total para pintar tanques cilíndricos de
combustível.

Sabemos que:
● A lata de tinta custa R$ 50,00
● Cada lata contém 5 litros
● Cada litro de tinta pinta 3 metros quadrados

SITUAÇÃO PROBLEMA 2 - Analisando a solução
● O custo = quantidade de latas * R$ 50,00
● A quantidade latas = a quantidade total de litros / 5
● A quantidade total de litros = área do cilindro / 3
● Área do cilindro = área da base + área lateral
● Área da base = PI * (R ** 2)
● Área lateral = (2 * PI * R * H)
● Sendo que R (raio) e H (altura) são dados de entrada e PI é uma constante de valor 3,14.
'''
import math

# VALOR DE PI
# EM CAIXA ALTA POR QUE E UMA CONSTANTE

PI = 3.14

'''
preco_lata_tinta = 50
litro_lata_tinta = 5
pinta_lata_tinta = 3
'''


altura = float(input('Digite a Altura do Cilindro .: '))
raio   = float(input('Digite o Raio do Cilindro ...: '))

area_lateral       = (2 * PI * raio * altura)
area_base          = PI * (raio ** 2)
area_cilintro      = area_base + area_lateral
quant_total_litros = area_cilintro / 3
quant_total_latas  = quant_total_litros / 5
custo              = quant_total_latas * 50.0

print(f'A Altura digitada foi ......: {altura}')
print(f'O Raio digitado foi ........: {raio}')
print(f'A Area Lateral foi .........: {area_lateral}')
print(f'A Area da Base foi .........: {area_base}')
print(f'A Area do Cilindo foi ......: {area_cilintro}')
print(f'Total de Litros Utilizada ..: {quant_total_litros}')
print(f'Total de Latas Utilizada ...: {math.ceil(quant_total_latas)}')
print(f'O Custo deste Projeto e de .: {custo}')