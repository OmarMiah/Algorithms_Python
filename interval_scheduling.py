import bisect # finds where to put a value in a sorted list to remain sorted

def previous_intervals(I):
    p = []
    start = [task[0] for task in I]
    finish = [task[1] for task in I] 

    for i in range(len(I)):
        index = bisect.bisect(finish, start[i]) - 1
        p.append(index)

    return p


def find_solution(j):
    if j == -1:
        return
    else: 
        if (I[j][2] + OPT[p[j]]) >= OPT[j-1]:
            O.append(I[j])
            find_solution(p[j])
        else: 
            find_solution(j-1)
    pass

def compute_opt(j):
    # use recursive formula max(Wj + OPT(p(j)), OPT(j-1))
    if j == -1:
        return 0
    elif (0 <= j) and (j < len(OPT)):
        return OPT[j]
    else:
        return max (I[j][2] + compute_opt(p[j]), compute_opt(j-1))
    

def weighted_interval(I):
    for j in range(len(I)):
        opt_j = compute_opt(j)
        OPT.append(opt_j)

    find_solution(len(I)-1)
    
    return OPT[-1]

if __name__ == "__main__":
    # OPT for optimal weight, 0 for best items to pick 
    OPT = []
    O = []

    # (start, end, weight)
    t1 = (0,3,3)
    t2 = (1,4,2)
    t3 = (0,5,4)
    t4 = (3,6,1)
    t5 = (4,7,2)
    t6 = (3,9,5)
    t7 = (5,10,2)
    t8 = (8,10,1)
     
    # list of intervals to be sorted
    I = [t1,t2,t3,t4,t5,t6,t7,t8]
    # key is the function used to sort the where I pass in lambda
    # input is a tuple and out
    I.sort(key = lambda tup : tup[1])

    p = previous_intervals(I)

    opt_solution = weighted_interval(I)
    print('Maximum weight: ' + str(opt_solution))
    print('The best jobs to take are: ' + str(O[::-1]))