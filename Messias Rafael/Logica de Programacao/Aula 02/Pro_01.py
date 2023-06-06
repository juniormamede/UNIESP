'''
Construir um algoritmo que calcule a média aritmética entre
quatro notas bimestrais fornecidas por um aluno (usuário).

Dados de entrada: quatro notas (n1, n2, n3, n4)
Dados de saída: média aritmética anual (ma)
'''


nota1 = None
while nota1 is None:
      v_nota1 = input('Digite a Primeira Nota  : ')
      try:
         nota1 = float((v_nota1).replace(',', '.'))
      except ValueError:
         print('Valor Inválido, digite novamente!')

nota2 = None
while nota2 is None:
      v_nota2 = input('Digite a Segunda Nota   : ')
      try:
          nota2 = float((v_nota2).replace(',','.'))
      except ValueError:
          print('Valor Inválido, digite novamente!')

nota3 = None
while nota3 is None:
      v_nota3 = input('Digite a Terceira Nota  : ')
      try:
          nota3 = float((v_nota3).replace(',','.'))
      except ValueError:
          print('Valor Inválido, digite novamente!')

nota4 = None
while nota4 is None:
      v_nota4 = input('Digite a Quarta Nota    : ')
      try:
          nota4 = float((v_nota4).replace(',','.'))
      except ValueError:
          print('Valor Inválido, digite novamente!')

ma = ( nota1 + nota2 + nota3 + nota4) / 4

'''print(f'Sua Média Foi : {ma}' )'''

if ma >= 8.0 :
   print(f'Sua Media Foi : {ma}')
   print('Você esta de PARABENS')
elif  ma >= 6.0 and ma < 8.0 :
   print(f'Sua Média foi {ma}')
   print('Voce Esta com Notas Regulares, continue estudando')
else:
   print(f'Sua Média Foi : {ma}')
   print('Você precisa melhorar !!!')