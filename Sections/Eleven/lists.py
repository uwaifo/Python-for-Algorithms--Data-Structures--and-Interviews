import timeit
def method_1():
    l = []
    for n in range(10000):
        l = l + [n]

def method_2():
    l = []
    for n in range(10000):
        l.append(n)

def method_3():
    l = [n for n in range(10000)]

def method_4():
    l = list(range(10000))


# print(timeit.timeit(method_1)) 
# print(timeit.timeit(method_2)) 
# print(timeit.timeit(method_3)) 
# print(timeit.timeit(method_4)) 
'''
Lists

In Python lists act as dynamic arrays and support a number of common operations through methods called on them. The two most common operations performed on a list are indexing and assigning to an index position. These operations are both designed to be run in constant time, O(1).

Let's imagine you wanted to test different methods to construct a list that is [0,1,2...10000]. Let go ahead and compare various methods, such as appending to the end of a list, concatenating a list, or using tools such as casting and list comprehension.
'''


d = {'k1':1,'k2':2,'s1':1000}
print(d['s1'])
'''
dictionaries and lists are basically hashtables and dynamic arrays

'''
'''
Operation 	Big-O Efficiency
index [] 	O(1)
index assignment 	O(1)
append 	O(1)
pop() 	O(1)
pop(i) 	O(n)
insert(i,item) 	O(n)
del operator 	O(n)
iteration 	O(n)
contains (in) 	O(n)
get slice [x:y] 	O(k)
del slice 	O(n)
set slice 	O(n+k)
reverse 	O(n)
concatenate 	O(k)
sort 	O(n log n)
multiply 	O(nk)
'''
