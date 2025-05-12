from matplotlib import pyplot as plt        # import plotting funcs
from TimeFunctions import  time_function    # import the time function you will write
from Duplicates import has_duplicates_1, has_duplicates_2     # import the has_duplicates functions you are interested in


# All code below is included as a demo. Feel free to change any of it.

##### Initialize datasets
x = [100, 500, 1000]
x1 = range(0,1001,50)


##### Measure the running times
# Generate 3 corresponding y-values
y1 = []
for n in x:
    L = [i for i in range(n)] # Worst case: A list with no duplicates
    y1.append(time_function(has_duplicates_1, L)) # append running time to y
y2 = []
for n in x1:
    L = [i for i in range(n)] # Worst case: A list with no duplicates
    y2.append(1000 * time_function(has_duplicates_1, L)) # append running time to y
y3 = []
for n in x1:
    L = [i for i in range(n)] # Worst case: A list with no duplicates
    y3.append(1000 * time_function(has_duplicates_2, L)) # append running time to y
##### Plot datasets
plt.figure()                                                        # create a new figure
plt.scatter(x, y1, c='r', marker='x', label='has_duplicates_1')     # add scatter plot to figure
plt.ylabel("running time (s)")                                      # label y axis
plt.legend()                                                        # add legend to figure
plt.savefig('fig_1.png')

plt.figure()                                                        # create a new figure
plt.scatter(x1, y2, c='r', marker='x', label='has_duplicates_1')     # add scatter plot to figure
plt.scatter(x1, y3, c='b', marker='*', label='has_duplicates_2')
plt.xlabel("number of items")
plt.ylabel("running time (ms)")                                      # label y axis
plt.legend()                                                        # add legend to figure
plt.savefig('dups.png')                                          # save figure

# Note: You can either use plt.show() or plt.savefig(). Using both does not work.



