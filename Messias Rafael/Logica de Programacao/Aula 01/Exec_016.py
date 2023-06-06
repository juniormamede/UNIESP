# coding=utf-8
'''
Nossa equipe de desenvolvimento ficou responsável por desenvolver um programa que gerencie uma lista de convidados
para uma festa. É preciso criar uma mensagem padrão, e uma lista de convidados. Você pode escolher três personagens de
filmes para adicionar a sua lista de convidados.

a. Sabendo que um dos seus convidados não pode participar, adicione ao programa uma mensagem informando que
ele será retirado da lista, e altere o código para receber um novo personagem. Não esqueça de utilizar as funções
que te permite adicionar os novos convidados pelo teclado.

b. Adicione a opção de poder adicionar mais pessoas à sua lista.
i. Uma opção para adicionar um convidado querido ao início da lista;
ii. Uma convidado no meio da lista;
iii. E por um convidado ao fim da lista;
'''
'''
Adicionando Elementos da Lista
Index        0    1    2    3
lista      [ 1.2, 2.1, 3.1, 4.1  ] 
Elementos    1ª   2ª   3ª   4ª

-> Inset Insere o Elemente no indice informado
nome_da_lista.insert(indice,elemento)
-> Inset Insere o Elemente no final da lista
nome_da_lista.append(elemento)
'''


lista = []

while True:
    v_convidaddos = input('Digite os Nomes dos Convidados : ')
    lista.append(v_convidaddos)


#print(v_convidaddos)


