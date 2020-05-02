import histograma as hs
import numpy as np

def test(x1, x2):
  print('Test: ')
  hist_diff = np.abs(x1 - x2).sum()
  if(hist_diff < TOL):
    print(f'OK!\nDiff = {hist_diff:.2e}\n')
  else:
    print(f'FAIL!\nDiff = {hist_diff:.2e}\n')
    exit(-1)

TOL = 1.e-14

a = np.arange(20)

hist_v1, bins_v1 = hs.histograma_v1(a, bins=10, density=False)
hist_v2, bins_v2 = hs.histograma_v2(a, bins=10, density=False)
hist_np, bins_np = np.histogram(a, bins=10, density=False)

print('Teste do histograma (density=False):')

print('V1 - hist:')
test(hist_v1, hist_np)
print('V1 - bins:')
test(bins_v1, bins_np)

print('V2 - hist:')
test(hist_v2, hist_np)
print('V2 - bins:')
test(bins_v2, bins_np)

hist_v1, bins_v1 = hs.histograma_v1(a, bins=10, density=True)
hist_v2, bins_v2 = hs.histograma_v2(a, bins=10, density=True)
hist_np, bins_np = np.histogram(a, bins=10, density=True)

print('Teste do histograma (density=True):')

print('V2 - hist:')
test(hist_v1, hist_np)
print('V2 - bins:')
test(bins_v1, bins_np)

print('V2 - hist:')
test(hist_v2, hist_np)
print('V2 - bins:')
test(bins_v2, bins_np)
