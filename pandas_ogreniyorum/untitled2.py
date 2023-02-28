# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 10:16:14 2023

@author: iecet
"""

import pandas as pd
import numpy as np

r = np.random.randint(200, size = 30)

lb = 30
ub = 70

filter_l = r < lb
filter_u = r > ub
filter = (r < lb) | (r > ub)

l = r[filter_l]
u = r[filter_u]
t = r[filter]


