#Say "Hello, World!" With Python
print("Hello, World!")
#Python If-Else
n= int(input())
if(n % 2==1):
    print("Weird")

else:
    if(2<=n<=5 or n>20):
        print("Not Weird")
    else:
        print("Weird")

#Arithmetic Operators

a = int(input())
b = int(input())

print(a+b)
print(a-b)
print(a*b)

#Python: Division

a = int(input())
b = int(input())
print(a//b)
print(a/b)


#Loops
n = int(input())
for i in range(n):
    print(i*i)

#Write a function
def is_leap(year):
    leap = False
    if (year % 4 != 0):
        return leap
    else:
        if (year % 100 == 0 and year % 400 != 0):
            return leap
        else:
            leap = True

    return leap

#Print Function
n = int(input())
    string=''
    for i in range(n):
        string= string+ str(i+1)

print(string)

#List Comprehensions
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(result)

#Find the Runner-Up Score
n = int(input())
arr = list(map(int, input().split()))
maxi = max(arr)
lista = []
for elem in arr:
    if (elem != maxi):
        lista.append(elem)

print(max(lista))

#Nested Lists
big_list = []
score_list = []
for _ in range(int(input())):
    little_list = []
    name = input()
    score = float(input())
    little_list.append(name)
    little_list.append(score)
    score_list.append(score)
    big_list.append(little_list)

mini = min(score_list)
new_list = []
for elem in score_list:
    if (elem != mini):
        new_list.append(elem)
slg = min(new_list)

big_list.sort()
for item in big_list:
    if (item[1] == slg):
        print(item[0])

#Finding the percentage
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
total=0
for item in student_marks[query_name]:
    total=total+item
print("{0:.2f}".format(total/3))

#Lists
N = int(input())
lista = []
for i in range(N):
    line = []
    line = input().split()
    if (line[0] == "print"):
        print(lista)
    elif (len(line) == 1):
        eval('lista.{}()'.format(line[0]))

    elif (len(line) == 2):
        eval('lista.{}({})'.format(line[0], line[1]))
    elif (len(line) == 3):
        eval('lista.{}({},{})'.format(line[0], line[1], line[2]))

#Tuples
n = int(input())
integer_list = map(int, input().split())
tupla=tuple(integer_list)
print(hash(tupla))

#sWAP cASE
def swap_case(s):
    stringa = ''
    for elem in s:
        if (97 <= ord(elem) <= 122):
            stringa = stringa + elem.upper()

        else:
            stringa = stringa + elem.lower()

    return stringa

#String Split and Join
def split_and_join(line):
    lista=line.split()
    result="-".join(lista)
    return result

#What's Your Name?
def print_full_name(a, b):
    print("Hello "+a+" "+b+"! You just delved into python.")

#Mutations
def mutate_string(string, position, character):
    lista = list(string)
    lista[position] = character

    return ("").join(lista)

#Find a string
def count_substring(string, sub_string):
    count = 0
    i = 0
    j = 0
    sub_len = len(sub_string)
    while i < len(string):

        if (string[i:(i + sub_len)] == sub_string):
            count = count + 1
            i = i + 1
        else:
            i = i + 1

    return count

#String Validators
s = input()
    alnum=False
    alpha=False
    digits=False
    lower=False
    upper=False
    for elem in s:
        if(elem.isalpha()):
            alnum=True
            alpha=True
        if(elem.isdigit()):
            digits=True
            alnum= True
        if(elem.islower()):
            lower=True
        if(elem.isupper()):
            upper=True
    print(alnum)
    print(alpha)
    print(digits)
    print(lower)
    print(upper)

#Text Wrap
def wrap(string, max_width):
    i = 0
    result = ''
    while (i < len(string)):
        if (i % max_width == 0 and i != 0):

            result = result + "\n" + string[i]
            i = i + 1
        else:
            result = result + string[i]
            i = i + 1
    return result

#Designer Door Mat
n,m= map(int,input().split())
for i in range(1,n,2):
    print((i*".|.").center(m,"-"))
print("WELCOME".center(m,"-"))
for i in range(n-2,0,-2):
    print((i*".|.").center(m,"-"))

#String Formatting (fail)
def print_formatted(number):
    space_1=len(str(bin(number)).replace("0o",''))
    space=space_1*" "
    for i in range(1,number+1,1):
        binary=bin(i)
        octal=oct(i)
        hexadecimal=hex(i).capitalize()
        final=str(i) +space+str(octal).replace("0o",'')+space+str(hexadecimal).replace("0x",'')+space+str(binary).replace("0b",'')
        print(final)

#Capitalize!
def solve(s):
    lista = s.split(" ")
    new_list = []
    print(lista)
    for elem in lista:
        new_list.append(elem.capitalize())
    return (" ").join(new_list)

#The Minion Game
def minion_game(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    lista = []
    for i in range(len(string)):
        if (string[i] in vowels):
            kevin = kevin + len(string[i:])

        else:
            stuart = stuart + len(string[i:])
    if (kevin > stuart):
        print("Kevin " + str(kevin))
    elif (stuart > kevin):
        print("Stuart " + str(stuart))
    else:
        print("Draw")

#Merge the Tools
def merge_the_tools(string, k):
    lista = []
    new_string = ''
    cont = 1
    for i in range(0, len(string)):
        if (cont == k):
            if (string[i] not in new_string):
                new_string = new_string + string[i]
            lista.append(new_string)
            new_string = ''
            cont = 1
        else:
            if (string[i] not in new_string):
                new_string = new_string + string[i]
            cont += 1

    for elem in lista:
        print(elem)

#Introduction to Sets
def average(array):
    ins= set(array)
    return sum(ins)/len(ins)

#Symmetric Difference
n=int(input())
lista1=list(map(int,input().split()))
m=int(input())
lista2= list(map(int,input().split()))
set_1=set(lista1)
set_2=set(lista2)
dif_1=list(set_1.difference(set_2))
dif_2=list(set_2.difference(set_1))
result= dif_1+dif_2
result.sort()
for  elem in result:
    print(elem)

#No Idea!
m,n=list(map(int,input().split()))
arr=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
happyness=0
for elem in arr:
    if(elem in A):
        happyness+=1
    if(elem in B):
        happyness-=1
print(happyness)

#Set.add()
n= int(input())
ins=set()
for i in range(n):
    ins.add(input())
print(len(ins))

#Set .discard(), .remove() & .pop()
n = int(input())
set1 = set(map(int, input().split()))
m = int(input())
for i in range(m):
    lista = input().split()
    if (len(lista) == 1):
        eval("set1.{}()".format(lista[0]))
    else:
        if (int(lista[1]) in set1):
            eval("set1.{}({})".format(lista[0], lista[1]))
print(sum(set1))

#Set.union() Operation
n= int(input())
eng=set(map(int,input().split()))
m= int(input())
fra=set(map(int,input().split()))
print(len(eng.union(fra)))

#Set.intersection() Operation
n= int(input())
eng=set(map(int,input().split()))
m= int(input())
fra=set(map(int,input().split()))
print(len(eng.intersection(fra)))

#set.difference() Operation
n= int(input())
eng=set(map(int,input().split()))
m= int(input())
fra=set(map(int,input().split()))
print(len(eng.difference(fra)))

#Set.symmetric_difference() Operation
n= int(input())
eng=set(map(int,input().split()))
m= int(input())
fra=set(map(int,input().split()))
print(len(eng.symmetric_difference(fra)))

#Set Mutations
n = int(input())
A = set(map(int, input().split()))
m = int(input())
for i in range(m):
    command = input().split()
    B = set(map(int, input().split()))
    eval("A.{}({})".format(command[0], B))
print(sum(A))

#The Captain's Room
K= int(input())
rooms= list(map(int,input().split()))
cont=0
set_1=set()
set_2=set()
for elem in rooms:
    if(elem) in set_1:
        set_2.add(elem)
    else:
        set_1.add(elem)
print((set_1.symmetric_difference(set_2)).pop())

#Check Subset
test= int(input())
for i in range(test):
    m=int(input())
    A=  set(map(int,input().split()))
    n=int(input())
    B=set(map(int,input().split()))
    print(A.issubset(B))

#Check Strict Superset
A= set(map(int,input().split()))
n=int(input())
flag=True
for i in range(n):
    B= set(map(int,input().split()))
    if(not B.issubset(A) or len(B)>=len(A)):

        flag=False

print(flag)

#collections.Counter()
from collections import Counter
X= int(input())
numbers=list(map(int,input().split()))
dic=Counter(numbers)
money=0
N= int(input())
for i in range(N):
    customer=list(map(int,input().split()))
    if(dic[customer[0]]>0):
        dic[customer[0]]-=1
        money+=customer[1]
print(money)

#DefaultDict Tutorial
from collections import defaultdict
n,m= map(int,input().split())
B=[]
d= defaultdict(lambda:str(-1))


for i in range(n):
    A=str(input())
    if(d[A]=="-1"):
        d[A]=""
        d[A]=str(i+1)
    else:
        d[A]= d[A]+' '+str(i+1)


for i in range(m):
    B.append(input())

for elem in B:
    print(d[elem])

#Collections.namedtuple()
N= int(input())
cols=input().split()
index=0
for i in range(len(cols)):
    if(cols[i]=="MARKS"):
        index=i;
lista=[]
for i in range(N):
    lista.append(int(input().split()[index]))
print(sum(lista)/len(lista))

#Collections.OrderedDict()
from collections import OrderedDict
N= int(input())
dic=OrderedDict()
obj=''
price=0
for i in range(N):
    elem = input().split()
    if(len(elem)==2):
        obj=elem[0]
        price=int(elem[1])
    else:
        obj= ' '.join(elem[0:2])
        price=int(elem[2])
    if(obj not in dic):
        dic[obj]= price
    else:
        dic[obj]+=price
for key, value in dic.items() :
    print (key, value)

#Word Order
from collections import OrderedDict
N= int(input())
dic=OrderedDict()
for i in range(N):
    obj=input()
    if(obj not in dic):
        dic[obj]=1
    else:
        dic[obj]+=1
print(len(dic))
lista=[]
for key,values in dic.items():
    lista.append(str(values))
print(" ".join(lista))

#Collections.deque()
from collections import deque
n= int(input())
d=deque()
for i in range(n):
    lista= list(input().split())
    if(len(lista)==1):
        command=lista[0]
        eval("d.{}()".format(command))
    if(len(lista)==2):
        command=lista[0]
        param= str(lista[1])
        eval("d.{}({})".format(command,param))
print(*d)

#Company Logo

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    d = {}
    for elem in s:
        if (elem not in d):
            d[elem] = s.count(elem)
    lista = d.items()
    sorted_list = sorted(lista, key=lambda x: (x[1], -(ord(x[0]))), reverse=True)
    for item in sorted_list[0:3]:
        print(*item)
#Company Logo (different version)
def sorter(item):
    lettera = item[0]
    cont = item[1]
    return (cont, lettera)


if __name__ == '__main__':
    s = input()
    d = []
    l = []
    for elem in s:
        if (elem not in l):
            l.append(elem)
            d.append((-ord(elem), s.count(elem)))

    lista = sorted(d, key=sorter, reverse=True)
    for i in range(3):
        print(chr(-lista[i][0]), lista[i][1])

#Piling Up!
from collections import deque

d = deque()
n = int(input())
for i in range(n):
    n2 = int(input())
    lista = []
    d = deque(map(int, input().split()))
    k = -1
    flag = False
    for j in range(n2):
        if (d[0] >= d[-1]):
            current = d.popleft()
        else:
            current = d.pop()
        lista.append(current)
        if (flag):

            if (current > lista[k]):
                print("No")
                break
        k += 1
        flag = True
    if (len(lista) == n2):
        print("Yes")

#Calendar Module
import calendar
date=list(map(int,input().split()))
print(list(calendar.day_name)[(calendar.weekday(date[2],date[0],date[1]))].upper())

#Time Delta
def time_delta(t1, t2):
    date_1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    date_2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((date_1 - date_2).total_seconds())))

