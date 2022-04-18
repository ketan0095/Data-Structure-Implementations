# -------------------------------------------------
# Linear Search
# Problem : Search number from a list sequentially
# Complexity : O(n)
# -------------------------------------------------
from math import floor
import time

# list need not have to be sorted

scale1 = []
scale2 = []

for j in range(1, 9):
    # range_ =100000001
    range_ = 10**j + 1
    # print("range is ",range_)
    user_list = [i for i in range(range_)]

    # user_input =range_-1  3 worse case
    user_input = range_ // 2

    t1 = time.time()
    # print("Searching strated :")
    for i in range(len(user_list)):
        if i == user_input:
            # print("Found it !!")
            t2 = time.time() - t1
            scale1.append(range_)
            scale2.append(t2)
            break
    else:
        # print("Could not find the no.")
        t2 = time.time() - t1
    # print("Time taken for {} secs : {}".format(j,t2))

    # break

print("Linear Search results : ")
print(scale1)
print(scale2)
print("------------------------------------------")
