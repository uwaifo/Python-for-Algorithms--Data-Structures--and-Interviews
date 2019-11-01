'''
So both silutions bellow are quadratic
see vfind_with_collections.py for linear solution 0(n)
'''

def find_missing_number(arr1,arr2):
    #understand that in many such questions it would be wise to sanitize
    #the arguments such sorting, removing white spaces , making lowercase etc   
    
    
    #sort arrays
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1

    #otherwise return the last element of the first array
    return arr1[-1]


arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(find_missing_number(arr1,arr2))
# print(find_missing_number([1,2,3,4,5,6,7],[3,7,2,1,4,6]))#5
# print(find_missing_number([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))#6


    


#Bellow is a naive solution as it pays no mind to the posibilitiy of having duplicates

def finder(arr1,arr2):

    # check for in-equality in arguments
    if len(arr1) == len(arr2):
        return

    for item in arr1:
        #print(item)
        if item not in arr2:
            return item


'''
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(finder(arr1,arr2))
print(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]))#5
print(finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))#6
'''
#Complexity = O(n) Linear both space and time 