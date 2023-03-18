# python3
import heapq


def parallel_processing(n, m, data):
    output = []
    th_queue = [(0, i) for i in range(n)]
    heapq.heapify(th_queue)


    for i in range(m):
        tm, thr =  heapq.heappop(th_queue)
        output.append((thr, tm))
        heapq.heappush(th_queue, (tm + data[i], thr))


    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = [int(x) for x in input().split()]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = [int(x) for x in input().split()]

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thr, st_tm in result:
        print(thr, st_tm)



if __name__ == "__main__":
    main()
