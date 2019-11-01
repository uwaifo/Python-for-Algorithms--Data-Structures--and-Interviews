
import  collections

def find_missing_number(arr1, arr2):

    #automatically add key to dictionary if it doesnt exist ie no throwing of missingg kety error
    d = collections.defaultdict(int)

    #loop through array
    for num in arr2:
        #auto-added if not in dictionary
        #if in dictionary and to re-occourance
        d[num] += 1
    
    return d

    for num in arr1:
        if d[num] ==0:
            return num
        else:
            d[num] -= 1 
         
    # arr1.sort()
    # arr2.sort()

    # for num1,num2 in zip(arr1,arr2):
    #     if num1 != num2:
    #         return num1

    # return arr1[-1]


arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(find_missing_number(arr1,arr2))
#print(find_missing_number([1,2,3,4,5,6,7],[3,7,2,1,4,6]))#5
#print(find_missing_number([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))#6

