# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:05:28 2017

@author: singh
"""

import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500


grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height= 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stacked= True, color=['r','b'])
plt.xlabel('height')
plt.ylabel('number of dogs')
plt.show()

##Eye colour test
blue_eye = 1 +  1 * np.random.randn(greyhounds)
brown_eye = 1 + 1 * np.random.randn(labs)

plt.xlabel('blue eye colour')
plt.ylabel('number of dogs')
plt.hist([blue_eye ,brown_eye], stacked= True, color=['r','b'])
