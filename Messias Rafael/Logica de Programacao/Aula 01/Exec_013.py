# coding=utf-8
'''
Gerenciar um estoque para a empresa U não é complicado, mas ele te pediu para desenvolver um programa para realizar
esta tarefa.

Ela precisa que o usuário informe a quantidade máxima e mínima do estoque do produto X, e também a
quantidade real existente no estoque.

Por fim, o programa deve responder se é necessário adquirir mais produtos,
comparando o estoque real com a média entre valor máximo e mínimo.

a. se o estoque real estiver abaixo da média, informar a necessidade de compra;
b. se estiver acima da média informar que não precisa adquirir novos produtos;
c. se estiver na média, informa que em breve será necessária nova aquisição de produtos;
'''

v_qtmax         = float(raw_input('Digite a Quantidade Maxima .: '))
v_qtmin         = float(raw_input('Digite a Quantidade Minima .: '))
v_estoque_atual = float(raw_input('Digite o Estoque Atual .....: '))

v_media_est = ( v_qtmax + v_qtmin ) / 2

if v_estoque_atual < v_media_est :
   print('Estoque Atual ......: {:.2f}' .format(v_estoque_atual))
   print('Giro de Mercadoria .: {:.2f}' .format(v_media_est))
   print('Sugestão de compra em {:.2f} unidades' .format(v_media_est - v_estoque_atual ))
elif v_estoque_atual > v_media_est :
   print('Estoque Atual ......: {:.2f}' .format(v_estoque_atual))
   print('Giro de Mercadoria .: {:.2f}' .format(v_media_est))
   print('Com base em nosso giro, ainda temos saldo de mercadoria em {:.2f} unidades' .format( v_estoque_atual - v_media_est))
else :
   print('Estoque Atual ......: {:.2f}' .format(v_estoque_atual))
   print('Giro de Mercadoria .: {:.2f}' .format(v_media_est))
   print('Com base em nosso giro, temos {:.2f} unidades, logo não precisamos comprar mercadorias' .format( v_estoque_atual))