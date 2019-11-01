'''
Question
Write some code, that will flatten an array of arbitrarily nested arrays of integers into a flat array of integers.
e.g. [[1,2,[3]],4] -> [1,2,3,4]. Your solution should be a link to a gist on gist.github.com with your implementation.

Solution
We create the 'Flattener' class. Objects of the class can call its 'flatten_list' method which would return a one dimensioned (flat) array
containing contents of the original array passed .
Kindly read the code comments to understand the algorithm
Thank you.
'''
class Flattener(object):
    def __init__(self):
        #list to store the flattened cells of arrgument array
        self.result = []

    def flatten_list(self,arg_array):
        #check array is valid 
        if len(arg_array) <= 0:
            return None
 
        #loop over each element of argument array
        for item in arg_array:
            if type(item) == list:

                self.flatten_list(item)
            else:
                self.result.append(item)
        return self.result

#RUN TEST BY TYPING THE FOLLOWING COMMANDS 
# $ python test_flattener.py

