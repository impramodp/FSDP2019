# -*- coding: utf-8 -*-

import numpy as np
list1=[13, 18, 13, 14, 13, 16, 14, 21, 13]
x=np.array(list1)
print("mean: ",np.mean(x))
print("meadian: ",np.median(x))
print("mode: :",np.bincount(x).argmax())
p=x.max()
q=x.min()
r=p-q
print("range: ",r)