#Exceptions
for i in range(int(input())):

    try:
        a, b = map(int, input().split())
        print(int(a // b))
    except Exception as e:
        print("Error Code:", e)

#Zipped!
N,X= map(int,input().split())
lista=[i for i in range(N)]
subj=[]
for i in range(X):
    subj.append(list(map(float,input().split())))
scores=zip(*subj)
for elem in scores:
    print(sum(elem)/len(elem))

#Athlete Sort
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    lista=sorted(arr,key=lambda item: (item[k]))
    for elem in lista:
        print(*elem)

#ginortS
s=input()
lista=sorted(s,key=lambda x:(x.isdigit() and int(x)%2==0,x.isdigit() and int(x)%2==1,x.isupper(),x.islower(),x))
print(''.join(lista))

#Map and Lambda Function
cube = lambda x: x**3

def fibonacci(n):
    if(n==0):
        return []
    if(n==1):
        return [0]
    a=0
    b=1
    lista=[0,1]
    for i in range(n-2):
        c=a+b
        lista.append(c)
        a=b
        b=c
    return lista

#Detect floating point number
import re
n= int(input())
for i in range(n):
    s=input()
    print(bool(re.match('^[+-]?[0-9]*\.[0-9]+$',s)))

#Re.split()
regex_pattern = r"[,.]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#Group(),Groups() & Groupdict()
import re
s=input()
result=re.search(r'([a-z0-9])\1+',s)
print(result.group(1) if result else -1)

#Re.findall() & Re.finditer
import re
s=input()
pattern= r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})[qwrtypsdfghjklzxcvbnm]'
result=re.findall(pattern,s,re.I)
if(result):
    print("\n".join(result))
