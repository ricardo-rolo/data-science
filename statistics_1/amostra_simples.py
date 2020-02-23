# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:40:46 2020

@author: ric10
"""

import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')
base

base.shape

np.random.seed(2345)
amostra = np.random.choice(a = [0,1], size = 150, replace = True, 
                           p = [0.5,0.5])

len(amostra)
len(amostra[amostra == 1])
len(amostra[amostra == 0])