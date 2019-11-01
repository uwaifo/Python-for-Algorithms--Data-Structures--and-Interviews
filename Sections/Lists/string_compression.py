'''
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
For this problem, you can falsely "compress" strings of single or double letters. 
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.


'''
import collections
def compress(s):
    letter_store = collections.defaultdict(int)
    result = ''

    for letter in s:
        #print(letter)
        letter_store[letter] += 1
    
    for sl in letter_store:
        result += sl+ str(letter_store[sl])
    return result
        

    
print(compress('aabbCCDD'))
print(compress('AAAAABBBBCCCC'))#'A5B4C4'
print(compress('AAABCCDDDDD')) #A3B1C2D5
print(compress('AABBCC')) # A2B2C2