else:
    print('-1')

#Re.start() & Re.end()
import re
s= input()
k=input()
i=0
length_k=len(k)
length_s=len(s)

if(re.search(k,s)):
    while(length_k+i<length_s):
        result=re.search(k,s[i:])
        print((result.start()+i,result.end()+i-1))
        i+=result.start()+1
else:
    print((-1,-1))

#Regex substitution
import re
n=int(input())
for i in range(n):
    s=input()
    print(re.sub(r'(?<= )(&&|\|\|)(?= )',lambda x: "and" if x.group()=="&&" else "or",s))

#Validating roman numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#Validating phone numbers
import re
n=int(input())
for i in range(n):
    if(re.match(r'[789]\d{9}$',input())):
        print("YES")
    else:
        print("NO")

#Validating and parsing email addresses
import email.utils
import re
n= int(input())
pattern=r'<[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>'
for i in range(n):
    name,address=map(str,input().split(" "))
    result=re.match(pattern,address)
    if(result):
        print(name,address)

#Hex color code
import re
n=int(input())
pattern="(?:[:;\s])(#(?:[0-9a-fA-F]{3}){1,2})"
for i in range(n):
    css= input()
    result=re.findall(pattern,css)
    if(result):
        for elem in result:
            print(elem)

#HTML parser-part1
n= int(input())
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :',tag)
        for elem in attrs:
            print("->",elem[0],'>',elem[1])
    def handle_endtag(self, tag):
        print('End   :',tag)
    def handle_startendtag(self, tag, attrs):
        print('Empty :',tag)
        for elem in attrs:
            print("->",elem[0],'>',elem[1])
