# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:05:35 2023

@author: Jose-de-Siqueira

Versão: 1.0 de 4/3/2024

Alguns exemplos de funções com e sem erros, para testar cada um dos aspectos
do corretor individual, como listado abaixo:

    1- Se uma função entrar em loop, para algum valor de teste, o corretor
       aponta o erro por tempo esgotado, ou por esgotamento de memória
       (stack overflow), sem deixar de corrigir a mesma função para outros
       valores de teste. Exemplo de uso da variável de configuração TIMEOUT.
       
       Os argumentos dos testes de funções simples, sem input e print, são
       coletados em uma lista em que os argumentos das funções são encapsula-
       dos em tuplas.

    2- Correção de função com entrada de dados via input e saída via print, 
       por simulação. Exemplo de uso da variável de configuração INPUT_PRINT.
       
       Os argumentos dos testes de funções com input e print são coletados em
       uma lista de tuplas com dois argumentos: o primeiro argumento é uma tu-
       pla que será passada como argumento da função a ser testada; o segundo
       argumento é uma lista com valores para simular a entrada do comando
       input. Os prints da execução são coletados pelo corretor e comparados
       com os prints do gabarito.
       
    3- Correção por verificação de id de parâmetro de entrada e saída. Exemplo
       de uso da variável de configuração ESPECIAL.
       
    4- Correção de função com retorno de float com arrendondamento definido
       pelo usuário. Exemplo de uso da variável de configuração ARREDONDAMENTO.
    5- Correção de função com manipulação de dicionários.
    
Estado:
    19/2/2024
    Geração de intervalos aleatórios funcionando. Utilizar variáveis dinâmicas
    para gerar os intervalos a partir da lista de nomes de testes, TESTES_EXES
    com uso de exec: 
    exec(f'{teste_x_y_z} = gia.gerador_de_intervalos_aleatorios(intervalo)[0]')
    7/2/2024
    Importa Intervalos.gerador_de_intervalos_aleatorios para gerar os testes.
    Início dos testes de geração.
    
    29/8/2023
    Desenvolvimento do corretor com input e print.
    
    16/8/2023
    1- Exemplos de correção de funções que entram em loop para diferentes ar-
       gumentos, mas não impedem a correção para outros argumentos 
       (funções 1.1 a 1.4).
       
"""

import Intervalos.gerador_de_intervalos_aleatorios as gia
# função que gera listas de listas com intervalos aleatórios para testes

def exercicio_1_1(n):
    """
    Cálculo do fatorial de n recursivo, sem erros.

    Parameters
    ----------
    n : int
        Valor para o qual se quer calcular o fatorial.

    Returns
    -------
    Retorna None se n < 0 e int para n >= 0.

    """
    
    if n < 0:
        res = None
    elif n == 0:
        res = 1
    else:
        res = n * exercicio_1_1(n-1)
    return res

def exercicio_1_2(n):
    """
    Cálculo do fatorial de n iterativo, sem erros.

    Parameters
    ----------
    n : int
        Valor para o qual se quer calcular o fatorial..

    Returns
    -------
    Retorna None se n < 0 e int para n >= 0.

    """
    
    if n < 0:
        res = None
    else:
        res = 1 
        while n > 0:
            res *= n
            n -= 1
    return res

def exercicio_1_3(n):
    """
    Versão recursiva que entra em loop porque falta a cláusula de base (n == 0).
    Parameters
    ----------
    Parameters
    ----------
    n : int
        Valor para o qual se quer calcular o fatorial..

    Returns
    -------
    Retorna None se n < 0 e int para n >= 0.
    """
    
    if n < 0:
        res = None
    # elif n == 0:
    #   res = 1
    else:
        res = n * exercicio_1_3(n-1)
    return res

def exercicio_1_4(n):
    """
    Versão iterativa que entra em loop por timeout para qualquer valor de <n>

    Parameters
    ----------
    n : int
        Valor para o qual se quer calcular o fatorial..

    Returns
    -------
    Retorna None se n < 0 e int para n >= 0.
    """
    
    if n < 0:
        res = None
    else:
        res = 1 
        while n > 0:
            res *= n
            # n -= 1
    return res

# Intervalos a serem gerados com as indicações passadas na lista abaixo:

intervalos_recursivos = [1,[-12,-2],[0,0,0],10, [1,100,10], 4, [100,900,100]]

intervalos_iterativos = [1,[-12,-2],[0,0,0],10, [1,100,10], 2, [100,1000,900], 2, [1000,3000,1000]]

# A cada execução de funções_exercicios (este arquivo), novos valores de teste
# são gerados aleatoriamente pela função abaixo:

teste_1_1 = gia.gerador_de_intervalos_aleatorios(intervalos_recursivos)[0]

teste_1_2 = gia.gerador_de_intervalos_aleatorios(intervalos_iterativos)[0]

teste_1_3 = gia.gerador_de_intervalos_aleatorios(intervalos_recursivos)[0]

teste_1_4 = gia.gerador_de_intervalos_aleatorios(intervalos_iterativos)[0]

def exercicio_2_1(sentinela,ordem):
    """
    Versão recursiva de leitura de dados com sentinela. Retorna a quantidade 
    de dados lidos e a soma dos valores. Imprime os dados na ordem em que
    foram entrados. Sem erros.
    
    Parameters
    ----------
    sentinela: int
        Valor para parar a entrada de dados.

    ordem: int
        Ordem de entrada dos dados para impressão. Deve ser 0 na chamada da
        função.
    
    Returns
    -------
    (quantidade,soma): (int,int).

    """
    
    valor = int(input(f'Entre com o {ordem}o. valor: '))
    print(f'Quantidade: {ordem} Valor: {valor}')

    if valor == sentinela:
        soma = 0 # acabaram-se os dados
        quantidade = ordem
    else:
        quantidade,soma = exercicio_2_1(sentinela,ordem+1)
        soma = soma+valor
    return quantidade,soma

# Os argumentos dos testes tem que ser tupla!
teste_2_1 = [((-1,0),[1,2,3,-1]),((-2,0),[-2]),((-3,0),[-3,1,2,0])]
#teste_2_1 = [((-1,0),[-1]),((-1,0),[1,2,3,4,-1]),((0,0),[-1,1,2,3,4,5,6,0])]

#teste_2_1 = [(-1,0),(-2,0),(-3,0)]
#for arg in teste_2_1:
#    print(f'arg: {arg} res: {exercicio_2_1(*arg)}')
