import os
import main
import matplotlib.pyplot as plt
import sys
import gc

#print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000000)

for m in range(3, 10):
    N_arr = []
    exec_arr = []
    visited_arr = []
    for n in range(2, 7):
        max_exec = 0
        max_visited = 0
        for test in range(0, 5):
            os.system("python3 input.py -M" + str(m) + " -N " + str(n))
            execution_time, visited = main.main()
            max_exec = execution_time if execution_time > max_exec else max_exec
            max_visited = visited if visited > max_visited else max_visited
        N_arr.append(n)
        visited_arr.append(max_visited)
        exec_arr.append(max_exec)
    # plt.subplot(5, 2, m%10+1)
    plt.figure(figsize=(12, 8), dpi=300)
    plt.semilogy(N_arr, exec_arr, "-g")
    plt.semilogy(N_arr, N_arr, '-r')
    plt.semilogy(N_arr, list(map(lambda x:pow(x,2),N_arr)), '-b')
    plt.title('Execution time - M Card = ' + str(m))
    plt.xlabel('N cardinality')
    plt.ylabel('Execution time [ms]')
    plt.tight_layout()
    plt.savefig('img/exec_M_' + str(m) + '.png')
    plt.figure(figsize=(12, 8), dpi=300)
    plt.semilogy(N_arr, visited_arr, "-g")
    plt.semilogy(N_arr, N_arr, '-r')
    plt.semilogy(N_arr, list(map(lambda x: pow(x, 2), N_arr)), '-b')
    plt.title('Visited nodes - M Card = ' + str(m))
    plt.xlabel('N cardinality')
    plt.ylabel('Visited nodes')
    plt.tight_layout()
    plt.savefig('img/visited_M_' + str(m) + '.png')
    del N_arr
    del exec_arr
    gc.collect()


#plt.subplot(1, 2, 1)
#plt.plot(N_arr, exec_arr, "-g")
#plt.subplot(1, 2, 2)
#plt.plot(N_arr, visited_arr, "-r")
