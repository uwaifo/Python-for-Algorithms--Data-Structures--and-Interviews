class Solution(object):
    def __init__(self):
        pass 
        
    def anagram2(self,str_1, str_2):

        #remove space and 
        str_1 = str_1.replace(' ', '').lower()
        str_2 = str_2.replace(' ', '').lower()

        #check for length equality
        if len(str_1) != len(str_2):
            return False

        #couting dictionary
        #to store letters and count its number of occourances
        counter = {}

        for letter in str_1:
            #if such letter has been inputed into the counter
            if letter in counter:
                #update its count by one
                counter[letter] += 1
            else: 
                #the counter has no such letter and we start its ocourance by one
                counter[letter] = 1
        
        #Now that we have filled the counter with the letters and its ocourances
        #print(counter)
        # for item in counter:
        #     print(item)
        #Reverse previous and empt the dict
        for letter in str_2:
            if letter in counter:
                counter[letter] -= 1
            else:
                counter[letter] = 1
        for item in counter:
            if counter[item] != 0:
                return False

        return True


            
caller = Solution()
print(caller.anagram2('clint eastwood','old west action'))
print(caller.anagram2('same', 'ema s'))
print(caller.anagram2('aa', 'bb'))
