#Exclusive or 

def find_missing_number(arr1,arr2):
    result = 0
    #print(arr1 + arr2)

    #perform XOR on values of both arrays
    for item in arr1 + arr2:
        result^=item
        #print(result)
    
    return result


arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(find_missing_number(arr1,arr2))
#print(find_missing_number([1,2,3,4,5,6,7],[3,7,2,1,4,6]))#5
#print(find_missing_number([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))#6
