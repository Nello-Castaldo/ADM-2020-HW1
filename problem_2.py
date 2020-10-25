#Birthday Cake Candles

import math
import os
import random
import re
import sys



def birthdayCakeCandles(candles):
    height=max(candles)
    cont=0
    for elem in candles:
        if(elem==height):
            cont+=1
    return cont

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (v2 < v1):
        if ((x1 - x2) % (v2 - v1) == 0):
            return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# Viral Advertising

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    recipients=5
    new_rec=0
    tot=0
    for i in range(n):
        new_rec=(recipients//2)*3
        liked=recipients//2
        recipients=new_rec
        tot+=liked
    return tot

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Recursive Digit Sum

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k,flag):
    lista=list(map(int,n))
    if(not flag):
        total=sum(lista)*k
        return superDigit(str(total),k,True)
    if(len(lista)==1):
        return lista[0]
    else:
        total=sum(lista)
        return superDigit(str(total),k,True)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k,False)

    fptr.write(str(result) + '\n')

    fptr.close()

# Insertion Sort - Part 1
import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    value=arr[n-1]
    i=2
    while(value<arr[n-i] and i<=n):
        temp=arr[n-i]
        arr[n-i+1]=temp
        i+=1
        print(*arr)
    arr[n-i+1]=value
    print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# Insertion Sort - Part 2


import math
import os
import random
import re
import sys


# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    length = len(arr)
    i = 1
    while (i < length):
        j = i - 1
        value = arr[i]
        while (j >= 0 and arr[j] > value):
            temp = arr[j]
            arr[j + 1] = temp
            j -= 1
        arr[j + 1] = value
        i += 1
        print(*arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


