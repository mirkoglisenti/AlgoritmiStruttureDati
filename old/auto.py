import os
import main
import matplotlib.pyplot as plt
import sys
import gc
import faulthandler



faulthandler.enable()


#print(sys.getrecursionlimit())

M_min = 2
M_max = 8
N_min = 2
N_max = 8

sys.setrecursionlimit(2147483647)

for m in range(M_min, M_max):
    N_arr = []
    exec_arr = []
    visited_arr = []
    for n in range(N_min, N_max):
        max_exec = 0
        max_visited = 0
        for test in range(0, 5):
            os.system("python3 input.py -M" + str(m) + " -N " + str(n))
            execution_time, visited = main.main(False)
            max_exec = execution_time if execution_time > max_exec else max_exec
            max_visited = visited if visited > max_visited else max_visited
        N_arr.append(n)
        visited_arr.append(max_visited)
        exec_arr.append(max_exec)
    # plt.subplot(5, 2, m%10+1)
    plt.figure(figsize=(12, 8), dpi=300)
    plt.semilogy(N_arr, exec_arr, "-g", label="Execution time")
    plt.semilogy(N_arr, N_arr, '-r', label="N")
    plt.semilogy(N_arr, list(map(lambda x:pow(x,2),N_arr)), '-b', label="$N^2$")
    plt.semilogy(N_arr, list(map(lambda x: 2**x, N_arr)), '-k', label="$2^N$")
    plt.legend()
    plt.title('EC - Execution time - M Card = ' + str(m))
    plt.xlabel('N cardinality')
    plt.ylabel('Execution time [ms]')
    plt.tight_layout()
    plt.grid()
    plt.savefig('img/ec_exec_M_' + str(m) + '.png')
    plt.close()
    plt.figure(figsize=(12, 8), dpi=300)
    plt.semilogy(N_arr, visited_arr, "-g", label="Visited nodes")
    plt.semilogy(N_arr, N_arr, '-r', label="N")
    plt.semilogy(N_arr, list(map(lambda x: pow(x, 2), N_arr)), '-b', label="$N^2$")
    plt.semilogy(N_arr, list(map(lambda x: 2 ** x, N_arr)), '-k', label="$2^N$")
    plt.legend()
    plt.title('EC - Visited nodes - M Card = ' + str(m))
    plt.xlabel('N cardinality')
    plt.ylabel('Visited nodes')
    plt.tight_layout()
    plt.grid()
    plt.savefig('img/ec_visited_M_' + str(m) + '.png')
    plt.close()
    del N_arr
    del exec_arr
    gc.collect()

for m in range(M_min, M_max):
    N_arr = []
    exec_arr = []
    visited_arr = []
    for n in range(N_min, N_max):
        max_exec = 0
        max_visited = 0
        for test in range(0, 5):
            os.system("python3 input.py -M" + str(m) + " -N " + str(n))
            execution_time, visited = main.main(True)
            max_exec = execution_time if execution_time > max_exec else max_exec
            max_visited = visited if visited > max_visited else max_visited
        N_arr.append(n)
        visited_arr.append(max_visited)
        exec_arr.append(max_exec)
    # plt.subplot(5, 2, m%10+1)
    plt.figure(figsize=(12, 8), dpi=300)
    plt.semilogy(N_arr, exec_arr, "-g", label="Execution time")
    plt.semilogy(N_arr, N_arr, '-r', label="N")
    plt.semilogy(N_arr, list(map(lambda x:pow(x,2),N_arr)), '-b', label="$N^2$")
    plt.semilogy(N_arr, list(map(lambda x: 2 ** x, N_arr)), '-k', label="$2^N$")
    plt.legend()
    plt.title('EC+ - Execution time - M Card = ' + str(m))
    plt.xlabel('N cardinality')
    plt.ylabel('Execution time [ms]')
    plt.tight_layout()
    plt.grid()
    plt.savefig('img/ecplus_exec_M_' + str(m) + '.png')
    plt.close()
    plt.figure(figsize=(12, 8), dpi=300)
    plt.semilogy(N_arr, visited_arr, "-g", label="Visited nodes")
    plt.semilogy(N_arr, N_arr, '-r', label="N")
    plt.semilogy(N_arr, list(map(lambda x: pow(x, 2), N_arr)), '-b', label="$N^2$")
    plt.semilogy(N_arr, list(map(lambda x: 2 ** x, N_arr)), '-k', label="$2^N$")
    plt.legend()
    plt.title('EC+ - Visited nodes - M Card = ' + str(m))
    plt.xlabel('N cardinality')
    plt.ylabel('Visited nodes')
    plt.tight_layout()
    plt.grid()
    plt.savefig('img/ecplus_visited_M_' + str(m) + '.png')
    plt.close()
    del N_arr
    del exec_arr
    gc.collect()



#plt.subplot(1, 2, 1)
#plt.plot(N_arr, exec_arr, "-g")
#plt.subplot(1, 2, 2)
#plt.plot(N_arr, visited_arr, "-r")
