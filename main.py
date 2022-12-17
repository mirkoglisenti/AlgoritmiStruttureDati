import argparse
import numpy as np
import time
from distutils.util import strtobool
import sys
from threading import Thread
import keyboard
import os

sys.setrecursionlimit(2147483647)

class EC(Thread):
# class EC:
    def __init__(self, A, plus):
        super().__init__()
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
        self.stop = False

    def run(self):
        for i in range(0, self.n):
            if self.stop:
                break
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
                if self.stop:
                    break
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

    # @njit
    def esplora(self, I, U, Inter):
        for k in range(0, len(Inter)):
            if self.stop:
                break
            if Inter[k] == 1:
                Itemp = I.copy()
                Itemp = np.append(Itemp, k)

                if self.ecPlus:
                    cardTemp = U + self.card[k]

                    if cardTemp == self.m:
                        self.visitedNodes += 1
                        self.COV.append(Itemp)
                    else:
                        Intertemp = np.logical_and(Inter[0:k], self.B[0:k, k]).astype(int)
                        self.visitedNodes += 1
                        if (Intertemp != np.zeros(len(Intertemp), dtype=int)).any():
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
parser.add_argument("-P", "--plus", type=lambda x: bool(strtobool(x)), help="EC plus", nargs='?', default=False, const=True)
parser.add_argument("-T", "--time", type=int, help="Tempo massimo esecuzione [s]", default=-1)
args = parser.parse_args()


if __name__ == '__main__':
# def main(ecplus = False):
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

    # if args.plus or ecplus:
    if args.plus:
        print('Algoritmo EC+')
        ec = EC(A, True)
    else:
        print('Algoritmo EC')
        ec = EC(A, False)

    start = time.time()

    ec.start()
    # ec.run()

    if args.time != -1:
        print('Eseguo lo script con un timeout di ' + str(args.time) + ' secondi ...')
        while time.time() - start < args.time:
            continue
        ec.stop = True
    else:
        print('Calcolo in corso ...')
        print('Puoi interrompere l\'esecuzione in qualsiasi momento premendo il tasto "q"')
        while ec.is_alive() and not keyboard.is_pressed("q"):
            continue
        if ec.is_alive():
            ec.stop = True

    ec.join()

    end = time.time()

    execution_time = round((end - start), 3)

    print('Calcolo terminato in ' + str(execution_time) + ' secondi!')
    print('Salvo il file di output con tutte le informazioni')

    file = open(args.output, "w")
    file.write(';;;Cardinalità di M: ' + str(m) + '\n')
    file.write(';;;Cardinalità di N: ' + str(n) + '\n')
    idx = 1
    for x in A:
        file.write(';;; Insieme ' + str(idx) + '\n' + str(x) + '\n')
        idx += 1
    if ec.stop:
        file.write('\n;;; COV (script interrotto):\n')
    else:
        file.write('\n;;; COV:\n')
    if ec.COV == []:
        file.write(';;; Nessuna copertura esatta trovata\n')
    else:
        for x in ec.COV:
            x = np.array(x, dtype=int)
            file.write(str(x+1) + '\n')
    if args.plus:
    # if args.plus or ecplus:
        file.write('\n;;; Algoritmo EC+\n')
    else:
        file.write('\n;;; Algoritmo EC\n')
    file.write(';;; Execution time: ' + str(execution_time) + ' s (' + str(round(execution_time/60, 3)) + ' minutes) \n')
    file.write(';;; Total nodes: ' + str(ec.totalNodes) + ' \n')
    file.write(';;; Visited nodes: ' + str(ec.visitedNodes) + ' \n')
    file.write(';;; Percentage of nodes visited: ' + str(round((ec.visitedNodes / ec.totalNodes) * 100, 2)) + ' \n')
    file.close()

    uid = int(os.environ.get('SUDO_UID'))
    gid = int(os.environ.get('SUDO_GID'))

    os.chown(args.output, uid, gid)

    print('Fatto!\nTermino la mia esecuzione')

    # return execution_time, ec.visitedNodes