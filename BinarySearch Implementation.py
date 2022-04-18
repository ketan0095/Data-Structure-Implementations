from math import floor
import time

#---------------------------------------------------
# Binary Search 
# Problem : Search number from a list quickly
# Complexity : O(log n)
#---------------------------------------------------

# list need to be sorted

sc1 =[]
sc2 =[]

def findMiddle(num1,num2):
    range_ =num2-num1
    middle = float(range_)/2
    return num1 + floor(middle)


for j in range(1,9):
    range_ =10**j+1
    if range_ not in sc1:
        sc1.append(range_)
    user_list =[i for i in range(range_)]

    # user_input =user_list[-1]  # worse case 
    user_input = user_list[-1]//2

    # set the limits
    lower_lim =user_list[0]
    upper_lim =user_list[-1]


    check_ =findMiddle(lower_lim,upper_lim)
    # count =0

    t1 =time.time()

    while True:
        if check_ == user_input:
            break
        
        if check_ < user_input:
            lower_lim =check_
            upper_lim =user_list[-1]
            check_ =findMiddle(lower_lim,upper_lim)
            if check_ == upper_lim:
                break

        if check_ > user_input:
            lower_lim =user_list[0]
            upper_lim_index =user_list.index(check_)
            upper_lim =user_list[upper_lim_index]
            check_ =findMiddle(lower_lim,upper_lim)
            if check_ == upper_lim:
                break
    #     count +=1
    # print("count :",count)
    time.sleep(0.0001)
    t2 =round(time.time()-t1,6)
    # print("Total time taken for range {} is {} secs".format(range_,t2))
    sc2.append(t2)


print("Binary Search results : ")
print(sc1)
print(sc2)
print("--------------------------------------")
