import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from LancamentoMoedas import LancamentoMoedas

n_lancamentos = 25
p_vitoria     = 0.3

# ... gerando os experimentos
moeda = LancamentoMoedas(n_lancamentos, p_vitoria)

X = []
P = []

# ... lancamentos
for i in range(0, n_lancamentos + 1):
    a = moeda.probabilidade(i)
    print(f'P(X = {i}) = {a}')
    X.append(i)
    P.append(a)

# plotando a distribuicao de probabilidade
df = pd.DataFrame({'X' : X, 'P': P})
sns.barplot(x ='X', y = 'P', data = df, palette=sns.color_palette("husl", 1))
plt.show()

