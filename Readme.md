# Progetto Algoritmi e Strutture Dati

Progetto per il corso "Algoritmi e Strutture Dati" per la laurea magistrale in Ingegneria Informatica all'Università degli Studi di Brescia.

## Indice

<!-- TOC -->
* [Obiettivo del progetto](#obiettivo-del-progetto)
* [Implementazione](#implementazione)
* [Fasi del progetto](#fasi-del-progetto)
* [Test](#test)
* [Grafici](#grafici)
  * [Tempo di esecuzione](#tempo-di-esecuzione)
  * [Numero di nodi visitati](#numero-di-nodi-visitati)
* [Conclusioni](#conclusioni)
<!-- TOC -->

## Obiettivo del progetto



## Implementazione


## Fasi del progetto

## Test

## Grafici

Ho creato vari grafici per riportare il numero di nodi visitati (rappresentanti una sorta di complessità spaziale nel caso pessimo)
e il tempo di esecuzione totale dell'algoritmo (rappresentante quindi la complessità temporale) al variare della
cardinalità di N (numero di insiemi di elementi del dominio M).

I grafici sono stati creati con la libreria Matplotlib di Python e usano la scala logaritmica per l'asse
delle y in modo da poter notare più facilmente il comportamento esponenziale delle curve.

Li riporto qua sotto e poi andrò ad analizzarli.

### Tempo di esecuzione

| ![](./img/ec_exec_M_2.png)  | ![](./img/ecplus_exec_M_2.png) |
|:---------------------------:|:------------------------------:|
| *EC (cardinalità di M = 2)* |  *EC+ (cardinalità di M = 2)*  |

| ![](./img/ec_exec_M_3.png)  | ![](./img/ecplus_exec_M_3.png) |
|:---------------------------:|:------------------------------:|
| *EC (cardinalità di M = 3)* |  *EC+ (cardinalità di M = 3)*  |

| ![](./img/ec_exec_M_4.png)  | ![](./img/ecplus_exec_M_4.png) |
|:---------------------------:|:------------------------------:|
| *EC (cardinalità di M = 4)* |  *EC+ (cardinalità di M = 4)*  |

| ![](./img/ec_exec_M_5.png)  | ![](./img/ecplus_exec_M_5.png) |
|:---------------------------:|:------------------------------:|
| *EC (cardinalità di M = 5)* |  *EC+ (cardinalità di M = 5)*  |

| ![](./img/ec_exec_M_6.png)  | ![](./img/ecplus_exec_M_6.png) |
|:---------------------------:|:------------------------------:|
| *EC (cardinalità di M = 6)* |  *EC+ (cardinalità di M = 6)*  |

| ![](./img/ec_exec_M_7.png)  | ![](./img/ecplus_exec_M_7.png) |
|:---------------------------:|:------------------------------:|
| *EC (cardinalità di M = 7)* |  *EC+ (cardinalità di M = 7)*  |


In tutti i grafici qua sopra riportati bisogna verificare l'andamento della curva verde.
Notiamo come non sembra in alcun modo tendere ad un comportamento esponenziale, piuttosto ad uno lineare
ma questo è dovuto alla casualità della generazione dei file di input e quindi rende in parte vana l'analisi
di questa misura temporale. In ogni caso è interessante analizzare come ad input casuali corrispondano comunque sempre
tempi lineari e nell'ordine dei millisecondi. L'analisi è stata svolta con cardinalità massime di N e M pari a 7 in quanto
tentare di lanciare l'algoritmo con delle grandezze massime maggiori comportava una eccezione di segmentation fault.

### Numero di nodi visitati

| ![](./img/ec_visited_M_2.png) | ![](./img/ecplus_visited_M_2.png) |
|:-----------------------------:|:---------------------------------:|
|  *EC (cardinalità di M = 2)*  |   *EC+ (cardinalità di M = 2)*    |

| ![](./img/ec_visited_M_3.png) | ![](./img/ecplus_visited_M_3.png) |
|:-----------------------------:|:---------------------------------:|
|  *EC (cardinalità di M = 3)*  |   *EC+ (cardinalità di M = 3)*    |

| ![](./img/ec_visited_M_4.png) | ![](./img/ecplus_visited_M_4.png) |
|:-----------------------------:|:---------------------------------:|
|  *EC (cardinalità di M = 4)*  |   *EC+ (cardinalità di M = 4)*    |

| ![](./img/ec_visited_M_5.png) | ![](./img/ecplus_visited_M_5.png) |
|:-----------------------------:|:---------------------------------:|
|  *EC (cardinalità di M = 5)*  |   *EC+ (cardinalità di M = 5)*    |

| ![](./img/ec_visited_M_6.png) | ![](./img/ecplus_visited_M_6.png) |
|:-----------------------------:|:---------------------------------:|
|  *EC (cardinalità di M = 6)*  |   *EC+ (cardinalità di M = 6)*    |

| ![](./img/ec_visited_M_7.png) | ![](./img/ecplus_visited_M_7.png) |
|:-----------------------------:|:---------------------------------:|
|  *EC (cardinalità di M = 7)*  |   *EC+ (cardinalità di M = 7)*    |

Anche in questi grafici prendiamo in considerazione la curva verde. Notiamo come, all'aumentare della
cardinalità di M, la curva verde tende ad approssimarsi molto bene alla curva blu ($N^2$). Questo è in linea
con le ipotesi teoriche in quanto il ciclo utilizzato dall'algoritmo dovrà verificare, in sintesi, tutte le coppie (in realtà 
non sono esattamente presi a coppie ma cerchiamo di mantenere il concetto semplice) di elementi dell'insieme N, questo va ad 
approssimarsi molto bene con la grandezza $N^2$.

## Conclusioni

&copy; Glisenti Mirko - Università degli Studi di Brescia (2022)