from scipy.stats import spearmanr, pearsonr, rankdata
from Correlacao.correlacao import corr, posto

x = [2.1, 2.01, 0.5, 3.6, 3.6, 3.6, 3.6, 3.6]
y = [2.3, 3.3 ,-0.3, 5.5, 5.5, 4.3, 3.4, -2.0]

print('')
print(f'x = {x}')
print(f'posto(x) = {posto(x)}')
print(f'scipy rank(x) = {rankdata(x)}')

print('')
print(f'y = {y}')
print(f'posto(y) = {posto(y)}')
print(f'scipy rank(y) = {rankdata(y)}')


rho1 = corr(x, y, method = 'spearman')
rho2, _ = spearmanr(x,y)
print('')
print(f'rho       = {rho1}')
print(f'scipy rho = {rho2}')


rho1 = corr(x, y, method = 'pearson')
rho2, _ = pearsonr(x,y)

print('')
print(f'rho       = {rho1}')
print(f'scipy rho = {rho2}')
