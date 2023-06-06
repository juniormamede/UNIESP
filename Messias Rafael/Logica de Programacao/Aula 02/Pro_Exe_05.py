'''
Um programa que permita saber qual o peso ideal de uma pessoa.
● Para homens: (72,7 * h) - 58
● Para mulheres: (62,1 * h) - 44,7

Dados de entrada: altura e sexo de uma pessoa.
'''

sexo_mf = input('Digite seu Genero : ').upper()

if sexo_mf == 'M':
    altura = None
    while altura is None:
      v_altura = input('Digite sua Altura : ')
      try:
          altura = float((v_altura).replace(',','.'))
      except ValueError:
          print('Voce Digitou a Altura Errada!!!')
    p_ideal = (72.7 * altura) - 58
    print(f'Seu Peso Ideal é : {p_ideal}')
elif sexo_mf == 'F':
    altura = None
    while altura is None:
      v_altura = input('Digite sua Altura : ')
      try:
          altura = float((v_altura).replace(',','.'))
      except ValueError:
          print('Voce Digitou a Altura Errada!!!')
    p_ideal = (62.1 * altura) - 58
    print(f'Seu Peso Ideal é : {p_ideal}')
else:
    print('Genero Incorreto')