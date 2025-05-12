import random
import Fitting
import time
from matplotlib import pyplot as plt
#sorting algorithm
def bubble_sort(L):
    n = len(L)
    for i in range(n):
        for j in range(n):
            if L[i] < L[j]:
                L[i], L[j] = L[j], L[i]
#calculating time function
def time_function(func, args):
    start = time.time()
    func(args)
    return time.time() - start
if __name__ == "__main__":
    #generate length of lists to sort
    nums = [i for i in range(0,1001,50)]
    times = []

    #generate random lists and calculate times
    for n in nums:
        L = [random.randint(0,n) for i in range(n)]
        times.append(1000 * time_function(bubble_sort,L))

    #plot
    plt.figure()
    plt.scatter(nums, times, c='b', marker='x', label="raw data")

    #call fit data and plot is as the y
    plt.plot(nums, Fitting.fit_data(Fitting.lin, nums, times)[2], c='g', label="linear")
    plt.plot(nums, Fitting.fit_data(Fitting.quad, nums, times)[2], c='r', label='quad')
    plt.legend()
    plt.xlabel("number of items to sort")
    plt.ylabel("time to sort (ms)")
    plt.savefig("bestfit.png")
