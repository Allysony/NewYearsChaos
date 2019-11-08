#!/bin/python3
import math
import os
import random
import re
import sys

def minimumBribes(q):
    num_of_bribes = 0 
    length_of_queue = len(q) 
    # inspect from the end of queue
    while (length_of_queue != 1):
        # no bribes
        if q[length_of_queue - 1] == length_of_queue:
            pass 
        # 1 bribe
        elif q[length_of_queue - 2] == length_of_queue:
            num_of_bribes = num_of_bribes + 1
            temp = q[length_of_queue - 1]
            q[length_of_queue - 1] = length_of_queue
            q[length_of_queue - 2] = temp
        # 2 bribes
        elif q[length_of_queue - 3] == length_of_queue:
            num_of_bribes = num_of_bribes + 2
            temp = q[length_of_queue - 1]
            q[length_of_queue - 1] = length_of_queue
            temp2 = q[length_of_queue - 2]
            q[length_of_queue - 2] = temp
            q[length_of_queue - 3] = temp2
        # More than 2 bribes
        else:
            print("Too chaotic")
            return
        length_of_queue = length_of_queue - 1
    print(num_of_bribes)


      
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
