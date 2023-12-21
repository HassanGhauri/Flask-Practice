import math
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt

def priority_wise(Z,a,b):

    A = 55
    Zi = Z
    M = 1994
    C = 9

    Z1 = []
    R_list = []
    for i in range(0,10):
        if i == 0:
            Z1.append(Zi) 

        R = (A*Zi+C)%M
        R_list.append(R)
        Z1.append(R)
        
        Zi = R

    # print(R_list)
    # print(Z1)
    R_no = []
    for i in range(len(R_list)):
        random_no = R_list[i]/M
        R_no.append(random_no)

    #print(R_no)

    P_List = []
    for i in range(len(R_no)):
        priority = math.ceil((b-a) * R_no[i] + a)
        P_List.append(priority)

    P_L = np.array([])
    P_L = np.append(P_List,P_L)
    #print(P_L)
    return P_L

# #print(priority_wise(10112166,1,3))

# #priority_wise(10112166,1,3)



# cp= []
# cp_value = 0
# i = 0
# while(cp_value != 1.0):  
#         cp_value += (math.exp(-2.15) * math.pow(2.15,i))/math.factorial(i)
#         cp.append(cp_value)
#         i +=1

# cp_lookup = []    
# cp_lookup.append(0)
# for i in range(len(cp)):
#     cp_lookup.append(cp[i])
#     if i+2 == len(cp):
#         break 


# IA_time = []
# for i in range(len(cp)):
#     IA_time.append(0)


# IA = np.array([],dtype=int)
# IA = np.append(IA_time,IA)

# for j in range(len(cp)):
#     random_no = random.rand()
#     for i in range(len(cp)):
#         if cp_lookup[i] < random_no and random_no <= cp[i]:
#             IA[i] = IA[i]+1
#         if i + 2 == len(cp):
#             break
    

# arrival_time = []
# arrival_time.append(0)
# for i in range(len(IA)):
#     a_t = arrival_time[i] + IA[i]
#     arrival_time.append(a_t)
#     if i+2 == len(IA):
#         break


# service_time = []
# for i in range(len(arrival_time)):
#     random_no = random.rand()
#     st = math.ceil(-1.58*(math.log(random_no)))
#     service_time.append(st)
#     if i+1 == len(arrival_time):
#         break




# df = pd.DataFrame(data={"Cp":cp,"CP_Lookup":cp_lookup,"Inter_arrival_Time":IA,"Arrival_time":arrival_time,"Service_time":service_time})



# #print(cp)
# #print(len(cp))

# # print(cp_lookup)


# # print(IA)
# # print(arrival_time)
# # print(service_time)
# #print(len(cp),len(cp_lookup),len(IA),len(arrival_time),len(service_time))
# #print(df)
# fig = plt.figure(figsize=(12,8))
# cl = ["r","g","b"]

# plt.barh(y=df["Arrival_time"],width=df["Service_time"],color=cl)
# plt.show()