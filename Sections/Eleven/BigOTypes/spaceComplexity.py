def printer(n=10):#constant args
    for x in range(n):
        print("Hello Ralph")

#printer()

#Space complexity = O(1) constant
#Time complexity = O(n) linear
'''

Note how we only assign the 'hello world!' variable once, not every time we print.
So the algorithm has O(1) space complexity and an O(n) time complexity. 
'''


def create_list(n):
    new_list = []
    for item in range(n):
        new_list.append(item)
    return new_list
print(create_list(5))   

#Time complexity = O(n)  constant
#Space complexity = O(n) linear
'''
Note how the size of the new_list object scales with the input **n**, this shows that it is an O(n) algorithm with regards to **space** complexity.
_____

Thats it for this lecture, before continuing on, make sure to complete the homework assignment below: 
'''