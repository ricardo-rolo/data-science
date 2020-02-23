# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:07:34 2020

@author: ric10
"""

import pandas as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')

#contagem de ocorrências por 'class'
iris['class'].value_counts()

#separando os grupos de acordo com suas respectivas representatividades
x, _, y, _ = train_test_split(iris.iloc[:,0:4], iris.iloc[:, 4],
                              test_size = 0.5, stratify = iris.iloc[:,4])
y.value_counts()

infert = pd.read_csv('infert.csv')

#contagem de ocorrências por 'education'
infert['education'].value_counts()

#separando os grupos de acordo com suas respectivas representatitivades
x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1],
                                test_size = 0.6, stratify = infert.iloc[:, 1])
y1.value_counts()