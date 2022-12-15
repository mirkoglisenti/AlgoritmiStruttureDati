import sys
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Script per generare file di input per il problema di Exact Cover. È possibile specificare M e N dopo il nome dello script")
parser.add_argument("-M", "--Mcard", type=int, help="Cardinalità di M", default=10)
parser.add_argument("-N", "--Ncard", type=int, help="Cardinalità di N", default=10)
parser.add_argument("-P", "--probability", type=float, help="Probabilità del binomiale per decidere probabilità di uscita di 1 e 0", default=0.5)
parser.add_argument("-I", "--input", type=str, help="Nome del file di input (aaa.txt)", default="input.txt")
args = parser.parse_args()

if __name__ == '__main__':

    M = args.Mcard
    N = args.Ncard
    P = args.probability

    A = np.empty((N, M), dtype=int)
    init = 0

    if M <= N:
        A[0:M] = np.eye(M, dtype=int)
        init = M

    for i in range(init, N):
        nums = np.random.binomial(1, P, M)  # Distribuzione binomiale con percentuale P che esca 0 oppure 1

        equal = False

        for element in A:
            if(nums == element).all():
                equal = True

        while (nums == np.zeros(M)).all() or equal == True:
            nums = np.random.binomial(1, P, M)

            equal = False

            for element in A:
                if (nums == element).all():
                    equal = True

        A[i] = nums

    with open(args.input, 'w') as f:
        f.write(';;; Cardinalità M: ' + str(M) + '\n;;; Cardinalità N: ' + str(N) + '\n;;; Probabilità P: ' + str(P))
        for row in A:
            f.write('\n')
            content = np.array_str(row, max_line_width=sys.maxsize)
            f.write(content[1:-1] + ' -')
