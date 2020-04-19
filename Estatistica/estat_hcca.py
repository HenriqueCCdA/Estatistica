import ctypes as ct

class Estatistica():

    def __init__(self, path_lib = './C/Estatistica.dll'):
        self.__lib = ct.cdll.LoadLibrary(path_lib)
        # parametros da funcao media
        self.__lib.media.argtypes = [ct.POINTER(ct.c_double), ct.c_int]
        self.__lib.media.restype = ct.c_double
        # parametros da funcao variancia
        self.__lib.var.argtypes = [ct.POINTER(ct.c_double),
                                   ct.c_int,
                                   ct.c_int]
        self.__lib.var.restype = ct.c_double
        # parametros da funcao desviao padrao
        self.__lib.std.argtypes = [ct.POINTER(ct.c_double),
                                   ct.c_int,
                                   ct.c_int]
        self.__lib.std.restype = ct.c_double
        # parametros da mediana
        self.__lib.mediana.argtypes = [ct.POINTER(ct.c_double),
                                       ct.c_int,
                                       ct.c_short]
        self.__lib.mediana.restype = ct.c_double

    def media(self, a):
        '''
        ****************************************************************
        data de criacao  : 17/04/2020
        data de modificao: 00/00/0000
        ----------------------------------------------------------------
        Media : Cacula a media de a
        ----------------------------------------------------------------
        paremetros de enrada:
        a -> valores
        ----------------------------------------------------------------
        retorno: a media de de a calculada
        ----------------------------------------------------------------
        ****************************************************************
        '''
        n = len(a)        
        a_c = (ct.c_double * n) (*a)
        res = self.__lib.media(a_c, n)        
        return res        
    
    def var(self, a, ddof = 1):
        '''
        ****************************************************************
        data de criacao  : 17/04/2020
        data de modificao: 00/00/0000
        ----------------------------------------------------------------
        Var : Cacula a variancia de a
        ----------------------------------------------------------------
        paremetros de enrada:
        a    -> valores
        ddof -> graus de liberdade
        ----------------------------------------------------------------
        retorno: variania de de a calculada
        ----------------------------------------------------------------
        OBS:
        ----------------------------------------------------------------
        ddof = 0 : variancia populacional
        ddof = 1 : variancia amostral
        ****************************************************************
        '''

        n         = len(a)        
        
        # ... convertendo para o formato ctypes
        n_c       = ct.c_int(n)
        a_c       = (ct.c_double * n) (*a)
        ddof_c = ct.c_int(ddof)
        # ... chamando a funcao
        res = self.__lib.var(a_c, n_c, ddof_c)

        return res 
    
    
    def std(self, a, ddof = 1):
        '''
        ****************************************************************
        data de criacao  : 17/04/2020
        data de modificao: 00/00/0000
        ----------------------------------------------------------------
        std : Cacula o desvio padrao  de a
        ----------------------------------------------------------------
        paremetros de enrada:
        a    -> valores
        ddof -> graus de liberdade
        ----------------------------------------------------------------
        retorno: variania de de a calculada
        ----------------------------------------------------------------
        OBS:
        ddof = 0 : desvio padrao populacional
        ddof = 1 : desvio padrao amostral
        ****************************************************************
        '''

        n         = len(a)
        # ... convertendo para o formato ctypes
        n_c       = ct.c_int(n)
        a_c       = (ct.c_double * n) (*a)
        ddof_c = ct.c_int(ddof)
        # ... chamando a funcao
        res = self.__lib.std(a_c, n_c, ddof_c)

        return res

    def mediana(self, a, cod=1):
        '''
        ****************************************************************
        data de criacao  : 17/04/2020
        data de modificao: 00/00/0000
        ----------------------------------------------------------------
        std : Cacula o desvio padrao  de a
        ----------------------------------------------------------------
        paremetros de enrada:
        a    -> valores
        cod  -> algoritimo de ordenacao escolhido
        ----------------------------------------------------------------
        retorno: variania de de a calculada
        ----------------------------------------------------------------
        OBS:
        cod = 1 : bubblesort
        ****************************************************************
        '''

        n         = len(a)
        # ... convertendo para o formato ctypes
        n_c       = ct.c_int(n)
        a_c       = (ct.c_double * n) (*a)
        cod_c = ct.c_short(cod)
        # ... chamando a funcao
        res = self.__lib.mediana(a_c, n_c, cod_c)

        return res

