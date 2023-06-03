#Q1
''' keyword def is used to create a function we use for example'''
def functions():
    print('this is a function using keyword def withour any parameters and return type it just prints some strings')
def odd_num(n):
    for nums in range(n):
        if(nums % 2 != 0):
            print(nums)

odd_num(25)
functions()

#Q2
'''(*args) and (**kwargs) are the special keywords in python whereas 
args with star is used to pass variable length arguments to the function while
**kwargs is used to key-value aka dictionary based arguments to the function  '''
def fun1(*args):
    for args in args:
        print(args)

fun1('newton', 'hero', 'dieheart', 'fan')   

def fun2(**kwargs):
    for key, value in kwargs.items():
        print(key,'=', value)

fun2(hero = 'dhoni', leader = 'mahi', csk = 'final', mi = 'lost')

#Q3
'''iterator is an object that contains all the values of of an iterable object say
string s = 'newtoncse' so string is an iterable object and it returns an iterator object thru
iter() function'''
str1= 'newtoncse'
iter1 = iter(str1)
print(next(iter1))
print(next(iter1))
"string is an iterable object simpilary with tuples , lists "
#lets take examples of tuples..
tuple1 = (1, 3, 4, 'newton', 'hero')
iters = iter(tuple1)
print(next(iters))
'''we use iter( ) and next() methods respectively to iterator object and for iternation'''
list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
iter1 = iter(list1)

for i in range(5):
    print(next(iter1))



#Q4
'''generator function is a function in python to generate list of numbers in iterable form..
so generator function does not store values in memory so whenever we have to generate list of values then 
we use yield to generate the values, we can use next to iterate to the next values...
'''
def generate(n):
    for i in range(n):
        yield i
x = generate(10) #it generates the sequence of numbers and returns refrence to iterators 
print(x)        
#we can traverse the values using loop or next()
for i in x:
    print(i)

#Q5
import math

def isprime(n):
    yield 2
    count = 3
    while count < n:
        j = 2
        isprime = True
        while j < int(math.sqrt(count)) +1:
            if(count % j == 0):
                isprime = False
                break
            j += 1
        if isprime :
            yield count

        count +=2   
print('primss')
for i in isprime(20):
    print(i, " ")        

#Q6
def fibnicci(n):
    a = 0 
    b = 1
    print(a)
    while b < n:
        a, b = b, a+b
        print(a)


fibnicci(10)       

#Q7
str2 = 'pwskills'
print([x for x in str2])

#Q8
def ispalindrome(n):
    temp = 0
    num2= n
    while(num2):
        dig = num2 % 10
        temp = temp *10 + dig
        num2 = num2//10
        
    if(n == temp):
        print("yes palindrome")
    else:
        print("not a palindrome")

ispalindrome(121)

#Q9
print([x for x in range(101) if x % 2 != 0])
       
