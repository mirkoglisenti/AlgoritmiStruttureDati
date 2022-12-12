import argparse
import numpy as np
import time
from distutils.util import strtobool
import sys

sys.setrecursionlimit(2147483647)

class EC:
    def __init__(self, A, plus):
        self.COV = []
        self.A = A
        self.n, self.m = A.shape
        self.zeros = np.zeros(self.m, dtype=int)
        self.ones = np.ones(self.m, dtype=int)
        self.B = np.zeros((self.n, self.n), dtype=int)
        self.totalNodes = 2 ** self.n
        self.visitedNodes = 0
        self.ecPlus = plus
        self.card = np.zeros(self.n, dtype=int)

    def run(self):
        for i in range(0, self.n):
            if (self.A[i] == self.zeros).all():
                self.visitedNodes += 1
                continue
            elif (self.A[i] == self.ones).all():
                self.visitedNodes += 1
                self.COV.append([i])
                continue

            if self.ecPlus:
                count = 0
                for element in self.A[i]:
                    if element == 1:
                        count += 1
                self.card[i] = count

            self.visitedNodes += 1

            for j in range(0, i):
                if np.logical_and(self.A[i], self.A[j]).any():
                    self.visitedNodes += 1
                    self.B[j, i] = 0
                else:
                    I = np.array([i, j])
                    if self.ecPlus:
                        cardU = self.card[i] + self.card[j]
                        if cardU == self.m:
                            self.visitedNodes += 1
                            self.COV.append(I)
                            self.B[j, i] = 0
                        else:
                            self.B[j, i] = 1
                            Inter = np.logical_and(self.B[0:j, i], self.B[0:j, j]).astype(int)
                            self.visitedNodes += 1
                            if len(Inter) > 0 and (Inter != np.zeros(len(Inter), dtype=int)).any():
                                self.esplora(I, cardU, Inter)
                    else:
                        U = np.logical_or(self.A[i], self.A[j]).astype(int)
                        if (U == self.ones).all():
                            self.visitedNodes += 1
                            self.COV.append(I)
                            self.B[j, i] = 0
                        else:
                            self.B[j, i] = 1
                            Inter = np.logical_and(self.B[0:j, i], self.B[0:j, j]).astype(int)
                            self.visitedNodes += 1
                            if len(Inter) > 0 and (Inter != np.zeros(len(Inter), dtype=int)).any():
                                self.esplora(I, U, Inter)

    def esplora(self, I, U, Inter):
        for k in range(0, len(Inter)):
            if Inter[k] == 1:
                Itemp = I.copy()
                Itemp = np.append(Itemp, k)

                if self.ecPlus:
                    cardU = U
                    cardAKK = 0
                    for element in self.A[k]:
                        if element == 1:
                            cardAKK += 1
                    cardTemp = cardU + cardAKK

                    if cardTemp == self.m:
                        self.visitedNodes += 1
                        self.COV.append(Itemp)
                    else:
                        Intertemp = np.intersect1d(Inter, self.B[:k, k])
                        self.visitedNodes += 1
                        if len(Intertemp) > 0:
                            self.esplora(Itemp, cardTemp, Intertemp)
                else:
                    Utemp = np.logical_or(U, self.A[k]).astype(int)

                    if (Utemp == self.ones).all():
                        self.visitedNodes += 1
                        self.COV.append(Itemp)
                    else:
                        Intertemp = np.logical_and(Inter[0:k], self.B[0:k, k]).astype(int)
                        self.visitedNodes += 1
                        if (Intertemp != np.zeros(len(Intertemp), dtype=int)).any():
                            self.esplora(Itemp, Utemp, Intertemp)


parser = argparse.ArgumentParser(description="Script Exact Cover")
parser.add_argument("-I", "--input", type=str, help="Nome del file di input (aaa.txt)", default="input.txt")
parser.add_argument("-O", "--output", type=str, help="Nome del file di output (aaa.txt)", default="output.txt")
parser.add_argument("-P", "--plus", type=lambda x: bool(strtobool(x)), help="EC plus", nargs='?', default=False,
                    const=True)
args = parser.parse_args()


#if __name__ == '__main__':
def main(ecplus = False):
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

    A = np.array(A, dtype=int)

    n, m = A.shape

    file.close()

    start = time.time()

    if args.plus or ecplus:
    #if args.plus:
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
    for x in A:
        file.write(';;; Insieme ' + str(idx) + '\n' + str(x) + '\n')
        idx += 1
    file.write('\n;;; COV:\n')
    if ec.COV == []:
        file.write(';;; Nessuna copertura esatta trovata\n')
    else:
        for x in ec.COV:
            x = np.array(x, dtype=int)
            file.write(str(x+1) + '\n')
    if args.plus:
        file.write('\n;;; Algoritmo EC+\n')
    else:
        file.write('\n;;; Algoritmo EC\n')
    file.write(';;; Execution time: ' + str(execution_time) + ' ms\n')
    file.write(';;; Total nodes: ' + str(ec.totalNodes) + ' \n')
    file.write(';;; Visited nodes: ' + str(ec.visitedNodes) + ' \n')
    file.write(';;; Percentage of nodes visited: ' + str(round((ec.visitedNodes / ec.totalNodes) * 100, 2)) + ' \n')
    file.close()

    return execution_time, ec.visitedNodes