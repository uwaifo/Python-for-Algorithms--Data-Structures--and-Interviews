def func_quad(arg_list):
    for item_1 in arg_list:
        for item_2 in arg_list:
            print(item_1,item_2)

smallList = [1,2,3]
func_quad(smallList)

#Complexity = O(n)2  or O(n^2)

'''
Note how we now have two loops, one nested inside another. This means that for a list of n items, we will have to perform n operations for every item in the list! This means in total, we will perform n times n assignments, or n^2. So a list of 10 items will have 10^2, or 100 operations. You can see how dangerous this can get for very large inputs! This is why Big-O is so important to be aware of!
'''