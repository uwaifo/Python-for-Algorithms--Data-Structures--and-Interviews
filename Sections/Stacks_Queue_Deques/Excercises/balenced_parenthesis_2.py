'''
Given a string of opening and closing parentheses, check whether it’s balanced. 
We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. 
Assume that the string doesn’t contain any other character than these, no spaces words or numbers. 
As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. 
For example ‘([])’ is balanced but ‘([)]’ is not.
You can assume the input string has no spaces.
''' 

def balance_check(s):
    #check that s is a pair
    if len(s) % 2 != 0:
            return False
    #create a stack
    stack = []
    #define a dictionary of  matching pairs
    matching_pairs = {')':'(',']':'[','}':'{'}
    print(len(matching_pairs))
    
    for each in s:  
        #if the content of s is valid   
        if each in matching_pairs:
            #pop it off the stack and 
            if stack.pop() != matching_pairs[each]:
                return False
        else:
            
            stack.append(each)
    return stack == []
        
    

print(balance_check('[]'))
#print(balance_check('[](){([[[]]])}'))
#print(balance_check('[](){([[[]]])}'))




'''
caller = Stack()
caller.push('[')
caller.push(']')

print(caller.isEmpty())
print(caller.peek_top())
print(caller.peek_buttom())
print(caller.size())
caller.pop()
print(caller.size())


        

#txt = "}"[::-1]
#print(txt)
'''