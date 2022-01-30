import sys
from operator import itemgetter
from math import ceil

def W_i(tasks, t, i):
    w_i = tasks[i][0]
    for j in range(0,i):
        w_i += ceil(t/tasks[j][1]) * tasks[j][0]
    return w_i

def check(tasks):
    tasks.sort(key = itemgetter(1), reverse = True)
    for i in range(0,len(tasks)):
        feasible = False
        for t in range(1,tasks[i][1] + 1):
            if (W_i(tasks, t, i) <= t):
                feasible = True
                break
        if (not feasible):
            return False
    return True

def main():
    tasks = []
    for i in range(1, len(sys.argv)):
            task_information = sys.argv[i].split(',')
            task = (float(task_information[0]), int(task_information[1]))
            tasks.append(task)

    if (check(tasks)):
        print("There exists a feasible RM-Schedule")
    else:
        print("There doesn't exist a feasible RM-Schedule")

if __name__ == "__main__":
    main()
