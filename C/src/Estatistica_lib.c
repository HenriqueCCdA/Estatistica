#include<stdio.h>
#include<math.h>
#include"Estatistica_lib.h"
#include"Ord.h"

/**********************************************************************
 * Data de criacao  : 17/04/2020                                      *
 * Data de modificao: 00/00/0000                                      *
 * -------------------------------------------------------------------*
 * Media : Cacula a media de a                                        *
 * -------------------------------------------------------------------*
 * Paremetros de enrada:                                              *
 * -------------------------------------------------------------------*
 * a -> valores                                                       *
 * n -> numero de termos                                              *
 * -------------------------------------------------------------------*
 * Retorno: a media de a                                              *
 * -------------------------------------------------------------------*
**********************************************************************/
double media(double *x, int n){

    int i;
    double xBar;
    
    if( n == 1 )
      return x[0];

    for(i=0, xBar = 0; i<n ; i++)
      xBar += x[i]; 
 
    return xBar /= (double) n;
}
/*********************************************************************/

/**********************************************************************
 * Data de criacao  : 17/04/2020                                      *
 * Data de modificao: 00/00/0000                                      *
 * -------------------------------------------------------------------*
 * Var : Cacula a varianvia de a                                      *
 * -------------------------------------------------------------------*
 * Paremetros de enrada:                                              *
 * -------------------------------------------------------------------*
 * a    -> valores                                                    *
 * n    -> numero de termos                                           *
 * ddof -> graus de liberdade                                         *
 * -------------------------------------------------------------------*
 * Retorno: a variancia de a                                          *
 * -------------------------------------------------------------------*
 * OBS:                                                               *
 * -------------------------------------------------------------------*
 * ddof = 0 : variancia populacional                                  *
 * ddof = 1 : variancia amostral                                      *
**********************************************************************/
double var(double *x, int n, int ddof){

    int i, N;
    double var, xBar, delta;
   
    xBar = media(x, n);

    for(i=0, var = 0; i<n ; i++)
    {
      delta = x[i] - xBar;
      var  += delta*delta; 
    } 

    N = n - ddof;
    
    return var /= (double) N;
}
/**********************************************************************/

/***********************************************************************
 * Data de criacao  : 17/04/2020                                       *
 * Data de modificao: 00/00/0000                                       *
 * --------------------------------------------------------------------*
 * std : Cacula o desvio padrao de a                                   *
 * --------------------------------------------------------------------*
 * Paremetros de enrada:                                               *
 * --------------------------------------------------------------------*
 * a    -> valores                                                     *
 * n    -> numero de termos                                            *
 * ddof -> graus de liberdade                                          *
 * --------------------------------------------------------------------*
 * Retorno: o desvio padrao de a                                       *
 * --------------------------------------------------------------------*
 * OBS:                                                                *
 * --------------------------------------------------------------------*
 * ddof = 0 : variancia populacional                                   *
 * ddof = 1 : variancia amostral                                       *
***********************************************************************/
double std(double *x, int n, int ddof){

    return sqrt(var(x, n, ddof));

}
/**********************************************************************/

double mediana(double *x, int n, short cod){

  int id;

  if( n == 1 )
    return x[0];

  sort(x, n, 1);

/*... numero impar*/
  if(n%2){
    id = n/2;
    return x[id];
  }
/*... numero par*/
  else{
    id = n/2;
    return (x[id] + x[id-1])*0.5e0;
  }

}
/**********************************************************************/

/**********************************************************************
 * Data de criacao  : 17/04/2020                                      *
 * Data de modificao: 00/00/0000                                      *
 * -------------------------------------------------------------------*
 * sort : chama o algorimo de ordenacao desejado                      * 
 * -------------------------------------------------------------------*
 * Paremetros de enrada:                                              *
 * -------------------------------------------------------------------*
 * x -> valores                                                       *
 * n -> numero de termos                                              *
 * cos -> algoritmo desejado                                          *
 * -------------------------------------------------------------------*
 * Retorno: x ordenado                                                *
 * -------------------------------------------------------------------*
**********************************************************************/
static void sort(double *x, int n, short cod)
{  
  if(cod == 1)
    bubblesort(x, n);  
}
/**********************************************************************/