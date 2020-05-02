import numpy as np

def histograma_v1(x, bins=10, density=False):
    '''
    ********************************************************************
    Data de Criacao     : 02/05/2020
    Data de modificacao : 00/00/0000
    --------------------------------------------------------------------
    histogtama_v2 : calcula o histograma de x
    --------------------------------------------------------------------
    Paramentros
    --------------------------------------------------------------------
    x:  valores
    bins: numero de divisoes dos valores x
    density:  normaliza os valores hist (default=False)
    --------------------------------------------------------------------
    Retorno
    --------------------------------------------------------------------
    hist: histograma
    bins_edge:
    --------------------------------------------------------------------
    OBS: utiliza listas
    ********************************************************************
    '''
    x_min=min(x)
    x_max=max(x)
    n_x = len(x)
    dx = (x_max - x_min)/bins

    bins_edge = [float(x_min)]
    for i in range(0,bins-1):
        x_new = bins_edge[i] + dx
        bins_edge.append(x_new)
    bins_edge.append(float(x_max))

    hist  = []
    j     = 0
    count = 0
    for i in range(bins):
        x_inf = bins_edge[i]
        x_sup = bins_edge[i+1]
        count = 0
        # no ultimo intervalo [x_inf,x_sup]
        if(i == bins - 1):
            for k in range(j, n_x):
                if(x_inf <= x[k] <= x_sup):
                    count+=1
        # nos outros [x_inf,x_sup)
        else:
            for k in range(j, n_x):
                if(x_inf <= x[k] < x_sup):
                    j+=1
                    count+=1
                else:
                    break

        hist.append(count)

    # ... normaliza o hist atraves alfa = h1*b1
    #                                   + h2*b2 + ... + hn*bn
    if(density):
        alfa = 0.e0
        for i in range(len(hist)):
            alfa += hist[i] * (bins_edge[i+1] - bins_edge[i])

        for i in range(len(hist)):
            hist[i] = hist[i]/alfa

    return hist, bins_edge

def histograma_v2(x, bins=10, density=False):
    '''
    ********************************************************************
    Data de Criacao     : 02/05/2020
    Data de modificacao : 00/00/0000
    --------------------------------------------------------------------
    histogtama_v2 : calcula o histograma de x
    --------------------------------------------------------------------
    Paramentros
    --------------------------------------------------------------------
    x:  valores
    bins: numero de divisoes dos valores x
    density:  normaliza os valores hist (default=False)
    --------------------------------------------------------------------
    Retorno
    --------------------------------------------------------------------
    hist: histograma
    bins_edge:
    --------------------------------------------------------------------
    OBS: utiliza arranjos numpy
    ********************************************************************
    '''
    x_min=min(x)
    x_max=max(x)
    n_x = len(x)
    dx = (x_max - x_min)/bins

    bins_edge = np.empty(bins+1,dtype=float)
    hist      = np.empty(bins  ,dtype=float)

    bins_edge[0] = float(x_min)

    for i in range(0,bins-1):
        x_new = bins_edge[i] + dx
        bins_edge[i+1] = x_new

    bins_edge[-1] = float(x_max)

    j     = 0
    count = 0
    for i in range(bins):
        x_inf = bins_edge[i]
        x_sup = bins_edge[i+1]
        count = 0
        # no ultimo intervalo [x_inf,x_sup]
        if(i == bins - 1):
            for k in range(j, n_x):
                if(x_inf <= x[k] <= x_sup):
                    count+=1
        # nos outros [x_inf,x_sup)
        else:
            for k in range(j, n_x):
                if(x_inf <= x[k] < x_sup):
                    j+=1
                    count+=1
                else:
                    break

        hist[i] = count

    # ... normaliza o hist atraves alfa = h1*b1
    #                                   + h2*b2 + ... + hn*bn
    if(density):
        alfa = (hist * np.diff(bins_edge)).sum()

        hist = hist/alfa

    return hist, bins_edge