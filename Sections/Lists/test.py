def twoNumberSum(array, targetSum): 
    store_potentials = {}
    for item_1 in array:
        next_target = targetSum - item_1
        if next_target in store_potentials:
            return sorted([next_target, item_1])

        else:
            store_potentials[item_1] = True
    return []

		
    # Write your code here.
my_array = [3,5-5,8,11,1,-1,6]
print(twoNumberSum(my_array, 10))

#array[item_1], array[item_2]]