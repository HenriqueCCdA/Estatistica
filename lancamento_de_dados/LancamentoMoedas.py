class LancamentoMoedas():

    def __init__(self, n_lancamentos: int, prob_moeda: float = 0.5):
        self.__n: int = n_lancamentos
        self.__p: float = prob_moeda

    def combinacao(self, k: int) -> int:

        n = self.__n

        if n < k:
            raise Exception(f'{k} não pode ser maior que {n} !')
        if n == k:
            return 1

        num = 1
        for i in range(n - k + 1, n + 1):
            num *= i

        dem = 1
        for i in range(2, k + 1):
            dem *= i

        return int(num / dem)

    def probabilidade(self, x: int) -> float:

        k: int = x
        n: int = self.__n

        # ... total de combinacoes desejadas Cn,k
        total_comb = self.combinacao(x)
        # ...
        e1: int = k
        e2: int = n - k
        p: float = self.__p
        # ...
        prob: float = total_comb * (p ** e1) * ((1.0 - p) ** e2)

        return prob
