# coding=utf-8
'''
Elabore um algoritmo que leia o valor de dois números inteiros e a operação aritmética desejada;
calcule, então, a resposta adequada. Utilize os símbolos da tabela a seguir para ler qual operação aritmética escolhida.
Símbolo Operação aritmética
+ Adição
- Subtração
* Multiplicação
/ Divisão
** Potenciação
'''

v_num1 = float(input('Digite o Primeiro Número .......: '))
print('|----------------------|')
print('| +  -> Adição         |')
print('| -  -> Subtração      |')
print('| *  -> Multiplicação  |')
print('| /  -> Divisão        |')
print('| ** -> Potenciação    |')
print('|----------------------|')
v_oper =       input('Digite o Operador Aritmético ...: ')
v_num2 = float(input('Difite o Segundo Número ........: '))



if v_oper == '+' :
    print('Operador Escolhido .: +  -> Adição ')
    print('Resultado Obitido ..: {:.2f}' .format(v_num1 + v_num2))
elif v_oper == '-' :
    print('Operador Escolhido .: -  -> Subtração  ')
    print('Resultado Obitido ..: {:.2f}' .format(v_num1 - v_num2))
elif v_oper == '*' :
    print('Operador Escolhido .: *  -> Multiplicação  ')
    print('Resultado Obitido ..: {:.2f}' .format(v_num1 * v_num2))
elif v_oper == '/' :
    print('Operador Escolhido .: /  -> Divisão  ')
    print('Resultado Obitido ..: {:.2f}' .format(v_num1 / v_num2))
elif v_oper == '**' :
    print('Operador Escolhido .: ** -> Potenciação')
    print('Resultado Obitido ..: {:.2f}' .format(v_num1 ** v_num2))
else : print('Operador Inválido')