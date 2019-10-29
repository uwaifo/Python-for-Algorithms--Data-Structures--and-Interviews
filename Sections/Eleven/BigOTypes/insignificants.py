myList = [1,2,3]
def print_once(lst):
    for val in lst:
        print(val)

#print_once(myList)#linear



#insignificant 
def print_2(lst):
    for item in lst:
        print(item)
    for item in lst:
        print(item)

#print_2(myList)
#Complexity = O(2n)

'''
We can see that the first function will print O(n) items and the second will print O(3n) items. 
However for n going to inifinity the constant can be dropped, since it will not have a large effect,
 so both functions are O(n).
'''

def comp(lst):
    #This function prints the first item O(1)
    print(lst[0])

    #establish midpoint
    midpoint = len(lst) / 2
    #print(midpoint)
    #    Then is prints the first 1/2 of the list O(n/2)
    for item in lst[:int(midpoint)]:
        print(item)
    
    for x in range(10):
        print("number")


#Complexity = O(1 + n/2 + 10)

compLst = [1,2,3,4,5,6,7,8,9,10]
#comp(compLst)

'''
So let's break down the operations here. We can combine each operation to get the total Big-O of the function:
𝑂(1+𝑛/2+10)
We can see that as n grows larger the 1 and 10 terms become insignificant and the 1/2 term multiplied against n will also not have much of an effect as n goes towards infinity. This means the function is simply O(n)!
'''


def matcher(lst,match):
    for item in lst:
        if item == match:
            return True
    return False

print(matcher(compLst,6))
print(matcher(compLst,16))

'''
Note that in the first scenario, the best case was actually O(1), since the match was found at the first element. In the case where there is no match, every element must be checked, this results in a worst case time of O(n). Later on we will also discuss average case time.

Finally let's introduce the concept of space complexity.
'''