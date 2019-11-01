'''
Given a string,determine if it is compreised of all unique characters. 
For example, the string 'abcde' has all unique characters and should return True. 
The string 'aabcde' contains duplicate characters and should return false.
'''

import collections
def uni_char(s):
    char_counter = collections.defaultdict(int)
    result = True

    for letter in s:
        char_counter[letter] += 1
    
    for letter in char_counter:
        #print(char_counter[letter])
        if char_counter[letter] > 1:
            result = False
            return result

    return result

    

print(uni_char('goo'))#false
print(uni_char('abcdefg'))#True 