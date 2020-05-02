import numpy as np
import Estatistica.estat_hcca as est

lib = est.Estatistica()

a = [1.7, 1.4, 1.6, 1.5, 5.0]

media = lib.media(a)

var = lib.var(a, ddof=0)

std = lib.std(a,ddof=0)

print(media, var, std)
print(np.mean(a), np.var(a), np.std(a))

mediana = lib.mediana(a)
print(mediana)
print(np.median(a))

