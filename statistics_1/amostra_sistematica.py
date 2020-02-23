# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:28:15 2020

@author: ric10
"""

import numpy as np
import pandas as pd
from math import ceil

populacao = 150
amostra = 15
k= populacao / amostra #incremento

#sorteio do primeiro número
r = np.random.randint(low = 1, high = k + 1, size = 1)

#alocando primeiro número no tipo inteiro
acumulador = r[0]

#lista de números sorteados (ainda vazia)
sorteados = []

#preparando lista de sorteados
for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k

base = pd.read_csv('iris.csv')

#selecionando os valores sorteados na base de dados
base_final = base.loc[sorteados]