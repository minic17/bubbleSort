import random


def bubbleSort(input_list):

    listLength = len(input_list)
    
    while(True):
        superTrue=[]
        i=0
        while(i < listLength-1):
            if(input_list[i]<input_list[i+1]):
                tempVar = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i+1] = tempVar
                superTrue.append(False)
            i = i+1
        if(len(superTrue) == 0):
            print(input_list)
            break
        

#testing code written by minic17 2020 ALL RIGHTS RESERVED
n = 100
l = []
for i in range(n):
    l.append(random.randint(1,1000))
print(l)
bubbleSort(l)
print(l)
