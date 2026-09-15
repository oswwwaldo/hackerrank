#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    
    if (len(responseTimes) > 0):   
            
        count = 0;
    
        for number, index in enumerate(responseTimes):
            num = responseTimes[number]
            
            if (number > 0):
                previous_numbers = responseTimes[:number]
                average_time = sum(previous_numbers) / len(previous_numbers)
                
                if num > average_time:
                    count+=1;
        
        return count;
    
    else:
        return 0;

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
