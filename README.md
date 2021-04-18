# Estatística

Repositório criado para guarda alguns códigos de calculos estatisticos. O repositório é apenas para fins de estudo pessoal, nenhum código aqui visa ser
eficiente computacionalmente.

## Biblioteca em C

O arquivo fonte Estatistica_lib.c possui o código de algums cálculos estáticos simples ( media, desvio padrão, ...). O objetivo deste código é ser compilado com uma lib dinâmica para ser chamada posteriormente pelo python. Para chamar a lib foi utilizado o ctypes, a interface esta definida no arquivo estat_hcca.py.
O /Test/Teste_Estatistica_Lib.py possui exemplos de como utilizar esse módulo.

## Histograma

No arquivo histograma.py há a implementa de funcões que calculam histograma. Duas versão são implementadas
. A versão 1 utiliza apenas o python puro. Já a versão 2 utiliza arrays NumPy. No arquivo /Test/Teste_Hitograma.py
são executados os testes da implementação da versão 1 e 2 com o histogam do NumPy.

## Correlação

No arquivo correlacção.py há uma implementação do calculo do número de Spearman e Pearson. A implementaçã utiliza apenas o python vanila. No mesmo 
arquivo também exista uma função que calculo do posto (rank) de um vetor.

## Função normal

No arquivo normal.py há uma implementa de alguns cálculos importantes de distribuição normal. Por exemplo, calculo do parametro z, da pdf e cdf. 
