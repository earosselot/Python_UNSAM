# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 19:50:28 2021

@author: Eduardo
"""

# %% Ejercicio 5.8
# Empezando a plotear

import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load('../Data/Temperaturas.npy')
plt.hist(temperaturas, bins=32)
