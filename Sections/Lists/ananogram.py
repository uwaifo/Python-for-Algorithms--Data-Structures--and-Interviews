'''
Given two strings, check to see if they are anagrams.
An anagram is when the two strings can be written using the exact same letters 
(so you can just rearrange the letters to get a different phrase or word).
For example:

"public relations" is an anagram of "crap built on lies."
"clint eastwood" is an anagram of "old west action"
Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".
'''

class AnanogramCheck(object):
    def __init__(self):
        pass

    def checker(self,str_1,str_2):
        #remove whitespaces and lowercase all
        str_1 = str_1.replace(' ', '').lower()
        str_2 = str_2.replace(' ','').lower()
    

        return sorted(str_1) == sorted(str_2)
        result = False

        #check that both args are valod strings
        if not (len(str_1) == len(str_2)):
            return result

        for item_1 in str_1:
            if item_1 in str_2:
                str_2 =  str_2.replace(item_1,'')
                 
            
        if len(str_2) == 0:
            result = True

        return result
            
#original question format 
'''
def anagram(s1,s2):
    
    pass
'''
        
        
tester = AnanogramCheck()

print(tester.checker('ma se', 'same'))#true
print(tester.checker('clint eastwood','old west action'))# true
print(tester.checker('aa','bb'))#false
