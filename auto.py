import os
import main
import matplotlib.pyplot as plt

N_arr = []
M_arr = []
exec_arr = []
visited_arr = []

for m in range(10, 20):
    for n in range(10, 20):
        max_exec = 0
        max_visited = 0
        for test in range(0, 5):
            os.system("python3 input.py -M" + str(m) + " -N " + str(n))
            execution_time, visited = main.main()
            max_exec = execution_time if execution_time > max_exec else max_exec
            max_visited = visited if visited > max_visited else max_visited
        N_arr.append(n)
        M_arr.append(m)
        visited_arr.append(max_visited)
        exec_arr.append(max_exec)

print(N_arr)
print(M_arr)
print(exec_arr)
print(visited_arr)
plt.figure()
plt.subplot(1, 2, 1)
plt.plot(N_arr, exec_arr, "-g")
plt.subplot(1, 2, 2)
plt.plot(N_arr, visited_arr, "-r")

plt.show()
