#ifndef _ESTATISTICA_H_
  #define _ESTATISTICA_H_
  /*... funcoes exportadas*/
  double media(double *x, int n);
  double var(double *x, int n, int ddof);
  double std(double *x, int n, int ddof);
  double mediana(double *x, int n, short cod);

  /*...*/
  static void sort(double *x, int n, short cod);

#endif
