import argparse

parser = argparse.ArgumentParser(description="Script per verificare uguaglianza tra file di output")
parser.add_argument("-1", "--input1", type=str, help="Primo file", default="output1.txt")
parser.add_argument("-2", "--input2", type=str, help="Secondo file", default="output2.txt")
args = parser.parse_args()

if __name__ == '__main__':

    COV1 = []
    COV2 = []
    visited1 = 0
    visited2 = 0
    time1 = 0
    time2 = 0

    with open(args.input1, 'r') as file:
        for line in file:
            if ';;; COV' not in line:
                continue
            break
        for line in file:
            if ';;;' in line:
                break
            line = list(list(map(int, line[1:-2].split())))
            COV1.append(line)
        COV1 = COV1[0:-1]
        for line in file:
            if ';;; Execution' in line:
                time1 = float(line.split()[3])
            if ';;; Visited' in line:
                visited1 = int(line.split()[3])

    with open(args.input2, 'r') as file:
        for line in file:
            if ';;; COV' not in line:
                continue
            break
        for line in file:
            if ';;;' in line:
                break
            line = list(list(map(int, line[1:-2].split())))
            COV2.append(line)
        COV2 = COV2[0:-1]
        for line in file:
            if ';;; Execution' in line:
                time2 = float(line.split()[3])
            if ';;; Visited' in line:
                visited2 = int(line.split()[3])

    if (COV1 == COV2) and (visited1 == visited2):
        print('I due algoritmi hanno prodotto la stessa soluzione\n')
        if time2 < time1:
            print('Il primo output è stato più veloce di ' + str(round(time1 - time2, 3)) + ' secondi')
        else:
            print('Il primo output è stato più lento di ' + str(round(time2 - time1, 3)) + ' secondi')
    else:
        print('ERRORE: I due algoritmi NON hanno prodotto la stessa soluzione\n')