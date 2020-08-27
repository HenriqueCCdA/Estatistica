from scipy.stats import norm
from normal import Norm as MyNorm

mu = 5.0
sig = 1.0

myNorm = MyNorm(mu, sig)

print('pdf\n')
for i in (-2,-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0):
    print(i,  myNorm.pdf(i), norm.pdf(i, mu, sig))

print('cdf num\n')
for i in (-2,-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0):
    print(i, myNorm.cdf_num(i), norm.cdf(i, mu, sig))

print('cdf erf\n')
for i in (-2,-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0):
    print(i, myNorm.cdf_erf(i), norm.cdf(i, mu, sig))

print('ppf\n')
print(myNorm.ppf(0.95), norm.ppf(0.95, mu, sig))
print(myNorm.ppf(0.15), norm.ppf(0.15, mu, sig))


