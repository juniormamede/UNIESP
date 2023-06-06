# coding=utf-8
v_depini      = float(raw_input('Digite o Depósito Inicial ......: '))
v_saque_input =       raw_input('Digite o Valor que Deseja Sacar : ')

if v_saque_input == '':
    v_saque = 0
else:
    v_saque = float(v_saque_input)

if v_saque > v_depini:
    print('Valor Depositado .: {:.2f}'.format(v_depini))
    print('Valor do Saque ...: {:.2f}'.format(v_saque))
    print('Saldo Final ......: -{:.2f}'.format(v_saque - v_depini))
    print('Sua conta está NEGATIVA em {:.2f}. Favor efetuar um depósito no valor de {:.2f} para manter sua conta ativa.'.format(v_saque - v_depini, (v_saque - v_depini)))
elif v_saque < v_depini:
    print('Valor Depositado .: {:.2f}'.format(v_depini))
    print('Valor do Saque ...: {:.2f}'.format(v_saque))
    print('Saldo Final ......: {:.2f}'.format(v_depini - v_saque))
else:
    print('Valor Depositado .: {:.2f}'.format(v_depini))
    print('Valor do Saque ...: {:.2f}'.format(v_saque))
    print('Saldo Final ......: 0.00')
