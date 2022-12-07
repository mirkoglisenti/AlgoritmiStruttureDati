# Progetto Algoritmi e Strutture Dati

Progetto per il corso "Algoritmi e Strutture Dati" per la laurea magistrale in Ingegneria Informatica all'Università degli Studi di Brescia.

## Indice

<!-- TOC -->
* [Progetto Algoritmi e Strutture Dati](#progetto-algoritmi-e-strutture-dati)
  * [Indice](#indice)
<!-- TOC -->

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
Notiamo come non sembra in alcun modo 

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


&copy; Glisenti Mirko - Università degli Studi di Brescia (2022)