parser=MyHTMLParser()
for i in range(n):
    ht=input()
    parser.feed(ht)

#HTML parser-part2
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        string = data.split("\n")
        if (len(string) > 1):
            print(">>> Multi-line Comment")
            for elem in string:
                print(elem)
        else:
            print(">>> Single-line Comment")
            print(string[0])

    def handle_data(self, data):
        if (data != "\n"):
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Detect HTML Tags, Attributes and Attribute Values
n= int(input())
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for elem in attrs:
            print("->",elem[0],'>',elem[1])
    def handle_endtag(self, tag):
        return
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for elem in attrs:
            print("->",elem[0],'>',elem[1])
parser=MyHTMLParser()
for i in range(n):
    ht=input()
    parser.feed(ht)

#Validating UID helped
import re
n=int(input())
for i in range(n):
    UID = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2,}', UID)
        assert re.search(r'[0-9]{3,}', UID)
        assert not re.search(r'[^a-zA-Z0-9]', UID)
        assert not re.search(r'(.)\1', UID)
        assert len(UID) == 10
    except:
        print('Invalid')
    else:
        print('Valid')

#Validating Credit Card Numbers
import re
n=int(input())
pattern='^[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}'
pattern2='^[456][0-9]{15}'
for i in range(n):
    Cc=input()
    if((re.match(pattern,Cc) or re.match(pattern2,Cc)) and (len(Cc)==16 or len(Cc)==19)        and not re.search(r"([\d])\1\1\1", Cc.replace("-", ""))):
        print('Valid')
    else:
        print('Invalid')

#Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"([0-9])(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#Matrix Script

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
final=''
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
string=zip(*matrix)
for elem in string:
    final+=''.join(elem)
print(re.sub("(?<=\w)([^\w]+)(?=\w)",' ',final))

#XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    total=0
    for elem in node.iter():
        total+=len(elem.attrib)
    return total
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if(level==maxdepth):
        maxdepth+=1
    for child in elem:
        depth(child,level+1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#72 Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        number=[]
        for elem in l:
            number.append(elem[-10:])
        number.sort()
        for num in number:
            print("+91"+' '+str(num[0:5])+" "+str(num[-5:]))
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

#Decorators 2 - Name Directory
import operator


def person_lister(f):
    def inner(people):
        lista=sorted(people,key=lambda x: int(x[2]))
        for person in lista:
            yield f(person)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

#Arrays
import numpy

def arrays(arr):
    arr.reverse()
    return numpy.array(arr,float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#Shape and Reshape
import numpy
lista=list(map(int,input().split()))
arr=numpy.array(lista,int)
print(numpy.reshape(arr,(3,3)))

#Transpose and Flatten
import numpy as np
n,m=map(int,input().split())
matrix=np.array([input().split() for i in range(n)],int)
print(np.transpose(matrix))
print(matrix.flatten())

#Concatenate
import numpy as np
n,m,p= map(int,input().split())
arr_1=np.array([input().split() for i in range(n)],int)
arr_2=np.array([input().split() for i in range(m)],int)
print(np.concatenate((arr_1,arr_2),axis=0))

#Zeros and Ones
import numpy as np
dim=list(map(int,input().split()))
print(np.zeros(([dim[i] for i in range(len(dim))]),int))
print(np.ones(([dim[i] for i in range(len(dim))]),int))

#Eye and Identity
import numpy as np
n,m= map(int,input().split())
print(np.eye(n,m))

#Array Mathematics
import numpy
n,m=map(int,input().split())
a=numpy.array([input().split() for i in range(n)],int)
b=numpy.array([input().split() for i in range(n)],int)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)

#Floor, Ceil and Rint
import numpy as np
np.set_printoptions(sign=' ')
arr=np.array(input().split(),float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))

#Sum and Prod
import numpy as np
n,m=map(int,input().split())
a=np.array([input().split() for i in range(n)],int)
somma=np.sum(a,axis=0)
print(np.prod(somma))

#Min and Max
import numpy as np
n,m=map(int,input().split())
a=np.array([input().split() for i in range(n)],int)
minim=np.min(a,axis=1)
print(np.max(minim))

#Mean, Var, and Std
import numpy as np
np.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
a=np.array([input().split() for i in range(n)],int)
print(np.mean(a,axis=1))
print(np.var(a,axis=0))
print(np.std(a))

#Dot and Cross
import numpy as np
n=int(input())
a=np.array([input().split() for i in range(n)],int)
b=np.array([input().split() for i in range(n)],int)
print(np.dot(a,b))

#Inner and Outer
import numpy as np
a=np.array(input().split(),int)
b=np.array(input().split(),int)
print(np.inner(a,b))
print(np.outer(a,b))

#Polynomials
import numpy as np
a=np.array(input().split(),float)
value=int(input())
print(np.polyval(a,value))

#Linear Algebra
import numpy as np
np.set_printoptions(legacy='1.13')
n=int(input())
a=np.array([input().split() for i in range(n)],float)
print(np.linalg.det(a))

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





































