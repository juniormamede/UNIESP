'''
28. [FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), sendo
que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raízes reais).

Com import math
import math

# Input dos valores de A, B e C
v_valora = float(input("Digite o Valor de A: "))
v_valorb = float(input("Digite o Valor de B: "))
v_valorc = float(input("Digite o Valor de C: "))

# Calcula o discriminante (Delta)
v_delta = v_valorb**2 - 4 * v_valora * v_valorc

# Verifica o valor de delta
if v_delta > 0:
    # Duas raízes reais distintas
    v_valorx1 = (-v_valorb + math.sqrt(v_delta)) / (2 * v_valora)
    v_valorx2 = (-v_valorb - math.sqrt(v_delta)) / (2 * v_valora)
    print("A equação possui duas raízes reais distintas:")
    print("x1 =", v_valorx1)
    print("x2 =", v_valorx2)
elif v_delta == 0:
    # Uma raiz real (repetida)
    v_valorx = -v_valorb / (2 * v_valora)
    print("A equação possui uma raiz real (repetida):")
    print("x =", v_valorx)
else:
    # Sem raízes reais (raízes complexas)
    parte_real = -v_valorb / (2 * v_valora)
    parte_imaginaria = math.sqrt(-v_delta) / (2 * v_valora)
    print("A equação possui duas raízes complexas:")
    print("x1 =", parte_real, "+", parte_imaginaria, "i")
    print("x2 =", parte_real, "-", parte_imaginaria, "i")


'''
# strip() -> serve para remover os espaços em branco no início e no final de uma string,
# retornando uma cópia formatada da string sem os espaços em branco do ínicio e final.
v_valora = None
while v_valora is None or v_valora == 0:
    valor_input = input('Digite o Valor de A: ')
    if valor_input.strip() != '':
        v_valora = float(valor_input)

v_valorb = None
while v_valorb is None or v_valorb == 0:
    valor_input = input('Digite o Valor de B: ')
    if valor_input.strip() != '':
        v_valorb = float(valor_input)

v_valorc = None
while v_valorc is None or v_valorc == 0:
    valor_input = input('Digite o Valor de C: ')
    if valor_input.strip() != '':
        v_valorc = float(valor_input)


# D = b^2 - 4ac
v_delta = v_valorb**2 - 4 * v_valora * v_valorc
print('O Valor de Delta : {:.2f}' .format(v_delta))

# Valor de X' (Soma)
# x'  = (-b - RaizQuadrada(Delta)) / (2a)
# Valor de X'' (Subtrai)
# x'' = (-b + RaizQuadrada(Delta)) / (2a)

'''
A =  1
B = -6
C =  9
Delta = 0 (ZERO)
'''

if v_delta == 0 :
    v_deltazero = -v_valorb / ( 2 * v_valora )
    print('O valor de X\' e igual ao de x\" : {:.2f}' .format(v_deltazero) )

elif v_delta > 0 :
    v_valorx1 = (-v_valorb + v_delta ** 0.5) / (2 * v_valora)
    v_valorx2 = (-v_valorb - v_delta ** 0.5) / (2 * v_valora)
    print('Valor de X\' : {:.2f}' .format(v_valorx1))
    print('Valor de X\" : {:.2f}' .format(v_valorx2))
else :
    '''Nao existe Raiz Quadra de Numero Negatigo
       RaizQuadrada ( -4 ) = 2i
       Sendo i parte imaginaria 
    '''
    v_valorx = -v_valorb / (2 * v_valora)
    v_valori = (-v_delta) ** 0.5 / (2 * v_valora)
    print("x1 =", v_valorx, "+", v_valori, "i")
    print("x2 =", v_valorx, "-", v_valori, "i")