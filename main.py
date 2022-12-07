import argparse
import numpy as np
import time
from distutils.util import strtobool


class EC:
    def __init__(self, A, plus):
        self.indici_B = None
        self.B = None
        self.COV = []
        self.A = A
        self.n, self.m = A.shape
        self.n -= 1
        self.m -= 1
        self.M = np.ones(self.m + 1, int)
        self.totalNodes = 2 ** self.n
        self.visitedNodes = 0
        self.ecPlus = plus
        self.card = [-1]

    def run(self):
        self.B = np.zeros((self.n, self.n), int)
        prima_riga_libera_B = 0
        self.indici_B = np.zeros(self.n + 1, int)

        for i in range(1, self.n + 1):
            sum = np.sum(self.A[i])
            if sum == 0:
                self.visitedNodes += 1
                break
            elif sum == self.m:
                self.visitedNodes += 1
                self.COV.append([i])
                break

            if self.ecPlus:
                count = 0
                for element in self.A[i]:
                    if element == 1:
                        count += 1
                self.card.insert(i, count)

            self.indici_B[i] = prima_riga_libera_B
            prima_riga_libera_B += 1

            self.visitedNodes += 1

            for j in range(1, i):
                if self.intersezione_A(i, j):
                    self.visitedNodes += 1
                    self.set_B(j, i, 0)
                else:
                    I = np.array([i, j])
                    if self.ecPlus:
                        cardU = self.card[i] + self.card[j]
                    else:
                        U = self.unione(i, j)
                    if self.ecPlus:
                        if cardU == self.m:
                            self.visitedNodes += 1
                            self.COV.append(I)
                            self.set_B(j, i, 0)
                        else:
                            self.set_B(j, i, 1)
                            Inter = self.intersezione_B(i, j)
                            self.visitedNodes += 1
                            if len(Inter) > 0:
                                self.esplora(I, cardU, Inter)
                    else:
                        if (U[1:] == self.M[1:]).all():
                            self.visitedNodes += 1
                            self.COV.append(I)
                            self.set_B(j, i, 0)
                        else:
                            self.set_B(j, i, 1)
                            Inter = self.intersezione_B(i, j)
                            self.visitedNodes += 1
                            if len(Inter) > 0:
                                self.esplora(I, U, Inter)

    def esplora(self, I, U, Inter):
        Inter.sort()
        for k in Inter:
            kk = self.corrispondenza_inversa_indici(k)
            Itemp = I.copy()
            Itemp = np.append(Itemp, kk)
            if self.ecPlus:
                cardU = U
                cardAKK = 0
                for element in self.A[kk]:
                    if element == 1:
                        cardAKK += 1
                cardTemp = cardU + cardAKK
            else:
                Utemp = np.maximum(U, self.A[kk])

            if self.ecPlus:
                if cardTemp == self.m:
                    self.visitedNodes += 1
                    self.COV.append(Itemp)
                else:
                    Intertemp = np.intersect1d(Inter, self.B[:k, k])
                    self.visitedNodes += 1
                    if len(Intertemp) > 0:
                        self.esplora(Itemp, cardTemp, Intertemp)
            else:
                if (Utemp[1:] == self.M[1:]).all():
                    self.visitedNodes += 1
                    self.COV.append(Itemp)
                else:
                    Intertemp = np.intersect1d(Inter, self.B[:k, k])
                    self.visitedNodes += 1
                    if len(Intertemp) > 0:
                        self.esplora(Itemp, Utemp, Intertemp)

    def get_B(self, i, j):
        if i > j:
            i, j = j, i
        return self.B[self.indici_B[i], self.indici_B[j]]

    def corrispondenza_inversa_indici(self, k):
        i = k + 1
        while self.indici_B[i] < k:
            i += 1
        return i

    def set_B(self, i, j, val):
        if i > j:
            i, j = j, i
        self.B[self.indici_B[i], self.indici_B[j]] = val

    def intersezione_A(self, i, j):
        prodotto_righe = self.A[i] * self.A[j]
        somma = np.sum(prodotto_righe)
        return somma > 0

    def intersezione_B(self, i, j):
        if j <= 1:
            return np.array([])
        r_max = self.indici_B[j - 1]
        col_i = self.indici_B[i]
        col_j = self.indici_B[j]
        prodotto_sottocolonne = self.B[:r_max + 1, col_i] * self.B[:r_max + 1, col_j]
        nonzero = np.flatnonzero(prodotto_sottocolonne)
        return nonzero

    def unione(self, i, j):
        return np.maximum(self.A[i], self.A[j])


parser = argparse.ArgumentParser(description="Script Exact Cover")
parser.add_argument("-I", "--input", type=str, help="Nome del file di input (aaa.txt)", default="input.txt")
parser.add_argument("-O", "--output", type=str, help="Nome del file di output (aaa.txt)", default="output.txt")
parser.add_argument("-P", "--plus", type=lambda x: bool(strtobool(x)), help="EC plus", nargs='?', default=False,
                    const=True)
args = parser.parse_args()


if __name__ == '__main__':
#def main(ecplus = False):
    M_size = 0
    file = open(args.input, "r")
    A = []
    for line in file:
        if ';;;' in line:
            continue
        if '-' in line:
            line = list(line.split())
            elements = []
            for element in line[0:-1]:
                elements.append(int(element))
            A.append(elements)

    A = np.array(A)
    m, n = A.shape

    x = np.zeros((1, n), dtype=int)
    A = np.vstack((x, A))

    y = np.zeros((m + 1, 1), dtype=int)
    A = np.column_stack((y, A))

    file.close()

    start = time.time()

    #if args.plus or ecplus:
    if args.plus:
        ec = EC(A, True)
    else:
        ec = EC(A, False)

    ec.run()

    end = time.time()

    execution_time = round((end - start) * 10 ** 3, 3)

    file = open(args.output, "w")
    file.write(';;;Cardinalità di M: ' + str(m) + '\n')
    file.write(';;;Cardinalità di N: ' + str(n) + '\n')
    idx = 1
    for x in A[1:]:
        x = x[1:]
        file.write(';;; Insieme ' + str(idx) + '\n' + str(x) + '\n')
        idx += 1
    file.write('\n;;; COV:\n')
    if ec.COV == []:
        file.write(';;; Nessuna copertura esatta trovata\n')
    else:
        for x in ec.COV:
            file.write(str(x) + '\n')
    if args.plus:
        file.write('\n;;; Algoritmo EC+\n')
    else:
        file.write('\n;;; Algoritmo EC\n')
    file.write(';;; Execution time: ' + str(execution_time) + ' ms\n')
    file.write(';;; Total nodes: ' + str(ec.totalNodes) + ' \n')
    file.write(';;; Visited nodes: ' + str(ec.visitedNodes) + ' \n')
    file.write(';;; Percentage of nodes visited: ' + str(round((ec.visitedNodes / ec.totalNodes) * 100, 2)) + ' \n')
    file.close()

    #return execution_time, ec.visitedNodes