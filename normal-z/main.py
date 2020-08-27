from scipy.stats import norm
from normal import Norm as MyNorm

mu = 5.0
sig = 0.5

myNorm = MyNorm(mu, sig)

print('pdf')
print("______________________________________")
print(f"|  x   |      My      |     scipy    |")
print("______________________________________")
for i in (-2,-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0):
    x = i + mu
    print(f"| {x:4.1f} | {myNorm.pdf(x):.6e} | {norm.pdf(x, mu, sig):.6e} |")
print("______________________________________")

print('\ncdf num')
print("______________________________________")
print(f"|  x   |      My      |     scipy    |")
print("______________________________________")
for i in (-2,-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0):
    x = i + mu
    print(f"| {x:4.1f} | {myNorm.cdf_num(x):.6e} | {norm.cdf(x, mu, sig):.6e} |")
print("______________________________________")

print('\ncdf erf')
print("______________________________________")
print(f"|  x   |      My      |     scipy    |")
print("______________________________________")
for i in (-2,-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0):
    x = i + mu
    print(f"| {x:4.1f} | {myNorm.cdf_erf(x):.6e} | {norm.cdf(x, mu, sig):.6e} |")
print("______________________________________")

print('\nppf')
print("______________________________________")
print(f"|  P   |      My      |     scipy    |")
print("______________________________________")
for i in (0.15, 0.95):
    print(f"| {i:4.2f} | {myNorm.ppf(i):12.2f} | {norm.ppf(i, mu, sig):12.2f} |")
print("______________________________________")


